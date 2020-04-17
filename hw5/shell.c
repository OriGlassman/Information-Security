#include <sys/socket.h>
#include <stdio.h>
#include <arpa/inet.h>
#include <sys/types.h>





int main(){
	int sockfd;
	struct sockaddr_in serv_addr = {0};
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(1337);
	serv_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
	connect(sockfd, (struct sockaddr*) &serv_addr, sizeof(serv_addr));






	return 0;
}