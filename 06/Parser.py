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
		# Remove the @ and parenthesis to expose the symbol/constant
		return curCom.translate(None,'@()');

	# Pull the Destination component out of a C command
	def dest(self):
		# Check if there *is* a dest in the command
		if '=' in curCom:
			# Split the command at the equal sign and take the first part.
			outDest = curCom.split('=')[0];
			return outDest;
		else:
			return "";

	# Pull the Computation component out of a C command
	def comp(self):
		outComp = curCom;
		# Check if there is a dest in the command
		if '=' in outComp:
			# Remove the dest component.
			outComp = outcomp.split('=')[1];
			
		# Check if there is a jump in the command
		if ';' in outComp:
			# Remove the jump component.
			outComp = outcomp.split(';')[0];

		# Return whatever is left at this point - it should be the comp.
		return outComp;

	# Pull the Jump component out of a C command
	def jump(self):
		# Check if there *is* a jump in the command
		if ';' in curCom:
			# Split the command at the semicolon and take the second part.
			outJump = curCom.split(';')[1];
			return outJump;
		else:
			return "";
