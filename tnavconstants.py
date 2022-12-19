re_pattern = {
    'keyword' : r"(?i)^\s*(?P<keyword>\w+)\s*(--(?P<comment>.*)){0,1}",
    'DATES' : r"(?i)^\s*(?P<day>\d{1,2})\s*('?(?P<month>[A-Z]{3})'?)\s*(?P<year>\d{4})(\s+(?P<time>\d{2}:\d{2}:\d{2}([.]\d{4})?))?\s*/",
    'TSTEP' : r"((?P<n>\d+)[*])?(?P<days>(\d*[.])?\d+)",
    'INCLUDE' : r"^\s*'(?P<path>.+)'\s*\/", 
    'WEFAC' : r"(?i)'?(?P<well>(\w|[*])+)'?\s+(?P<coef>1|0?.\d*|(\d*).?\d+E(-|[+])\d+)\s*'?(?P<use>(NO|YES)?)'?\s*/",
    'GEFAC' : r"(?i)'?(?P<group>(\w|[*])+)'?\s+(?P<coef>1|0?.\d*|(\d*).?\d+E(-|[+])\d+)\s*'?(?P<use>(NO|YES)?)'?\s*/"
}

months_dict = {
    'JAN' : 1,
    'FEB' : 2,
    'MAR' : 3,
    'APR' : 4,
    'MAY' : 5,
    'JUN' : 6,
    'JUL' : 7,
    'JLY' : 7,
    'AUG' : 8,
    'SEP' : 9,
    'OCT' : 10,
    'NOV' : 11,
    'DEC' : 12
} 

