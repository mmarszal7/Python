import os
from os import listdir
from os.path import isfile, join

# Todo: 
# (line 52) - program should not calculate lines of not selected extensions (problem with list indexing)

class ExtensionInfo:
	def __init__(self, name):
		self.name = name
		self.picked = False
		self.numberOfLines = 0

def getExtensionList(folderPath):
	extensions = []
	for dirpath,dirnames,filenames in os.walk(folderPath):
		for file in filenames:
			file_extension = os.path.splitext(file)[-1]
			extensions.append(file_extension)
	
	return [ExtensionInfo(ext) for ext in list(set(extensions))]
	
def chooseExtensions(extensions):
	print('Pick from avaiable extensions:')
	print('E. End picking')
	print('A. All extensions')
	for index, ext in enumerate(extensions):
		print(str(index) + '. ' + ext.name)

	while(True):
		try:
			pickedValue = input()
			if(pickedValue == 'E' or pickedValue == 'e'): break
			elif(pickedValue == 'A' or pickedValue == 'a'): 
				for ext in extensions: 
					ext.picked = True
			else:
				pickedNumber = int(pickedValue)
				extensions[pickedNumber].picked = not extensions[pickedNumber].picked
			
			print('\nPicked: ')
			print([ext.name for ext in extensions if ext.picked == True])
		except ValueError:
			print('Picked value must be a number!')
		except IndexError:
			print('Pick number from 0 to ' + str(index) + '!')
			
	return extensions
	
def calculateLinesPerExtension(projectPath, pickedExtensions):
	extensions = [ext.name for ext in pickedExtensions]
	for dirpath,dirnames,filenames in os.walk(projectPath):
		for file in filenames:
			file_extension = os.path.splitext(file)[-1]
			try:
				if(file_extension in extensions):
					lines = sum(1 for line in open(os.path.join(dirpath, file)))
					pickedExtensions[extensions.index(file_extension)].numberOfLines += lines
			except UnicodeDecodeError:
				pass
				#print('Could not compute lines of file: ' + os.path.join(dirpath, file))
	
	printLinesPerExtension(pickedExtensions)
				
def printLinesPerExtension(pickedExtensions):
	sum = 0
	print('Number of lines:')
	for ext in pickedExtensions: 
		if ext.picked == True: 
			sum += ext.numberOfLines
			print(ext.name + ':\t' + str(ext.numberOfLines))
	print('Summary: ' + str(sum))
				
if __name__ == "__main__":
	print('Project folder path:')
	projectPath = input() #os.getcwd()
	
	avaiableExtensions = getExtensionList(projectPath)
	pickedExtensions = chooseExtensions(avaiableExtensions)
	calculateLinesPerExtension(projectPath, pickedExtensions)
	
	
	