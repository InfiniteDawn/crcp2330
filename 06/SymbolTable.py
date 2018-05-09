# 	An Asm2Hack Assembler - Jakob Wells - May, 2018
#	Using the laid out class structure provided by the text
#	Written for Python 2.7.12 (the version that came with Ubuntu)
#
#SymbolTable.py - Handles assembling the symbols and related references.

class SymbolTable:
	def __init__(self):
		# Uses a python dictionary for the symbol table
		# These are built on a Hash Table, but offer some
		# helpful built-in functions for this type of project.
		self.symboltable = dict([("SP"  ,0),("LCL" ,1),("ARG" ,2),("THIS",3),("THAT",4),
								 ("R0"  ,0),("R1"  ,1),("R2"  ,2),("R3"  ,3),("R4"  ,4),
								 ("R5"  ,5),("R6"  ,6),("R7"  ,7),("R8"  ,8),("R9"  ,9),
								 ("R10",10),("R11",11),("R12",12),("R13",13),("R14",14),
								 ("R15",15),("SCREEN",16384),("KBD",24576)]);

	# Add a symbol:address pair to the dictionary.
	def addEntry(self,symbol,address):
		self.symboltable[symbol] = address;
		print("Added entry: " + symbol + " : " + str(address));
		return;

	# Check if a symbol is already recorded.
	def contains(self,symbol):
		return (symbol in self.symboltable);


	# Retrieve the address that corresponds to a symbol.
	def getAddress(self,symbol):
		return self.symboltable[symbol];