keywords = {'ACF', 'ACFS', 'ACTDIMS', 'ACTION', 'ACTIONG', 'ACTIONR', 'ACTIONW', 'ACTIONX', 'ACTNUM', 'ADD', 'ADDREG', 'ADDZCORN', 'ADSALNOD', 'ADSORP', 'AIM', 'AIMFRAC', 'AIMPVI', 'ALKADS', 'ALKALINE', 'ALKROCK', 'ALPHA', 
'ALPHAD', 'ALPHAI', 'ALPHANUD', 'ALPHANUI', 'ALPHANUM', 'ALPOLADS', 'ALSURFAD', 'ALSURFST', 'AMALGAM', 'AMF', 'AMFVD', 'API', 'APIGROUP', 'APILIM', 'APIVD', 'AQANCONL', 'AQANTRC', 'AQSTREAW', 'AQUANCON', 'AQUCHWAT', 
'AQUCON', 'AQUCT', 'AQUDIMS', 'AQUFET', 'AQUFETP', 'AQUFLUX', 'AQUNUM', 'AQUTAB', 'ASPDEPO', 'ASPFLRT', 'ASPHALTE', 'ASPLCRT', 'ASPP', 'ASPP', 'ASPPW', 'ASPREWG', 'ASPVISO', 'BDENSITY', 'BIC', 'BICS', 
'BIGMODEL', 'BIOTC', 'BLACKOIL', 'BOX', 'BRANPROP', 'BRINE', 'CALTRAC', 'CALVAL', 'CALVALR', 'CARFIN', 'CART', 'CATYPE', 'CBMOPTS', 'CCTYPE', 'CCTYPES', 'CECON', 'CGDTYPE', 'CGVTYPE', 'CNAMES', 'CO', 
'COAL', 'COALNUM', 'COARSEN', 'CODTYPE', 'COMPDAT', 'COMPDATL', 'COMPDATM', 'COMPINJK', 'COMPLMPL', 'COMPLUMP', 'COMPMBIL', 'COMPMOBI', 'COMPOFF', 'COMPORD', 'COMPRP', 'COMPS', 'COMPSEGL', 'COMPSEGS', 'COMPVD', 'COMPW', 
'COORD', 'COORDSYS', 'COPY', 'COPYBOX', 'COPYREG', 'COVTYPE', 'CREF', 'CREFW', 'CREFWS', 'CSKIN', 'CVCRIT', 'CVTYPE', 'CVTYPES', 'CWTYPE', 'DATES', 'DATUM', 'DATUMR', 'DATUMRX', 'DCQDEFN', 'DELAYACT', 
'DENSITY', 'DEPTH', 'DETAILMF', 'DETAILVD', 'DGRDT', 'DIFFC', 'DIFFCBM', 'DIFFCGAS', 'DIFFCGO', 'DIFFCOAL', 'DIFFCOG', 'DIFFCOIL', 'DIFFMMF', 'DIFFMX', 'DIFFMX', 'DIFFMY', 'DIFFMY', 'DIFFMZ', 'DIFFMZ', 'DIFFUSE', 
'DIFFX', 'DIFFY', 'DIFFZ', 'DIMENS', 'DISGAS', 'DNGL', 'DOMAINS', 'DPCDT', 'DPGRID', 'DPNUM', 'DRAINAGE', 'DREF', 'DREFS', 'DREFT', 'DREFW', 'DREFWS', 'DRILPRI', 'DRSDT', 'DRVDT', 'DUALPERM', 
'DUALPORO', 'DUMPFLUX', 'DX', 'DXV', 'DYV', 'DZMATRIX', 'DZMTRX', 'DZMTRXV', 'DZNET', 'DZV', 'ECHO', 'ECLMC', 'EDIT', 'EDITNNC', 'EDITNNCR', 'EHYSTR', 'EHYSTRR', 'END', 'ENDACTIO', 'ENDBOX', 
'ENDFIN', 'ENDNUM', 'ENDSCALE', 'ENDSKIP', 'ENKRVC', 'ENKRVD', 'ENKRVT', 'ENPCVC', 'ENPCVD', 'ENPCVT', 'ENPTVC', 'ENPTVD', 'ENPTVT', 'EOS', 'EOSNUM', 'EOSS', 'EPSCOMP', 'EQLDIMS', 'EQLDKVCR', 'EQLDREAC', 
'EQLDTAB', 'EQLNUM', 'EQLOPTS', 'EQUALREG', 'EQUALS', 'EQUIL', 'ESSNODE', 'EXCEL', 'EXTRAPMS', 'FACTLI', 'FAULTDIM', 'FAULTS', 'FBHPDEF', 'FIELD', 'FIELDSEP', 'FIP', 'FIPNUM', 'FIPOWG', 'FIPSEP', 'FLUXNUM', 
'FLUXREG', 'FMTIN', 'FOAM', 'FOAMADS', 'FOAMDCYO', 'FOAMDCYW', 'FOAMFCN', 'FOAMFRM', 'FOAMFSC', 'FOAMFSO', 'FOAMFST', 'FOAMFSW', 'FOAMMOB', 'FOAMMOBP', 'FOAMMOBS', 'FOAMOPTS', 'FOAMROCK', 'FORMOPTS', 'FULLIMP', 'GADVANCE', 
'GAS', 'GASBEGIN', 'GASCCMP', 'GASCONC', 'GASEND', 'GASFCOMP', 'GASFDECR', 'GASFDELC', 'GASFIELD', 'GASFTARG', 'GASMONTH', 'GASPERIO', 'GASSATC', 'GASVISCF', 'GASVISCT', 'GASYEAR', 'GCONINJE', 'GCONPRI', 'GCONPROD', 'GCONSALE', 
'GCONSUMP', 'GCONTOL', 'GCUTBACK', 'GDCQ', 'GDCQECON', 'GDFILE', 'GDRILPOT', 'GECON', 'GEFAC', 'GEODIMS', 'GEOMECH', 'GINJGAS', 'GLIFTLIM', 'GLIFTOPT', 'GMDISBC', 'GMPSTBC', 'GNETDP', 'GNETINJE', 'GNETPUMP', 'GPMAINT', 
'GPMAINT', 'GPTABLE', 'GPTABLE', 'GPTABLEN', 'GPTDIMS', 'GRAVDR', 'GRAVDRM', 'GRAVITY', 'GRID', 'GRIDFILE', 'GRIDOPTS', 'GRIDUNIT', 'GRUPFUEL', 'GRUPINJE', 'GRUPLIM', 'GRUPMAST', 'GRUPNET', 'GRUPPROD', 'GRUPRIG', 'GRUPSALE', 
'GRUPSLAV', 'GRUPTARG', 'GRUPTREE', 'GSATCOMP', 'GSATINJE', 'GSATPROD', 'GSEPCOND', 'GSWINGF', 'GTADD', 'GTMULT', 'GUIDERAT', 'SSOL', 'HEATCR', 'HEATCRT', 'HEATDIMS', 'HEATER', 'HEATERL', 'HEATTX', 'HEATTY', 'HEATTZ', 
'HEATVAP', 'HEATVAPE', 'HEATVAPS', 'HMMLCTAQ', 'HMMLFTAQ', 'HMMLTPX', 'HMMLTPXY', 'HMMROCKT', 'HMMULTX', 'HMMLTXY', 'HMMULTX', 'HMMULTZ', 'HMRREF', 'HWELLS', 'HWKRO', 'HWKRORG', 'HWKRORW', 'HWKRW', 'HWKRWR', 'HWPCW', 
'HWSOGCR', 'HWSOWCR', 'HWSWCR', 'HWSWL', 'HWSWLPC', 'HWSWU', 'HXFIN', 'IKRG', 'IKRGR', 'IKRGRX', 'IKRGRX', 'IKRGRY', 'IKRGRY', 'IKRGRZ', 'IKRGRZ', 'IKRGX', 'IKRGX', 'IKRGY', 'IKRGY', 'IKRGZ', 
'IKRGZ', 'IKRO', 'IKRORG', 'IKRORGX', 'IKRORGX', 'IKRORGY', 'IKRORGY', 'IKRORGZ', 'IKRORGZ', 'IKRORW', 'IKRORWX', 'IKRORWX', 'IKRORWY', 'IKRORWY', 'IKRORWZ', 'IKRORWZ', 'IKROX', 'IKROX', 'IKROY', 'IKROY', 
'IKROZ', 'IKROZ', 'IKRW', 'IKRWR', 'IKRWRX', 'IKRWRX', 'IKRWRY', 'IKRWRY', 'IKRWRZ', 'IKRWRZ', 'IKRWX', 'IKRWX', 'IKRWY', 'IKRWY', 'IKRWZ', 'IKRWZ', 'IMBNUM', 'IMBNUMMF', 'IMPES', 'IMPLICIT', 
'IMPORT', 'INCLUDE', 'INIT', 'IONROCK', 'IONXROCK', 'IONXSURF', 'IPCG', 'IPCW', 'ISGAS', 'ISGCR', 'ISGCRX', 'ISGCRX', 'ISGCRY', 'ISGCRY', 'ISGCRZ', 'ISGCRZ', 'ISGL', 'ISGLPC', 'ISGLX', 'ISGLX', 
'ISGLY', 'ISGLY', 'ISGLZ', 'ISGLZ', 'ISGU', 'ISGUX', 'ISGUX', 'ISGUY', 'ISGUY', 'ISGUZ', 'ISGUZ', 'ISOGCR', 'ISOGCRX', 'ISOGCRX', 'ISOGCRY', 'ISOGCRY', 'ISOGCRZ', 'ISOGCRZ', 'ISOLNUM', 'ISOWCR', 
'ISOWCRX', 'ISOWCRX', 'ISOWCRY', 'ISOWCRY', 'ISOWCRZ', 'ISOWCRZ', 'ISWCR', 'ISWCRX', 'ISWCRX', 'ISWCRY', 'ISWCRY', 'ISWCRZ', 'ISWCRZ', 'ISWL', 'ISWLPC', 'ISWLX', 'ISWLX', 'ISWLY', 'ISWLY', 'ISWLZ', 
'ISWLZ', 'ISWU', 'ISWUX', 'ISWUX', 'ISWUY', 'ISWUY', 'ISWUZ', 'ISWUZ', 'JALS', 'JFUNC', 'JFUNCR', 'KRG', 'KRGR', 'KRGRX', 'KRGRX', 'KRGRY', 'KRGRY', 'KRGRZ', 'KRGRZ', 'KRGX', 
'KRGX', 'KRGY', 'KRGY', 'KRGZ', 'KRGZ', 'KRNUM', 'KRNUMMF', 'KRO', 'KRORG', 'KRORGX', 'KRORGX', 'KRORGY', 'KRORGY', 'KRORGZ', 'KRORGZ', 'KRORW', 'KRORWX', 'KRORWX', 'KRORWY', 'KRORWY', 
'KRORWZ', 'KRORWZ', 'KROX', 'KROX', 'KROY', 'KROY', 'KROZ', 'KROZ', 'KRW', 'KRWR', 'KRWRX', 'KRWRX', 'KRWRY', 'KRWRY', 'KRWRZ', 'KRWRZ', 'KRWX', 'KRWX', 'KRWY', 'KRWY', 
'KRWZ', 'KRWZ', 'KVALUES', 'KVCR', 'KVCRS', 'KVCRWAT', 'KVTABLE', 'KVTABT', 'KVTEMP', 'KVWI', 'LAB', 'LANGMEXT', 'LANGMPL', 'LANGMUIR', 'LANGMULT', 'LBCCOEF', 'LBCCOEFR', 'LGR', 'LGRCOPY', 'LGRLOCK', 
'LGROFF', 'LGRON', 'LICENSES', 'LIFTOPT', 'LILIM', 'LKRO', 'LKRORG', 'LKRORW', 'LKRW', 'LKRWR', 'LOWSALT', 'LPCW', 'LSALTFNC', 'LSLTWNUM', 'LSOGCR', 'LSOWCR', 'LSWCR', 'LSWL', 'LSWLPC', 'LSWU', 
'LTOSIGMA', 'LUMPDIMS', 'LUMPING', 'LWKRO', 'LWKRORG', 'LWKRORW', 'LWKRW', 'LWKRWR', 'LWPCW', 'LWSLTNUM', 'LWSOGCR', 'LWSOWCR', 'LWSWCR', 'LWSWL', 'LWSWLPC', 'LWSWU', 'LX', 'MAPAXES', 'MAPUNITS', 'MATCORR', 
'MAXTRANZ', 'MAXVALUE', 'MEMORY', 'MESSAGE', 'METRIC', 'MIDS', 'MINDZNET', 'MINPORV', 'MINPV', 'MINPVV', 'MINROCKV', 'MINRV', 'MINVALUE', 'MISC', 'MISCEXP', 'MISCIBLE', 'MISCNUM', 'MISCSTR', 'MISCSTRP', 'MISCSTRR', 
'MLANG', 'MONITOR', 'MSFN', 'MULTFLT', 'MULTIN', 'MULTIPLY', 'MULTIREG', 'MULTMF', 'MULTNUM', 'MULTOUT', 'MULTOUTS', 'MULTPV', 'MULTREGP', 'MULTREGT', 'MULTSIG', 'MULTSIGV', 'MULTX', 'MULTX', 'MULTY', 'MULTY', 
'MULTZ', 'MULTZ', 'MW', 'MWS', 'MWW', 'MWWS', 'NCOMPS', 'NCONSUMP', 'NEI', 'NETBALAN', 'NETCOMPA', 'NETWORK', 'NEWTRAN', 'NEXTSTEP', 'NGASREM', 'NNC', 'NNCGEN', 'NODEPROP', 'NODPCDT', 'NODPPM', 
'NOMIX', 'NONNC', 'NOSIM', 'NPROCX', 'NSTACK', 'NTG', 'NUMRES', 'NUPCOL', 'NWATREM', 'NXFIN', 'OFM', 'OIL', 'OILAPI', 'OILVINDX', 'OILVISCC', 'OILVISCT', 'OLDTRAN', 'OMEGAA', 'OMEGAAS', 'OPERATE', 
'OPERATER', 'OPERNUM', 'OPTIONS', 'OPTIONS', 'OUTSOL', 'OVERBURD', 'PARACHOR', 'PARALLEL', 'PATHS', 'PBUB', 'PBVD', 'PCG', 'PCRIT', 'PCRITS', 'PCW', 'PDEW', 'PDVD', 'PEDERSEN', 'PEDTUNE', 'PEDTUNER', 
'PERMAVE', 'PERMMF', 'PERMSTAB', 'PERMX', 'PETGRID', 'PETOPTS', 'PICOND', 'PIMTDIMS', 'PIMULTAB', 'PINCH', 'PINCHNUM', 'PINCHOUT', 'PINCHREG', 'PINCHXY', 'PLMIXNUM', 'PLMIXPAR', 'PLYADS', 'PLYADSS', 'PLYATEMP', 'PLYCAMAX', 
'PLYDHFLF', 'PLYESAL', 'PLYKRRF', 'PLYMAX', 'PLYROCK', 'PLYSHEAR', 'PLYSHLOG', 'PLYTRRF', 'PLYVISC', 'PLYVISCS', 'PLYVISCT', 'PLYVSCST', 'PMANUM', 'PMISC', 'POISSONR', 'POLYMER', 'PORO', 'PORV', 'PPCWMAX', 'PRCORR', 
'PREF', 'PREFS', 'PREFT', 'PREFW', 'PREFWS', 'PRESSURE', 'PRIORITY', 'PROPS', 'PRORDER', 'PRVD', 'PSEUPRES', 'PSPLITX', 'PVCDO', 'PVCO', 'PVDG', 'PVDO', 'PVDS', 'PVTG', 'PVTNUM', 'PVTO', 
'PVTW', 'PVTWSALT', 'PVZG', 'QDRILL', 'RADIAL', 'REACACT', 'REACCORD', 'REACENTH', 'REACLIMS', 'REACPHA', 'REACPORD', 'REACRATE', 'REACSORD', 'REACTION', 'RECOVERY', 'REFINE', 'REGDIMS', 'REGIONS', 'RESORB', 'RESTART', 
'RESVNUM', 'RKTRMDIR', 'ROCK', 'ROCKCOMP', 'ROCKCON', 'ROCKDEN', 'ROCKDIMS', 'ROCKFRAC', 'ROCKNUM', 'ROCKOPTS', 'ROCKPAMA', 'ROCKPROP', 'ROCKTAB', 'ROCKTABH', 'ROCKTRMX', 'ROCKTRMY', 'ROCKTRMZ', 'ROCKTSIG', 'ROCKV', 'ROMF', 
'RPTGRID', 'RPTHMD',  'RPTSCHED', 'RPTISOL', 'RPTRUNSP', 'RPTSMRY', 'RPTONLY', 'RPTONLYO', 'RPTRST', 'RS', 'RSCONST', 'RSCONSTT', 'RSVD', 'RSW', 'RSWVD', 'RTEMP', 'RTEMPA', 'RTEMPVD', 'RUNSPEC', 'RV', 'RVCONST', 
'RVCONSTT', 'RVVD', 'SALINITY', 'SALT', 'SALTNODE', 'SALTVD', 'SATNUM', 'SATOPTS', 'SCALECRS', 'SCALELIM', 'SCDATAB', 'SCDPDIMS', 'SCDPTAB', 'SCDPTRAC', 'SCHEDULE', 'SCREF', 'SDENSITY', 'SDREF', 'SEPARATE', 'SEPCOND', 
'SEPVALS', 'SFOAM', 'SGAS', 'SGCR', 'SGCRX', 'SGCRX', 'SGCRY', 'SGCRY', 'SGCRZ', 'SGCRZ', 'SGCWMIS', 'SGFN', 'SGL', 'SGLPC', 'SGLX', 'SGLX', 'SGLY', 'SGLY', 'SGLZ', 'SGLZ', 
'SGOF', 'SGU', 'SGUX', 'SGUX', 'SGUY', 'SGUY', 'SGUZ', 'SGUZ', 'SGWFN', 'SHRATE', 'SIGMA', 'SIGMAGD', 'SIGMAGDV', 'SIGMATH', 'SIGMAV', 'SKIP', 'SKIP', 'SKIP', 'SKIPREST', 'SKIPSTAB', 
'SKRO', 'SKRORW', 'SKRW', 'SKRWR', 'SLAVES', 'SLGOF', 'SMF', 'SOCRS', 'SOF', 'SOF', 'SOGCR', 'SOGCRX', 'SOGCRX', 'SOGCRY', 'SOGCRY', 'SOGCRZ', 'SOGCRZ', 'SOIL', 'SOILR', 'SOLID', 
'SOLIDADS', 'SOLIDMMC', 'SOLIDMMS', 'SOLUBILI', 'SOLUBILS', 'SOLUTION', 'SOLVDIRS', 'SOLVENT', 'SOMGAS', 'SOMWAT', 'SOR', 'SOROPTS', 'SORWMIS', 'SOWCR', 'SOWCRX', 'SOWCRX', 'SOWCRY', 'SOWCRY', 'SOWCRZ', 'SOWCRZ', 
'SPECGRID', 'SPECHA', 'SPECHB', 'SPECHEAT', 'SPECHG', 'SPECHH', 'SPECHS', 'SPECHT', 'SPECROCK', 'SPOLY', 'SPREF', 'SSFN', 'SSHIFT', 'SSHIFTS', 'SSOL', 'SSOLID', 'SSOWCR', 'SSWCR', 'SSWL', 'SSWU', 
'START', 'STCOND', 'STHERMX', 'STOG', 'STONE', 'STONE', 'STONE', 'STONEPAR', 'STOPROD', 'STOREAC', 'STOW', 'STREF', 'STVP', 'SUMMARY', 'SURF', 'SURFACT', 'SURFACTW', 'SURFADDW', 'SURFADS', 'SURFCAPD', 
'SURFESAL', 'SURFNUM', 'SURFROCK', 'SURFST', 'SURFSTES', 'SURFVISC', 'SURFWNUM', 'SWAT', 'SWATINIT', 'SWCR', 'SWCRX', 'SWCRX', 'SWCRY', 'SWCRY', 'SWCRZ', 'SWCRZ', 'SWFN', 'SWINGFAC', 'SWL', 'SWLPC', 
'SWLX', 'SWLX', 'SWLY', 'SWLY', 'SWLZ', 'SWLZ', 'SWOF', 'SWU', 'SWUX', 'SWUX', 'SWUY', 'SWUY', 'SWUZ', 'SWUZ', 'TABDIMS', 'TBLK', 'TCBDIMS', 'TCRIT', 'TCRITS', 'TEMP', 
'TEMPI', 'TEMPNODE', 'TEMPVD', 'THANALB', 'THCGAS', 'THCOIL', 'THCONMF', 'THCONR', 'THCONSF', 'THCROCK', 'THCSOLID', 'THCWATER', 'THERMAL', 'THERMEX', 'THPRES', 'THPRESFT', 'THSVC', 'THWVC', 'TIGHTENP', 'TITLE', 
'TLMIXPAR', 'TNUM', 'TOLCRIT', 'TOPS', 'TRACER', 'TRACERS', 'TRACK', 'TRACKREG', 'TRADS', 'TRANGE', 'TRANX', 'TRANY', 'TRANZ', 'TRCOEF', 'TRDCY', 'TRDIF', 'TREF', 'TREFS', 'TREFT', 'TRROCK', 
'TSTEP', 'TUNING', 'TUNINGS', 'TVDP', 'TZONE', 'UDADIMS', 'UDQ', 'UDQDIMS', 'UDQPARAM', 'UDT', 'UDTDIMS', 'UNIFIN', 'UNIFOUT', 'UNIFOUTS', 'USEFLUX', 'VAPOIL', 'VAPPARS', 'VCOMPACT', 'VCRIT', 'VCRITS', 
'VCRITVIS', 'VDFLOW', 'VDFLOWR', 'VDKRG', 'VDKRGC', 'VDKRO', 'VELDEP', 'VFPCHECK', 'VFPCHK', 'VFPIDIMS', 'VFPINJ', 'VFPPDIMS', 'VFPPROD', 'VFPTABL', 'VISCD', 'VISCREF', 'VREFW', 'WAGHALT', 'WAGHYSTR', 'WALKALIN', 
'WARN', 'WATDENT', 'WATER', 'WATERTAB', 'WATVISCT', 'WAVAILIM', 'WBHGLR', 'WCONHIST', 'WCONINJ', 'WCONINJE', 'WCONINJH', 'WCONINJP', 'WCONPROD', 'WCUTBACK', 'WCYCLE', 'WDFAC', 'WDFACCOR', 'WDRILPRI', 'WDRILRES', 'WDRILTIM', 
'WECON', 'WECONCMF', 'WECONINJ', 'WEFAC', 'WELCNTL', 'WELDRAW', 'WELLCOMP', 'WELLDIMS', 'WELLGR', 'WELLINJE', 'WELLLIM', 'WELLOPEN', 'WELLOPTS', 'WELLPROD', 'WELLSHUT', 'WELLSPEC', 'WELLSTRE', 'WELLSTRW', 'WELLTARG', 'WELLTCB', 
'WELLTCBT', 'WELLWAG', 'WELOPEN', 'WELOPENL', 'WELPI', 'WELPRI', 'WELSEGS', 'WELSOMIN', 'WELSPECL', 'WELSPECS', 'WELTARG', 'WFOAM', 'WFRICSEG', 'WFRICTN', 'WFRICTNL', 'WGASPROD', 'WGORPEN', 'WGRUPCON', 'WH', 'WH', 
'WHISTCTL', 'WHTEMP', 'WI', 'WINJGAS', 'WINJMIX', 'WINJMULT', 'WINJOIL', 'WINJORD', 'WINJTEMP', 'WINJW', 'WINJWAT', 'WLIFT', 'WLIFTOPT', 'WLIMTOL', 'WLIST', 'WLISTDYN', 'WMF', 'WMFVD', 'WNAMES', 'WNETDP', 
'WORKLIM', 'WORKTHP', 'WPAVE', 'WPAVEDEP', 'WPIMULT', 'WPIMULTL', 'WPITAB', 'WPOLYMER', 'WREGROUP', 'WRFT', 'WRFTPLT', 'WSALT', 'WSCCLEAN', 'WSCCLENL', 'WSCTAB', 'WSEGAICD', 'WSEGDFPA', 'WSEGDIMS', 'WSEGEXSS', 'WSEGFLIM', 
'WSEGFMOD', 'WSEGINIT', 'WSEGITER', 'WSEGLINK', 'WSEGPULL', 'WSEGSEP', 'WSEGSICD', 'WSEGTABL', 'WSEGVALV', 'WSEPCOND', 'WSOLVENT', 'WSURFACT', 'WTADD', 'WTAKEGAS', 'WTEMP', 'WTEST', 'WTMULT', 'WTRACER', 'WVFPDP', 'WVFPEXP', 
'WWPAVE', 'XMF', 'XMFVP', 'YMF', 'YMFVP', 'YOUNGMOD', 'ZCORN', 'ZCRIT', 'ZCRITS', 'ZCRITVIS', 'ZFACT', 'ZFACTOR', 'ZI', 'ZIPPY', 'ZMF', 'ZMFVD', 'IM', 'IM', 'AC', 'ADGCSTC', 
'ADGMAXC', 'ADMAXT', 'ADRT', 'ADSCOMP', 'ADSCOMP', 'ADSLANG', 'ADSPHBLK', 'ADSROCK', 'ADSTABLE', 'ADSTYPE', 'ALPHAKRG', 'ALTER', 'ALTER', 'ALTERCP', 'API', 'APIGRAD', 'APIT', 'APPOR', 'AQFUNC', 'AQLEAK', 
'AQMETHOD', 'AQPROP', 'AQUEOUS', 'AQUIFER', 'AQVISC', 'ARESOILK', 'AVG', 'AVISC', 'BG', 'BHPDEPTH', 'BIN', 'BKRGCW', 'BKROCW', 'BKRWIRO', 'BLOCKGRO', 'BOT', 'BOTAPI', 'BPCGMAX', 'BPCWMAX', 'BSGCON', 
'BSGR', 'BSOIRG', 'BSOIRW', 'BSORG', 'BSORW', 'BSWCRIT', 'BSWR', 'BVG', 'BVISC', 'BWI', 'CCPOR', 'CMM', 'CO', 'COAL', 'COAL', 'COMPNAME', 'CON', 'CONC', 'COORD', 'CORNERS', 
'COT', 'CP', 'CPG', 'CPL', 'CPOR', 'CPORPD', 'CPRPOR', 'CPT', 'CPTPOR', 'CRIT', 'CROCKTAB', 'CROCKTAB', 'CROCKTYP', 'CT', 'CT', 'CTPOR', 'CTYPE', 'CVO', 'CYCPRT', 'DAMP', 
'DATE', 'DATUMDEP', 'DENSITY', 'DENSTR', 'DEPLETIO', 'DEPTH', 'DGOC', 'DI', 'DIFFUSIO', 'DIFLIB', 'DIFRAC', 'DILATION', 'DRILLQ', 'DTOP', 'DTRAPN', 'DTRAPW', 'DUALPERM', 'DUALPOR', 'DWOC', 'EACT', 
'EACT', 'EGUST', 'EOSSET', 'EOSTYPE', 'EPSPC', 'EPSPCG', 'EQUALSI', 'EV', 'FILENAME', 'FORMINFR', 'FRACTURE', 'FREQFAC', 'FREQFACP', 'FRFRAC', 'FRWIDTHC', 'FZ', 'GASD', 'GASLIQKV', 'GASZONE', 'GCONCYCL', 
'GCONCYCL', 'GCONCYCL', 'GCONCYCR', 'GCONCYCR', 'GCONI', 'GCONIMUL', 'GCONM', 'GCONP', 'GCRV', 'GEOMETRY', 'GLCONTRO', 'GLIFT', 'GLOPT', 'GPRODGRO', 'GRAVITY', 'GRID', 'GROUP', 'HCFLAG', 'HEAD', 'HEATR', 
'HLOSSPRO', 'HLOSST', 'HLOSSTDI', 'HTWELL', 'HTWTEMP', 'HVAPR', 'HVR', 'HYS', 'HYS', 'HYS', 'HYS', 'HYS', 'HYS', 'HYSKRG', 'HYSKRO', 'HYSKROG', 'HYSKROW', 'HYSKRW', 'IDEALGAS', 'IFTTABLE', 
'IJK', 'INCLUDE', 'INCOMP', 'INITIAL', 'INITREGI', 'INJECTOR', 'INTCOMP', 'INTCOMP', 'INTYPE', 'INUNIT', 'ISECTOR', 'ISOTHERM', 'ITUBE', 'IVAR', 'IWELLBOR', 'JFUNC', 'SURF', 'KRGCW', 'KRINTRP', 'KROCW', 
'KROGCG', 'KROIL', 'KRPERF', 'KRTEMTAB', 'KRTYPE', 'KRWIRO', 'KV', 'KVTABLE', 'KVTABLIM', 'LAYER', 'LAYERGRA', 'LAYERXYZ', 'MANIFOLD', 'MASSDEN', 'MATRIX', 'MAXTEMP', 'MFRAC', 'MFRAC', 'MFRAC', 'MINSS', 
'MINTEMP', 'MIXVC', 'MODEL', 'MODELSHU', 'MOLDEN', 'MOLVOL', 'MONITOR', 'NC', 'NETGROSS', 'NETPAY', 'NULL', 'NUMERICA', 'PP', 'OCRV', 'OMEGA', 'OMEGA', 'OMEGASG', 'ON', 'OPERATE', 'OPERATE', 
'PADSORP', 'PB', 'PBC', 'PCGEND', 'PCHOR', 'PCON', 'PCRIT', 'PCWEND', 'PERF', 'PERFV', 'PERMCK', 'PERMEXP', 'PERMI', 'PERMSHAL', 'PERMTAB', 'PERMTABL', 'PHWELLBO', 'PINCHOUT', 'PINJW', 'PLANT', 
'PLNRFRAC', 'PLNRFRAC', 'PMIX', 'POLYADS', 'POLYCONC', 'POR', 'PORFORM', 'PORMAX', 'PPERM', 'PREFCONC', 'PRES', 'PRODUCER', 'PRPOR', 'PRSR', 'PSURF', 'PTHRESHI', 'PTUBE', 'PTYPE', 'PVC', 'PVCUTFR', 
'PVCUTOFF', 'PVISC', 'PVT', 'PVTAPI', 'PVTCOND', 'PVTS', 'PWELLBOR', 'QUAL', 'REFDEPTH', 'REFINE', 'REFPRES', 'RELAX', 'RENTH', 'RESDATE', 'RESTART', 'RHOW', 'ROCKCP', 'ROCKCP', 'ROCKFLUI', 'ROCKTYPE', 
'RORDER', 'RPHASE', 'RPT', 'RPT', 'RRFT', 'RRFTG', 'RRFTO', 'RRFTW', 'RTEMLOWR', 'RTEMUPR', 'RTYPE', 'RUN', 'RXCRITCO', 'RXEQBAK', 'RXEQBASE', 'RXEQFOR', 'SALINITY', 'SAT', 'SCONNECT', 'SECTORAR', 
'SEPARATO', 'SETPI', 'SG', 'SGCON', 'SGR', 'SGT', 'SHAPE', 'SHEAR', 'SHEAREFF', 'SHEARTAB', 'SHEARTHC', 'SHEARTHI', 'SHEARTHI', 'SHUTIN', 'SKIN', 'SLT', 'SO', 'SOIRG', 'SOIRW', 'SOLID', 
'SOLID', 'SOLVER', 'SONEQ', 'SORG', 'SORM', 'SORMAX', 'SORW', 'SRFTNG', 'SRFTNW', 'STOP', 'STOPROD', 'STOREAC', 'SURFLASH', 'SW', 'SW', 'SWCRIT', 'SWINIT', 'SWINIT', 'SWNEQ', 'SWR', 
'SWT', 'SWT', 'SWTI', 'TARGET', 'TCRIT', 'TEMP', 'TEMR', 'TFORM', 'THCONANT', 'THCONG', 'THCONMIX', 'THCONO', 'THCONR', 'THCONR', 'THCONS', 'THCONTAB', 'THCONW', 'THTYPE', 'TIME', 'TINJW', 
'TITLE', 'TMPSET', 'TRACER', 'TRANLI', 'TRANSF', 'TRANSI', 'TRANSMUL', 'TRCR', 'TRCR', 'TREFVS', 'TRIGGER', 'TSURF', 'UHTR', 'USER', 'VAMOD', 'VATYPE', 'VERTICAL', 'VGUST', 'VISCOEFF', 'VISCOR', 
'VISCTABL', 'VISCTYPE', 'VISVC', 'VOLMOD', 'VOT', 'VOTAPI', 'VSHIF', 'VSHIFT', 'VSMIXCOM', 'VSMIXEND', 'VSMIXFUN', 'VSTYPE', 'WCRV', 'WELGEO', 'WELL', 'WELSEP', 'WLISTSHU', 'WOC', 'WTINCR', 'WTMULT', 
'XFLOW', 'XNACL', 'ZCORN', 'ZOIL'}

