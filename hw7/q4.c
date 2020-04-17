#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/ptrace.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <sys/user.h>


int main(int argc, char **argv) {
    // Make the malware stop waiting for our output by forking a child process:
    if (fork() != 0) {
        // Kill the parent process so we stop waiting from the malware
        return 0;
    } else {
        // Close the output stream so we stop waiting from the malware
        fclose(stdout);
    }

    // The rest of your code goes here
    pid_t pid = atoi(argv[1]);
    struct user_regs_struct regs;
    if (ptrace(PTRACE_ATTACH, pid,NULL,NULL)==-1){
        perror("attach");
        return 1;
    }
    while (1){
        int status;
        waitpid(pid, &status, 0);

        if (ptrace(PTRACE_SYSCALL,pid,NULL,NULL)==-1){
            perror("first syscall");
            return 1;
        }
        waitpid(pid, &status, 0);
        
        if (ptrace(PTRACE_GETREGS,pid,NULL,&regs)==-1){
            perror("getregs");
            return 1;
        }

        if (regs.orig_eax==3){
            regs.edx=0;
        }

        if (ptrace(PTRACE_SETREGS,pid,NULL,&regs)==-1){
            perror("setregs");
            return 1;
        }    
  
        if (ptrace(PTRACE_SYSCALL,pid,NULL,NULL)==-1){
            perror("second syscall");
            return 1;
        }              
    }

    if (ptrace(PTRACE_DETACH, pid, NULL, NULL)== -1){
        perror("detach");
        return 1;
    }

    return 0;
}
