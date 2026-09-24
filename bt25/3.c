#include<stdio.h>
int main(){double sum=0.0;int n=1;double term;float den=1.0;
	do{den=den*n;
	 term=1.0/den;
		sum=sum+term;n++;}
	while(term>1e-10);
		printf("%lf",sum);
	return 0;}

