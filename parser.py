from datetime import datetime
import re
import os

from model import *
import constants as c

__version__ = '0.1'
 
class ScheduleNotFoundError(Exception):
	def __init__(self):
		self.message = 'Schedule not found'

class tNavigatorModelParser(object):
    '''Класс tNavigatorModelParser: Позволяет парсить данные их файлов ГДМ
    basepath: str полный путь к главному файлу модели (*.data)'''
    def __init__(self, basepath:str) -> None:
        self.__basepath = os.path.normpath(basepath)
        self.start = None
        self.file_with_schedule_section = None
        self.file_with_start_date = None
        self.schedule_lines = self.find_schedule_section(basepath)
        if len(self.schedule_lines) == 0:
            raise ScheduleNotFoundError 

    @property   
    def basepath(self):
        '''Путь к гдавному файлу модели'''
        return self.__basepath
    
    @staticmethod
    def read_lines(path: str):
        '''Прочитать значения из файла
        path: str - путь к файлу'''
        if os.path.exists(path):
            with open (path, 'r') as file:
                lines = file.readlines()
            return lines
        else:
            return []
        
    def find_schedule_section(self, path: str) -> list:
        '''Рекурсивный поиск секции SCHEDULE. Возвращает набор строк секции 
        (используется для определения стартовой даты и файла, в котором начинается секция SCHEDULE)
        path: str - путь к файлу, в котором осуществляется поиск'''
        lines = tNavigatorModelParser.read_lines(path)
        if len(lines) > 0:
            find_start = False
            find_include = False
            inc_list=[]
            start_i=-1
            end_i=-1
            for i, line in enumerate(lines):
                # ищем стартовую дату (она одна, в файле с расширением *.DATA)
                if re.match(r"(?i)(^\s*START)|(^\s*RESTARTDATE)", line):
                    find_start = True                
                if find_start and re.match(c.date_pattern, line):
                    self.file_with_start_date = path
                    start = re.search(c.date_pattern, line)
                    self.start = datetime(int(start.group('year')), 
                                 c.months_dict[start.group('month').upper()], 
                                 int(start.group('day')))
                    find_start = False
                
                # ищем секцию SCHEDULE, она одна, но может быть как в первом файле, так и в INCLUDE любой вложенности (НО ТОЛЬКО ОДИН РАЗ)
                if re.match(r"(?i)^\s*INCLUDE", line): 
                    find_include = True
                # запоминаем встречающиеся инклюды, на случай, если секции SCHEDULE не будет в файле *.DATA
                if find_include and re.match(c.include_pattern, line):
                    value = re.search(c.include_pattern, line).group()
                    inc_list.append(value)
                    find_include = False

                # если встречаем SCHEDULE, то запоминаем индекс строки
                if re.match(r"(?i)^\s*SCHEDULE", line): start_i = i

                # если встречаем уже встретили SCHEDULE и встречает END, то запоминаем индекс строки    
                if re.match(r"(?i)^\s*END", line) and start_i >=0: end_i = i
                
                if start_i>=0:
                    self.file_with_schedule_section = path
                    return lines[start_i:] if end_i<0 else lines[start_i:end_i+1] 

            # если не встретилась секция в первом фйале, то рекурсивно проходим по всеи INCLUDE, пока не встретиться секция SCHEDULE
            for inc in inc_list:
                sch_lines = self.find_schedule_section(os.path.normpath(os.path.join(os.path.dirname(self.basepath), inc)))
                if len(sch_lines) > 0:
                    return sch_lines
        # если совсем ничего не найдено - возвращаем пустой список
        return []

    def build_model(self) -> tNavigatorModel:
        '''Строит модель из  SCHEDULE секции указанного в конструкторе файла
        Возвращает класс модели tNavigatorModel'''
        kwlist = self.parse_schedule_section() 
        model = tNavigatorModel(self.start, kwlist, self.file_with_schedule_section)  
        return model         
    

    def __get_keywords_list(self, lines: list, path: str, keywords_list: list, index: int = 0, use_recursion:bool = True):
        '''Получает список ключевых слов. При use_recursion = True Рекурсивно вызывается для секций INCLUDE
        lines: list - список строк, которые парсятся
        path: str - относительный пусть файлу, из которого эти строки ('' -  для первого файла)
        keywords_list: list of tNavigatorKeyword - список объектов ключевых слов'''
        if keywords_list == None:
            keywords_list = []
        tNav_kw = None
        for line in lines:
            re_kw = re.search(c.keyword_pattern, line)
            if re_kw:
                kw = re_kw.group('keyword').upper()
                if kw in c.keywords:
                    tNav_kw_class = tNavigatorModel.get_keyword_class(kw)
                    tNav_kw = tNav_kw_class(kw, path)
                    # keywords_list.append(tNav_kw)
                    keywords_list.insert(index, tNav_kw)
                    index += 1 
            if tNav_kw != None:
                tNav_kw.add_line(line)

        # проходим по всем инклюдам и рекурсивно выполняем те же действия
        if use_recursion:
            inc_list = [x for x in keywords_list if x.name == 'INCLUDE' and x.include_path == path]
            for inc in inc_list:
                index = keywords_list.index(inc)
                value = inc.get_value()
                if value != None:
                    inc_path = os.path.normpath(os.path.join(os.path.dirname(self.basepath), value))
                    lines = tNavigatorModelParser.read_lines(inc_path)
                    self.__get_keywords_list(lines, value, keywords_list, index+1)

    def parse_schedule_section(self):
        '''Парсинг SCHEDULE секции. Возвращает список объектов ключевых слов lisf of tNavigatorKeyword'''
        keywords_list = []
        self.__get_keywords_list(self.schedule_lines, '/', keywords_list)
        return keywords_list
    
   
    def get_keywords_list(self, path: str):
        '''Получает список ключевых слов из файла
        paht:str - путь к файлу из которого необходимо получить ключевые слова'''
        lines =  tNavigatorModelParser.read_lines(path)
        keywords_list = []
        self.__get_keywords_list(lines, '', keywords_list, use_recursion=False)
        return keywords_list

if __name__ == '__main__':
    print(tNavigatorModelParser.__doc__)



        