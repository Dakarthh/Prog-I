#include <conio.h>
#include <stdio.h>
#include <stdlib.h>

int secc(int n) {
	if(n == 0) {
		printf("%d ", 0);
		return 0;
	}
	if(n % 2 == 0) {
		printf("%d ", n);
	}
	secc(n - 1);
}
int secc2(int n) {
	if(n < 0) {
		return -1 * secc(n);
	}
	return secc(n);
}