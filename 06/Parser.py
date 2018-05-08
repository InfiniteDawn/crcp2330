# 	An Asm2Hack Assembler - Jakob Wells - May, 2018
#	Using the laid out class structure provided by the text
#	Written for Python 2.7.12 (the version that came with Ubuntu)
#
#	Parser.py - Handles input parsing.

import Code; # For use in "translating"

class Parser:
	# Make a symbol whitelist - anything that uses characters 
	# outside this whitelist will throw a parsing error.
	symbolWhitelist = set('abcdefghijklmnopqrstuvwxyz' +
						  'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 
						  '1234567890_.$:');
	# Index within command list. Initialized to -1 so it
	# requires an initial advance() to enter the list proper
	comIndex = -1;
	# Temporary container for currently parsing command
	curCom = "";
	# List for instructions
	coms = [];

	# Initialize by loading in the file as a list of instructions
	def __init__(self,fileInput):
		
		# Retrieve all commands for easy access in list form.
		with open(fileInput) as file:
			# Dump file into a list of lines
			temp = file.readlines();
			# Clear whitespace. Filter out empty lines and comments
			for l in temp:
				if (l.strip() != "" and "//" not in l):
					coms.append(l.strip());

	# Check if the instruction list still has more left to go
	def hasMoreCommands(self):
		if (comIndex < len(coms) - 1):
			return True;
		else:
			return False;

	# Move up the current instruction
	def advance(self):
		comIndex += 1;
		curCom = coms[comIndex];
		# print(str(comIndex) + " : " + curCom);

	# Check what kind of instruction the current command is
	def commandType(self):
		if(curCom[0] == '@'):
			return "A_COMMAND";
		
		elif(curCom[0] == "("):
			return "L_COMMAND";
		
		else:
			return "C_COMMAND";

	# Pull the symbol/constant out of an A or L command
	def symbol(self):
		# 


		pass; # Insert Code

		return outSym;

	# Pull the Destination component out of a C command
	def dest(self):
		outDest = "";

		pass; # Insert Code

		return outDest;

	# Pull the Computation component out of a C command
	def comp(self):
		outComp = "";

		pass; # Insert Code

		return outComp;

	# Pull the Jump component out of a C command
	def jump(self):
		outJump = "";

		pass; # Insert Code

		return outJump;
