# 	An Asm2Hack Assembler - Jakob Wells - May, 2018
#	Using the laid out class structure provided by the text
#	Written for Python 2.7.12 (the version that came with Ubuntu)
#
#	Assembler.py - Driver for Assembler program.

from Parser import Parser
from Code import Code
from SymbolTable import SymbolTable

class Assembler:

	def assemble(self,fileInput):
		parser = Parser(fileInput);
		code = Code();

		symbols = self.firstPass(parser,code);

		output = self.secondPass(parser,code,symbols);

		# Write the assembled binary code to a file named [filename].hack
		with open(fileInput[:-3] + "hack",'w') as file:
			for line in output:
				file.write("%s\n" % line);

	def secondPass(self, parser, code):
		outputString = []
		while(parser.hasMoreCommands()):
			parser.advance();
			
			curType = parser.commandType();

			if (curType == "A_COMMAND"):
				symbol = parser.symbol();

				if self.isConstant(symbol):
					# Assemble the binary string for the constant A_COMMAND
					outputString.append("0"+self.int2Bin(int(symbol)));
				else:
					# This is a symbol, not a constant. Ignore it for now.
					pass;

			elif (curType == "L_COMMAND"):
				# No L_COMMANDs in the first iteration. Ignore it for now.
				pass;
			else: # C_COMMAND
				# Gather the peices that are present and convert to binary
				destPart = code.dest(parser.dest());
				compPart = code.comp(parser.comp());
				jumpPart = code.jump(parser.jump());

				# Assemble the binary string for the C_COMMAND
				outputString.append("111"+compPart+destPart+jumpPart);

		return outputString;

	# Helper function to determine if a A_INSTRUCTION uses a symbol or decimal constant
	def isConstant(self,inVal):
		try:				# This is a number
			i = int(inVal);
			if i >= 0: 		# This is a positive int.
				return True;
			else:			# Number is invalid
				print("Constant is Negative");
				return False;
		except ValueError:	# This isn't a number
			return False;

	# Helper function to convert an integer to its 15-bit binary notation.
	def int2Bin(self,inVal):
		# Returns a string of 15 bits corresponding to input.
		return '{0:015b}'.format(inVal);

				

testFile = "Add.asm"; # Stick the test file here!
#testFile = "RectL.asm";
#testFile = "MaxL.asm";
#testFile = "PongL.asm";

# Instantiate the driver object.
asm2hack = Assembler();
# Command an assembly.

asm2hack.assemble(testFile);