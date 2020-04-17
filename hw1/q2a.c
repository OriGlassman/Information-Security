#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    int input, output;

    if (argc != 2) {
        printf("USAGE: %s <number>\n", argv[0]);
        return -1;
    }

    input = atoi(argv[1]);

    asm ("MOV EBX, %0"
        :
        : "r"(input));

    asm (
        /* Your code starts here. */
        "CMP EBX, 0;" /* */
        "MOV EAX, 0;" /* prepare return value EAX=0 */
        "JLE _done;" /* check if EBX <= 0 */
        "PUSH EBX;" /* set function argument to n */
        "CALL FIB;" /* call fib(n) */
        "JMP _done;" /* finish up */
 "FIB:;" 
 		"PUSH EBP;" /* set frame pointer */
    	"MOV EBP, ESP;" /* set frame pointer */

    	"MOV EBX, [EBP+8];" /* get the argument n */
    	"CMP EBX, 1;" /* n ~ 1 */
    	"JG Recursion;" /* if n>1 jump to recursion. else, return n */
    	"MOV EAX, EBX;" /* return n */
    	"JMP _exit;" /* close the current recursive call */

  "Recursion:;"
  		"PUSH EDX;" /* save the value of EDX for further work */
  		"DEC EBX;" /* n-- */
  		"PUSH EBX;" /* set the argument to n-- */
  		"CALL FIB;" /* call f(n-1)*/
  		"MOV EDX, EAX;" /* save f(n-1) in EDX */
  		"DEC DWORD PTR [ESP];" /* n-- (decrease the value of n-1 in the stack) */
  		"CALL FIB;" /* call f(n-2) */
  		"ADD EAX, EDX;" /* calculate f(n-1) + f(n-2) */
  		"ADD ESP, 4;" /* clear n-2 from the stack */
  		"POP EDX;" /* return to the original value of EDX */

  "_exit:;"  	
  		"MOV ESP, EBP;" /* return frame pointer */
    	"POP EBP;" /* return frame pointer */
    	"RET;"

    "_done:;"


        /* Your code stops  here. */
    );

    asm ("MOV %0, EAX"
        : "=r"(output));

    printf("%d\n", output);
    
    return 0;
}
