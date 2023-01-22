import json
datas = open("classData/subjects.json", "r").read()
data = json.loads(datas)
subjects = data["value"]
names = []
for subject in subjects:
    names.append(subject["Abbreviation"])
print(names)