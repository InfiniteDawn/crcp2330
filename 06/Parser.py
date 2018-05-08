# 	An Asm2Hack Assembler - Jakob Wells - May, 2018
#	Using the laid out class structure provided by the text
#	Written for Python 2.7.12 (the version that came with Ubuntu)
#
#	Parser.py - Handles input parsing.

import Code; # For use in "translating"

class Parser:
	def __init__(self,fileInput):
		self.file = fileInput;
		self.comIndex = -1; # Start a -1 index - first advance will enter the list.
		self.curCom = "";
		self.coms = [];

		# Retrieve all commands for easy access in list form.
		with open(fileInput) as file:
			# Dump file into a list of lines
			temp = file.readlines();
			# Clear whitespace. Filter out empty lines and comments
			for l in temp:
				if (l.strip() != "" and "//" not in l):
					self.coms.append(l.strip());


	def hasMoreCommands(self):
		if (self.comIndex < len(self.coms) - 1):
			return True;
		else:
			return False;

	def advance(self):
		self.comIndex += 1;
		self.curCom = self.coms[self.comIndex];
		print(str(self.comIndex) + " : " + self.curCom);

	def commandType(self):
		if(self.curCom[0] == '@'):
			return "A_COMMAND";
		
		elif(self.curCom[0] == "("):
			return "L_COMMAND";
		
		else:
			return "C_COMMAND";
		

	def symbol():
		outSym = "";

		pass; # Insert Code

		return outSym;

	def dest():
		outDest = "";

		pass; # Insert Code

		return outDest;

	def comp():
		outComp = "";

		pass; # Insert Code

		return outComp;

	def jump():
		outJump = "";

		pass; # Insert Code

		return outJump;
