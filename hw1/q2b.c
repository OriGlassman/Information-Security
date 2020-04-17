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
        "MOV ECX, 2;" /*  i=2  */
        "MOV EAX, 1;" /* b=1*/
        "MOV ESI, 0;" /* a=0 */
    "_Loop:;"
        "CMP ECX, EBX;" /* i ~ n */
        "JG _done;"
        "MOV EDI, ESI;" /*  temp = a  */
        "ADD EDI, EAX;" /* temp = a+b */
        "MOV EDX, EDI;" /* c= a+b */
        "MOV ESI, EAX;" /* a=b */
        "MOV EAX, EDX;" /* b=c */
        "INC ECX;" /* i++ */
        "JMP _Loop;" /* continue loop */


    "_done:;"


        /* Your code stops  here. */
    );

    asm ("MOV %0, EAX"
        : "=r"(output));

    printf("%d\n", output);
    
    return 0;
}
