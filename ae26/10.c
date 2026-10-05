#include<stdio.h>
#include<math.h>
int main(){int r1=1;
	int s=4;
	float r2=7.0-4*pow(2,0.5);
	printf("%f",r2);
	//verification//
	float result=r1+r2+r2*sqrt(2)+sqrt(2)*r1;
        if((result-pow(32,0.5))<0.0001){printf("answer is correct");}
			else{printf("wrong answ");}
			return 0;}
