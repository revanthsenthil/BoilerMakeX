import requests
import json
classTypes = ['AAE', 'AAS', 'ABE', 'AD', 'AFT', 'AGEC', 'AGR', 'AGRY', 'AMST', 'ANSC', 'ANTH', 'ARAB', 'ASAM', 'ASEC', 'ASL', 'ASM', 'ASTR', 'AT', 'BAND', 'BCHM', 'BCM', 'BIOL', 'BME', 'BMS', 'BTNY', 'BUS', 'CAND', 'CDFS', 'CDIS', 'CE', 'CEM', 'CFS', 'CGT', 'CHE', 'CHEM', 'CHM', 'CHNS', 'CIMT', 'CJUS', 'CLCS', 'CLPH', 'CM', 'CMPL', 'CNIT', 'COM', 'CPB', 'CS', 'CSR', 'DANC', 'EAPS', 'EAS', 'ECE', 'ECET', 'ECON', 'EDCI', 'EDPS', 'EDST', 'EDUC', 'EEE', 'ENE', 'ENG', 'ENGL', 'ENGR', 'ENGT', 'ENTM', 'ENTR', 'EPCS', 'EXPL', 'FINA', 'FLL', 'FN', 'FNR', 'FR', 'FS', 'FVS', 'GEOL', 'GEP', 'GER', 'GRAD', 'GREK', 'GS', 'GSLA', 'HDFS', 'HEBR', 'HER', 'HHS', 'HIST', 'HK', 'HONR', 'HORT', 'HPER', 'HSCI', 'HSOP', 'HTM', 'IDE', 'IDIS', 'IE', 'IET', 'ILS', 'IPPH', 'IT', 'ITAL', 'JOUR', 'JPNS', 'JWST', 'KOR', 'LA', 'LALS', 'LATN', 'LC', 'LCME', 'LING', 'LS', 'MA', 'MARS', 'MATH', 'MCMP', 'ME', 'MET', 'MFET', 'MGMT', 'MSE', 'MSL', 'MUS', 'NRES', 'NS', 'NUCL', 'NUPH', 'NUR', 'NUTR', 'OBHR', 'OLS', 'PES', 'PHIL', 'PHPR', 'PHRM', 'PHYS', 'POL', 'PSY', 'PTEC', 'PTGS', 'PUBH', 
'RECR', 'REG', 'REL', 'RUSS', 'SA', 'SCI', 'SCLA', 'SFS', 'SLHS', 'SOC', 'SPAN', 'STAT', 'SYS', 'TDM', 'TECH', 'THTR', 'TLI', 'VCS', 'VIP', 'VM', 'WGSS', 'WOST', 'YDAE']
for classType in classTypes:
    apiRequest = "https://api.purdue.io/odata/Courses?$expand=Classes($filter=Term/Code eq '202320';$expand=Sections($expand=Meetings))&$filter=Subject/Abbreviation eq '" + classType + "'"
    data = requests.get(apiRequest).json()
    f = open("classData/" + classType + ".json", "w")
    f.write(json.dumps(data))
    f.close()