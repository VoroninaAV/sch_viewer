from datetime import datetime, date, time, timedelta
import re
import constants as c

__version__ = '0.1'

class tNavigatorKeyword(object):
    '''Класс tNavigatorKeyword: Описывает одно ключевое слово  
    name: str - название ключевого слова
    include_path: str = '' - относительный путь к файлу, в котором содержится это ключевое слово'''
    def __init__(self, name: str, include_path: str = '')  -> None:
        self.__name = name.upper()
        self.__include_path = include_path if include_path != None else ''
        self.body = []

  
    @property
    def name(self):
        '''Ключевое слово'''
        return self.__name

    @property
    def include_path(self):
        '''Относительный путь к файлу, в котором содержится это ключевое слово (для *.DATA файла путь = '/')'''
        return self.__include_path
    
    @include_path.setter
    def include_path(self, include_path):
        '''Относительный путь к файлу, в котором содержится это ключевое слово'''
        self.__include_path=include_path

    def add_line(self, line: str):
        '''Добавить строку в body
        line: str - строка, которая будет добавлена'''
        if not line.endswith('\n'):
            line = line+'\n'
        self.body.append(line)

    def get_body_text(self) -> str:
        '''Получить полный текст ключевого слова'''
        return "".join(self.body)

    def set_body_text(self, text: str):
        '''Установить текст ключевого слова
        text: str - текст ключевого слова, разжеленный Enter'''
        self.body = text.splitlines(keepends=True)

    # def get_body_value_text(self) -> str:
    #     '''Получить текст ключевого слова БЕЗ ключевого слова и комментариев'''
    #     s = ''
    #     for line in self.body[1:]:
    #         s += line[:line.index('--')]
    #     return s

    def get_body_text_without_keyword(self) -> str:
        '''Получить текст ключевого слова БЕЗ ключевого слова'''
        return "".join(self.body[1:])

    def get_value(self):
        '''Получить значение ключевого слова'''
        pass

    def __str__(self) -> str:
        return f"Путь к файлу: {self.include_path}\nТекст кочевого слова:\n{self.get_body_text()}"
    
    def get_comment(self) -> str:
        '''Получить коментарий ключевого слова. Берется только первый коментарий, сразу после ключевого слова'''
        search = re.search(c.keyword_pattern, self.get_body_text(), re.MULTILINE)
        return search.group('comment') if search else None
    
    # TODO is_correct не реализовано, должно быть переопределено в дочерних классах
    def is_correct(self) -> bool:
        '''Проверка на корректность ключевого слова'''      
        # 1. начинается c ключевого слова и это ключевое слово == self.name
        # 2. каждое значение заканчивается символом /
        # 3. ключевое слово заканчивается символом / (за исключением тех, что в списке keywords_without_slash_symbol)
        return len(self.body)>0

class DATES(tNavigatorKeyword):
    '''Класс DATES(tNavigatorKeyword): Описывает ключевое слово DATES'''
    def __init__(self, name: str='DATES', include_path='') -> None:
        if name == 'DATES':
            super().__init__(name, include_path)
        else: 
            raise KeyError

    def get_value(self) -> datetime:
        s = self.get_body_text_without_keyword()
        dt = re.search(c.date_pattern, s, re.MULTILINE)
        if dt:
            day = dt.group('day')
            month = dt.group('month').upper()
            year = dt.group('year')
            d = date(int(year), c.months_dict[month], int(day))
            time_str = dt.group('time')
            t = time()
            if time_str != None: 
                format = '%H:%M:%S.%f' if '.' in time_str else '%H:%M:%S'
                t = datetime.strptime(time_str.replace(' ',''), format).time()
            return datetime.combine(d, t)
        else:
            return None
    
    def set_value(self, date: datetime):
        def keys_with_value(dictionary, value, default=None):
            return [k for k, v in dictionary.items() if v == value]
        self.set_body_text(f"DATES\n{date.day} '{keys_with_value(c.months_dict, date.month)[0]}' {date.year} /\n/\n")
        pass

'''Класс INCLUDE(tNavigatorKeyword): Описывает ключевое слово INCLUDE'''
class INCLUDE(tNavigatorKeyword):
    def __init__(self, name='INCLUDE', include_path='') -> None:
        if name == 'INCLUDE':
            super().__init__(name, include_path)
        else: 
            raise KeyError

    def get_value(self) -> str:
        search = re.search(c.include_pattern, self.get_body_text(), re.MULTILINE)
        if search:
            return search.group('path')
        else:
            print(f'В тексте ключевого слова {self.name} ошибка\n{self}')
            return None

'''Класс TSTEP(tNavigatorKeyword): Описывает ключевое слово TSTEP'''
class TSTEP(tNavigatorKeyword):
    def __init__(self, name='TSTEP', include_path='') -> None:
        if name == 'TSTEP':
            super().__init__(name, include_path)
        else: 
            raise KeyError

    def get_value(self) -> timedelta:
        search = re.findall(c.tstep_pattern, self.get_body_text(), re.MULTILINE) 
        sum = 0
        for str in search:
            days = float(str[-2])
            n = 1 if (str[-3] == '') else int(str[-3])
            sum += days*n
        return timedelta(sum)

# TODO реализовать WEFAC
# WEFAC
# P25 .89 NO /
# P12 .7 /
# P13 .8 /
# I* .97 /
# /
class WEFAC(tNavigatorKeyword):
    def __init__(self, name = 'WEFAC', include_path='') -> None:
        '''WEFAC(tNavigatorKeyword) - ключевое слово определяет коэффициент эксплуатации для скважин.
Одна строка данных содержит следующие параметры:
1. название скважины, или список скважин, заданный ключевым словом WLIST,
2. коэффициент эксплуатации (доля времени, в течение которого скважина работает).
Коэффициент эксплуатации скважины должен быть больше нуля, иначе он будет
проигнорирован и взят по умолчанию;
По умолчанию: 1.
3. учитывать ли коэффициент эксплуатации при расчете потоков в ветвях и по-
терь давления в расширенной сети (BRANPROP, NODEPROP):
• YES – Потери давления в ветвях в расширенной сети рассчитываются с ис-
пользованием среднего по времени дебита скважины (дебита, умноженного
на коэффициент эксплуатации).
• NO – Потери давления в ветвях в расширенной сети рассчитываются с ис-
пользованием максимального дебита скважины (дебит не умножается на ко-
эффициент эксплуатации);
• По умолчанию: YES.'''
        if name == 'WEFAC':
            super().__init__(name, include_path)
        else: 
            raise KeyError

    def get_value(self):
        pass

if __name__ == '__main__':
    print(tNavigatorKeyword.__doc__)    