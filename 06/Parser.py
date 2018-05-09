# 	An Asm2Hack Assembler - Jakob Wells - May, 2018
#	Using the laid out class structure provided by the text
#	Written for Python 2.7.12 (the version that came with Ubuntu)
#
#	Parser.py - Handles input parsing.

class Parser:
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
					self.coms.append(l.strip());

	# Check if the instruction list still has more left to go
	def hasMoreCommands(self):
		if (self.comIndex < len(self.coms) - 1):
			return True;
		else:
			return False;

	# Move up the current instruction
	def advance(self):
		self.comIndex += 1;
		self.curCom = self.coms[self.comIndex];
		# print(str(comIndex) + " : " + curCom);

	# Check what kind of instruction the current command is
	def commandType(self):
		if(self.curCom[0] == '@'):
			return "A_COMMAND";
		
		elif(self.curCom[0] == "("):
			return "L_COMMAND";
		
		else:
			return "C_COMMAND";

	# Pull the symbol/constant out of an A or L command
	def symbol(self):
		# Remove the @ and parenthesis to expose the symbol/constant
		outSym = self.curCom.translate(None,'@()');
		return outSym;

	# Pull the Destination component out of a C command
	def dest(self):
		# Check if there *is* a dest in the command
		if '=' in self.curCom:
			# Split the command at the equal sign and take the first part.
			outDest = self.curCom.split('=')[0];
			return outDest;
		else:
			return "";

	# Pull the Computation component out of a C command
	def comp(self):
		outComp = self.curCom;
		# Check if there is a dest in the command
		if '=' in outComp:
			# Remove the dest component.
			outComp = outComp.split('=')[1];

		# Check if there is a jump in the command
		if ';' in outComp:
			# Remove the jump component.
			outComp = outComp.split(';')[0];

		# Return whatever is left at this point - it should be the comp.
		return outComp;

	# Pull the Jump component out of a C command
	def jump(self):
		# Check if there *is* a jump in the command
		if ';' in self.curCom:
			# Split the command at the semicolon and take the second part.
			outJump = self.curCom.split(';')[1];
			return outJump;
		else:
			return "";

	# This function is not defined by the book, but my implementation makes it
	# easier to just go through the list again rather than bother with dealing
	# with the actual input file a second time (as a plus, comments are pre-deleted).
	def resetParser(self):
		self.curCom = -1;
