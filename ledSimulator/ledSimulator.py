'''
Bitwise operations:
	a) bit shifting: <<, >>
	b) logic: &, |, ~, ^(XOR)
 '''
import os

def hexToBin(hexString):
	return bin(hexString)[2:]
	
def decToHex(decString):
	return hex(decString)
	
os.system('cls')
print("Choose start value:")
v = int(input())
os.system('cls')

while(True):
	print("Hex: v = " + str(decToHex(v)))
	print("LEDs: " + str(list(hexToBin(v))))
	print("v = ", end='')
	v = eval(input())