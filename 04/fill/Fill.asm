// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// So. The way I'm going to fill is by basically marking ever other
// pixel in a word on each pass - so it takes two full passes to
// darken / clear. I just think that's a nicer effect.

// I'm also making the choice to just write whatever the keyboard state
// says. So black if Key=Pressed, white otherwise.

// Thus, the write/clear operation will _not_ restart when the state changes


	// We'll use R0 as an Address marker. Cause its easier that way.
	// We initialize it to the Screen pointer.
	@SCREEN
	D=A
	@R0
	M=D

	// For simplicities sake:
	// R7 is the "Pass 1" darken or "Pass 2" clear
	// R8 is the "Pass 2" darken or "Pass 1" clear

	// Quick complaint - I can only load 15-bit values. Which is stupid.
	// So R8 requires me to load what I loaded for R7, and shift by one.
	@21845 // == 0101 0101 0101 0101
	D=A
	@R7
	M=D

	@R7 
	D=M
	D=D+M // Add number to itself - shifting it by one.
	@R8
	M=D // == 1010 1010 1010 1010
	

	// Start with PASS 1
	@R7
	D=M
	@R1
	M=D

	// NOW... We are ready to begin

(LOOPSTART)
	
	// First off, we check the keyboard *value*
	@KBD
	D=M
	@FILLWHITE
	D;JEQ // Jump to FillWhite if KBD is empty

	@FILLBLACK
	0;JMP // Else, jump to FillBlack


(FILLBLACK)
	
	// Write the current darken filter with an OR operation on address word
	@R1
	D=M
	@R0
	A=M // Sets my address to the value inside R0	
	M=D|M // This basically sets 0's to 1's according to our current filter


	@LOOPEND
	0;JMP // Now we just jump to the end of the loop


(FILLWHITE)

	// Write the current clear filter with an AND operation on address word
	@R1
	D=M
	@R0
	A=M // Sets my address to the value inside R0	
	M=D&M // This basically sets 1's to 0's according to our current filter

(LOOPEND)
	
	//Incremement screen-writing address
	@R0
	M=M+1

	// Check if screen address is past limits
	@R0
	D=M
	@KBD 	// Limit of screen address memory is the Keyboard address as it happens
	D=D-A

	@RESETADDRESS
	D;JEQ 	// Loop if R0 = KBD Address - which means we have left the bounds
	
	@REPEAT
	0;JMP 	// Otherwise, we just loop.

(RESETADDRESS)
	
	// Reset R0 to the base Screen Address
	@SCREEN
	D=A
	@R0
	M=D

	// Now, we check what pass we are on and toggle to the other pass
	@R7
	D=M
	@R1
	D=D-M		// Compare R7 and R1
	
	@RESET2PASS2
	D;JEQ		// Basically, if R7-R1=0, then we jump to PASS2
	
	@RESET2PASS1
	0;JMP 		// Else, we jump to PASS1

(RESET2PASS1)
	
	@R7
	D=M
	@R1
	M=D 		// Set R1 to R7

	@REPEAT
	0;JMP

(RESET2PASS2)

	@R8
	D=M
	@R1
	M=D 		// Set R1 to R8

(REPEAT)

	@LOOPSTART
	0;JMP