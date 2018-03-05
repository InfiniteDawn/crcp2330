// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
// Okay, so a *real* multiplication would be done with 
// logarithms or some kind of barrel shifting process. 
// But whatever. Easy way out it is.

// Program R2 = R0 * R1 as
// R2 = R0 + R0 + RO... (R1 times)

// I'm going to overwrite the R1 register, 
// hopefully that's fine - you'll lose the data.

	// Set R2 to zero - just to clean up
	@R2
	M=0

	// Lets check R0 is zero and skip 
	// the multiplication if it is
	@R0
	D=M
	@INPUTZERO
	D;JEQ


(GOMULT)
	// Checks if R1 is zero yet, jumps to end if so
	@R1
	D=M
	@STOPMULT
	D;JEQ

	// Adds R0 to R2
	@R0
	D=M
	@R2
	M=D+M

	// Decrements R1
	@R1
	M=M-1

	//Repeat until R1=0
	@GOMULT
	0;JMP


(INPUTZERO)
	
	// Lazy way to catch the case where R0 is zero
	// Just sets the output R2 to zero as well
	@R2
	M=0

	@TERM
	0;JMP

(TERM)
	
	@TERM
	0;JMP // Loop Forever
