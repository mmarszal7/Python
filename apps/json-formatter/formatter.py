import os
import json

# { "glossary": { "title": "example glossary", "GlossEntry": { "Acronym": "SGML", "Abbrev": "ISO 8879:1986", "GlossDef": { "GlossSeeAlso": ["GML", "XML"] }, "GlossSee": "markup" } } }

def toClipboard(text):
    command = 'echo {} | clip'.format(text.strip())
    os.system(command)

def formatter(jsonString, indent):
	parsed = json.loads(jsonString)
	return json.dumps(parsed, indent=indent)

def getJSONfromFile():
	print("Enter file name:")
	filename = input()
	f = open(filename, "r", encoding="utf8")
	jsonString = f.read()
	f.close()
	return jsonString
	
def getJSONfromConsole():
	print('Paste json:')
	return input()
	
def saveJSONtoFile(jsonString):
	f = open("temp.json", "w", encoding="utf8")
	f.write(jsonString)
	f.close()

print('Number of spaces for indent:')
indent = input()
print("Press 1 if you want to convert words from a file:")
jsonString = getJSONfromFile() if input() == "1" else getJSONfromConsole()

formattedJSON = formatter(jsonString, indent)
toClipboard(formattedJSON)
saveJSONtoFile(formattedJSON)
print('\n' + formattedJSON + '\nJSON copied to clipboard and save in temp.json file!')
