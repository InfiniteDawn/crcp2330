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
		self.symboltable = dict();

	# Add a symbol:address pair to the dictionary.
	def addEntry(self,symbol,address):
		pass;

	# Check if a symbol is already recorded.
	def contains(self,symbol):
		pass;

	# Retrieve the address that corresponds to a symbol.
	def getAddress(self,symbol):
		pass;