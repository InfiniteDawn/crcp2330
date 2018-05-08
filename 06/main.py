# 	An Asm2Hack Assembler - Jakob Wells - May, 2018
#	Using the laid out class structure provided by the text
#	Written for Python 2.7.12 (the version that came with Ubuntu)
#
#	Assembler.py - Driver for Assembler program.

from Parser import Parser
#import SymbolTable.py

class Assembler:

	outputString = []

	def assemble(self,fileInput):
		parser = Parser(fileInput);
		while(parser.hasMoreCommands()):
			parser.advance();
			
			curType = parser.commandType();

			if (curType = "A_COMMAND"):
				symbol = parser.symbol();

				if isConstant(symbol):
					outputString.append("0"+int2Bin(symbol));
				else:
					# This is a symbol, not a constant. Ignore it for now.
					pass;

			elif (curType = "L_COMMAND"):

			else: # C_COMMAND
	def isConstant(self,inVal):
		try:				# This is a number
			i = int(inVal);
			if i >= 0: 		# This is a positive int.
				return True;
			else:			# Number is invalid
				print("Invalid Constant!");
				return False;
		except ValueError:	# This isn't a number
			return False;
	def int2Bin(self,inVal):
		# Returns a string of 15 bits corresponding to input.
		return '{0:015b}'.format(inVal);

				


testFile = "Add.asm"; # Stick the test file here!

asm2hack = Assembler();
asm2hack.assemble(testFile);