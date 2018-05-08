# 	An Asm2Hack Assembler - Jakob Wells - May, 2018
#	Using the laid out class structure provided by the text
#	Written for Python 2.7.12 (the version that came with Ubuntu)
#
#	Code.py - Handles translating mnemonics to bitstrings
#	Less a class, and more a collection of useful functions and information

class Code:
	# Key:Value Pairs for COMP mnemoic to binary translation purposes.
	compDict = dict([("0"  ,"0101010"),("1"  ,"0111111"),("-1" ,"0111010"),("D"  ,"0001100"),
					 ("A"  ,"0110000"),("!D" ,"0001101"),("!A" ,"0110001"),("-D" ,"0001111"),
					 ("-A" ,"0110011"),("D+1","0011111"),("A+1","0110111"),("D-1","0001110"),
					 ("A-1","0110010"),("D+A","0000010"),("D-A","0010011"),("A-D","0000111"),
					 ("D&A","0000000"),("D|A","0010101"),("M"  ,"1110000"),("!M" ,"1110001"),
					 ("-M" ,"1110011"),("M+1","1110111"),("M-1","1110010"),("D+M","1000010"),
					 ("D-M","1010011"),("M-D","1000111"),("D&M","1000000"),("D|M","1010101")]);
	# Key:Value Pairs for DEST mnemoic to binary translation purposes.
	destDict = dict([(""   ,"000"),("M"  ,"001"),("D"  ,"010"),("MD" ,"011"),
					 ("A"  ,"100"),("AM" ,"101"),("AD" ,"110"),("AMD","111")]);
	# Key:Value Pairs for JUMP mnemoic to binary translation purposes.
	jumpDict = dict([(""   ,"000"),("JGT","001"),("JEQ","010"),("JGE","011"),
					 ("JLT","100"),("JNE","101"),("JLE","110"),("JMP","111")]);

	# Returns a 3-bit code corresponding to the input
	def dest(self,inDest):
		if inDest in self.destDict:
			return self.destDict[inDest];
		else:
			print("ERROR - Dest Not Recognized");
			return None;

	# Returns a 7-bit code corresponding to the input
	def comp(self,inComp):
		if inComp in self.compDict:
			return self.compDict[inComp];
		else:
			print("ERROR - Comp Not Recognized");
			return None;

	# Returns a 3-bit code corresponding to the input
	def jump(self,inJump):
		if inJump in self.jumpDict:
			return self.jumpDict[inJump];
		else:
			print("ERROR - Jump Not Recognized");
			return None;
