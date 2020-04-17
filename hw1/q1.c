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
        "MOV ECX, 3;" /* init i=3 */
    	"CMP EBX,1;"
    	"JG Loop1;" /* jump to gfp if input integer is bigger than 1 */
    	"MOV EAX, 0;" /* return 0 */
    	"JMP end;"
    	

   	"Loop1:;" 
    	"PUSH EBX;" /* save ebx */
    	"AND EBX, 0x01;" /* get the lsb */
    	"CMP EBX, 0;" /* check if it is 0 */
    	"JNE Break1;" /* end loop if the lsb is 1 */
    	"MOV ESI, 2;" /* max = 2 */
    	"POP EBX;" /* return to the last original value */
    	"SHR EBX, 1;" /* n>>=1 */
    	"JMP Loop1;" /* continue iterating */

    "Break1:;"
    	"POP EBX;" /* I could have kept ebx in the stack without poping and then pushing, but for the sake of clearity */
    	"PUSH EBX;" /* save current n */

    "Loop2:;"
    	"CMP ECX, [ESP];" /* check if i<n */
    	"JGE Break2;"
    	"Loop3:;"
    		"MOV EDX, 0;" /* nullify EDX so that the division will be correct */
    		"MOV EAX, EBX;" /* EAX=n so that we will divide n */
    		"DIV ECX;" /* n/i */
    		"CMP EDX, 0;" /*check if n % i ==0 */
    		"JNE Break3;" /* doesn't take the jump if n%i==0 */
    		"MOV ESI, ECX;" /* max = i */
    		"MOV EBX, EAX;" /* n = n/i */
    		"JMP Loop3;"

    	"Break3:;" 
    	"ADD ECX, 2;" /* i+=2 because we dont need to iterate over even numbers*/
    	"JMP Loop2;" /* continue iterating on i */

    "Break2:;"	
    	"ADD ESP, 4;" /*  close the stack */
    	"CMP EBX, 2;" /* n ~ 2 */
    	"JLE done;" /* if n<=2 we are done */
    	"MOV ESI, EBX;" /* max = n, this is for the case the input was a prime */

    "done:;"
    	"MOV EAX, ESI;" /* make the return value max */
    "end:;"

        /* Your code stops  here. */
    );

    asm ("MOV %0, EAX"
        : "=r"(output));

    printf("%d\n", output);
    
    return 0;
}





