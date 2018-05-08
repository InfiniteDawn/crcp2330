# 	An Asm2Hack Assembler - Jakob Wells - May, 2018
#	Using the laid out class structure provided by the text
#	Written for Python 2.7.12 (the version that came with Ubuntu)
#
#	Assembler.py - Driver for Assembler program.

from Parser import Parser
#import SymbolTable.py

class Assembler:
	def assemble(self,fileInput):
		parser = Parser(fileInput);
		while(parser.hasMoreCommands()):
			parser.advance();
		


testFile = "Add.asm"; # Stick the test file here!

asm2hack = Assembler();
asm2hack.assemble(testFile);