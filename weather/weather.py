import xmltodict
import json

filename = input()
file = open(filename)

jsonString = json.dumps(xmltodict.parse(file.read()), indent=2)

filename = filename.replace(".xml", "")

file = open(filename+'.json', "w")
file.write(jsonString)
