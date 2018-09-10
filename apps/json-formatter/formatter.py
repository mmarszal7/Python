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

print('Paste indent:')
indent = input()
print('Paste json:')
json = input()

formattedJSON = formatter(json, indent)
toClipboard(formattedJSON)
print('\n' + formattedJSON)
