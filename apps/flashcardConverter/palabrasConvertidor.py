def convertWords(words):
	result = ""
	for i in range(0, len(words), 2):
		result += (words[i] + "\t" + words[i+1] + "\n")
	return result

## Raw text conversion
def convertFromConsole():
	print("Enter/Paste your words (press Ctrl-D or Ctrl-Z on Windows when finished):")
	words = []
	while True:
		try:
			words.append(input()) 
		except EOFError:
			break
	print(convertWords(words))

# File based conversion
def convertFromFile():
	print("Enter file name:")
	filename = input()
	f = open(filename, "r+", encoding="utf8")
	
	words = f.read().split("\n")
	f.write("\n" + convertWords(words))
	f.close()

print("Press 1 if you want to convert words from a file:")
convertFromFile() if input() == "1" else convertFromConsole()
print("Conversion finished")