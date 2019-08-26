import os

# { "glossary": { "title": "example glossary", "GlossEntry": { "Acronym": "SGML", "Abbrev": "ISO 8879:1986", "GlossDef": { "GlossSeeAlso": ["GML", "XML"] }, "GlossSee": "markup" } } }

def toClipboard(text):
    command = 'echo {} | clip'.format(text.strip())
    os.system(command)

def formatter(json, indent):
	newJson = ''
	level = 0
	inString = False
	
	for c in json:
		if(c == '\"'):
			inString = not inString
			
		if(inString):
			newJson += c
			continue
		
		if(c == ','):
			newJson += '{}\n{}'.format(c, level * indent)
		elif(c == ']' or c == '}'):
			level -= 1
			newJson += '\n{}{}'.format(level * indent, c)
		elif(c == '{' or c == '['):
			level += 1
			newJson += '{}\n{}'.format(c, level * indent)
		else:
			newJson += c
	
	return newJson

def getJSONfromFile():
	print("Enter file name:")
	filename = input()
	f = open(filename, "r", encoding="utf8")
	json = f.read()
	f.close()
	return json
	
def getJSONfromConsole():
	print('Paste json:')
	return input()
	
def saveJSONtoFile(json):
	f = open("temp.json", "w", encoding="utf8")
	f.write(json)
	f.close()

print('Paste indent:')
indent = input()
print("Press 1 if you want to convert words from a file:")
json = getJSONfromFile() if input() == "1" else getJSONfromConsole()

formattedJSON = formatter(json, indent)
toClipboard(formattedJSON)
saveJSONtoFile(formattedJSON)
print('\n' + formattedJSON + '\nJSON copied to clipboard and save in temp.json file!')
