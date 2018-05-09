# 	An Asm2Hack Assembler - Jakob Wells - May, 2018
#	Using the laid out class structure provided by the text
#	Written for Python 2.7.12 (the version that came with Ubuntu)
#
#	Assembler.py - Driver for Assembler program.
#
#	It is assumed that the .asm file provided is without error - 
#	invalid programs may produce unpredictable results from this assembler

from Parser import Parser
from Code import Code
from SymbolTable import SymbolTable

class Assembler:

	def assemble(self,fileInput):
		parser = Parser(fileInput);
		code = Code();
		symtab = SymbolTable();

		# Run the first pass to handle labels.
		self.firstPass(parser,symtab);

		# Reset the parser index for the second pass.
		parser.resetParser();

		# Run the second pass to assembly the code, with labels included.
		output = self.secondPass(parser,code,symtab);

		# Write the assembled binary code to a file named [filename].hack
		with open(fileInput[:-3] + "hack",'w') as file:
			for line in output:
				file.write("%s\n" % line);
		return;

	def firstPass(self,parser,symtab):
		programCounter = 0;
		memoryCounter = 16;

		while(parser.hasMoreCommands()):
			parser.advance();

			curType = parser.commandType();

			if (curType == "A_COMMAND"):
				symbol = parser.symbol();

				if self.isConstant(symbol):
					# Its not a label, so we can ignore it for now.
					pass;
				else:
					# Check if the symbol is in the symbol table yet.
					if not symtab.contains(symbol):
						# Add symbol to this table, at the smallest available memory location
						symtab.addEntry(symbol,memoryCounter);
						memoryCounter += 1;

				programCounter += 1;

			elif (curType == "L_COMMAND"):
				label = parser.symbol();

				# Check if the label is currently in the table
				# Assume a currently present label is ignored.
				if not symtab.contains(symbol):
					# Add symbol to this table, at the current program address
					symtab.addEntry(symbol,programCounter);

					# Don't increment the program counter for labels!
				
			else: # C_COMMAND
				programCounter += 1;		


	def secondPass(self, parser, code, symtab):
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
					# Pull in whatever value this label corresponds to.
					value = symtab.getAddress(symbol);

					# Assemble the binary string for the variable A_COMMAND
					outputString.append("0"+self.int2Bin(value));
		

			elif (curType == "L_COMMAND"):
				pass; # Ignore labels in the second pass.

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

				

testFile = "Max.asm"; # Stick the test file here!
#testFile = "RectL.asm";
#testFile = "MaxL.asm";
#testFile = "PongL.asm";

# Instantiate the driver object.
asm2hack = Assembler();
# Command an assembly.

asm2hack.assemble(testFile);