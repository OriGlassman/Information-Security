#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <sys/ptrace.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>

int pid = 0x12345678;
int addr = 0x91011121;

int main() {
	if (ptrace(PTRACE_ATTACH, pid,NULL,NULL)==-1){
		perror("attach");
		return 1;
	}
	int status;
	waitpid(pid, &status, 0);
	if (WIFEXITED(status)){ 
		printf("wifexited\n");
		return 2;
	}

	int assembled_new_func = 0x00c3c031; // xor eax, eax ; ret

	if (ptrace(PTRACE_POKETEXT, pid, addr, assembled_new_func)== -1){
			perror("poketext");
			return 1;
	}


	if (ptrace(PTRACE_DETACH, pid, NULL, NULL)== -1){
		perror("detach");
		return 1;
	}





    return 0;
}