keywords_tNav = {'FRACTURE_STAGE', 'REPORTSCREEN', 'SKIPTNAV', 'COREYWO', 'INTERPOLATE', 'OPEN_BASE_MODEL', 'VISCOPTS', 'WINJV', 'ASPPW2DR', 'RPTGRAPHT', 'VFPCORR', 'PROPANTTABLE', 'WWAG', 'JRC', 
'PLYELVSCS', 'FRACTURE_POINTSET_STAGE', 'FRACTURE_FLOW', 'HYSTOPTS', 'FLOWFNAMES', 'IMPORT_PROJECT', 'ENPKTRC', 'STREAMLINE_PARAMS', 'STORE', 'ROCKFAIL', 'GECONX', 'HYSTKRWR', 'ENPCTRCM', 'FLASHCTRL', 
'FRACTURE_WELL', 'WELLTRACK', 'SALTPROP', 'ARITHMETIC_ARRAYS', 'PVTOPTS', 'RPTGRAPHL', 'LANGUAGE', 'HYSTPCG', 'WFRACL', 'VISCNUM', 'NOILREM', 'HYSTPCGR', 'PLYELVSC', 'KROM', 'ECDATES', 'TEMPR', 'WBHZONE', 
'OILTRAP', 'WTEMPDEF', 'RESTARTDATE', 'CYLINDER', 'KRSMOOTH', 'ASPVISOR', 'PLYELVSV', 'ENPCTRC', 'PCRITWS', 'WSKFUNC', 'ASPREWGR', 'BLOCK', 'RPTRSTD', 'RPTRSTT', 'LINEAR_ISOPERM', 'INNERWIDTH', 'ARITHMETIC', 
'HYSTKROWR', 'GLRTAB', 'MINPVR', 'PCWM', 'FLOWFUNC', 'THERMEX3', 'COMSOL', 'DRSDTVPE', 'WATHMODEL', 'ROCKAXES', 'TRMTEMP', 'WELLSTRV', 'ZONES', 'DEACDEPT', 'RPTMAPT', 'HYSTPCW', 'WGASLIFT', 'SPECHI', 'NPROPANTS', 
'RPTGRAPHD', 'TCRITW', 'PROPANTNAMES', 'HYSTPCWR', 'SRSALT', 'NETNODE', 'TCRITWS', 'ASPDEPOR', 'HYSTKROGR', 'JFPERM', 'AUTOSAVE', 'FAULTNNC', 'KRGM', 'AIMCTRL', 'FLOWFTAB', 'RPTRSTL', 'DEFINES', 'RFD_WFRAC', 
'VISCPT', 'WLOGDATA', 'LETGO', 'APPLYSCRIPT', 'FRACTURE_TEMPLATE', 'SWUPC', 'SYSTEM', 'NETCHOKE', 'REPORTFILE', 'SOLUHENRY', 'CARFINBG', 'NEFLASH', 'SGUPC', 
'COREYGOMOD', 'VDEF', 'WATVINDX', 'FRACTURE_SPECS', 'SEPDEN', 'WELLBRANCH', 'COMPVALL', 'RPTMAPS', 'STEVISCF', 'HYSTKRG', 'SPECHD', 'WORK', 'WSEGCNTL', 'SURFDW', 'DENSTRMIX', 'COMPFRAC', 'PLYVISCA', 'ECVAL', 
'COMPVAL', 'SKIPON', 'ROCKSTRE', 'HYSTKRGR', 'STHERMX2', 'WLOGCALC', 'LETWO', 'HYSTKRW', 'HYSTOPTSR', 'COREYGO', 'GASTRAP', 'VISGRID', 'ECINIT', 'WFRAC', 'SPECHJ', 'OVPG', 'TNAVCTRL', 
'PLYSHEARA', 'FAULTSL', 'ROCKSALT', 'CREFT1W', 'HYSTKROG', 'TREFW', 'FRACTURE_POINTSET', 'WELLSTRZ', 'ISWUPC', 'WECONX', 'WSEGICDPARAM', 'ACTIONC', 'WELLDATA', 'WFRP', 'CREFT2W', 'ROCKT', 'ARR', 'SALTTRM', 
'COMPFRACL', 'ISGUPC', 'COMPDATMD', 'ENPTRCM', 'RPTMAPL', 'SKIPOFF', 'WCUTBACX', 'PCGM', 'PLYELVMAXA', 'WELLINCL', 'WFRACPL', 'WINJZ', 'AQUGP', 'ROCKCONT', 'FRACTURE_PLANE', 'ENPKTRCM', 
'COREYWOMOD', 'PVTGEN', 'THETA', 'ENPTRC', 'FRACTURE_ARITHMETIC', 'TRMMULTC', 'FIPPATT', 'CREFPTW', 'COREYWG', 'WATVISCF', 'PHASEID', 'TRACERM', 'PLYELVSVA', 'RPTMAPD', 'VSHIF1', 'AQUOPTS', 'PREDEFINES', 
'FRACTURE_PIMULT', 'HYSTKROW', 'ASPFLRTR', 'GWRATMUL', 'LETWG', 'REACCONC', 'RUNCTRL', 'WPIFUNC', 'WFRACP', 'NFLOWFTB', 'TRMMULTT', 'DRSDTVP', 'HEATTCR', 'JCS', 'FRACTURE_PATH', 'SPECHC', 
'PCRITW', 'STANDG', 'COHESION', 'FRACTURE_POINTSET_VAL', 'IWORK', 'WDFACCORL', 'KRWM', 'WECONINJX', 'STANDO', 'THERMEX2', 'TRACEROPTS', 'OILVINDT'}

keywords_without_slash_symbol = {'TUNING', 'SKIPTEST', 'SCHEDULE', 'INCLUDE', 'COMPOFF', 'VFPPROD', 'WELLTRACK'}

keywords = {*keywords, *keywords_tNav}
