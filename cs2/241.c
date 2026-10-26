#include<stdio.h>
#include<stdbool.h>
int main(){int a,b;
	scanf("%d %d",&a,&b);

	int x=a&b;
	printf("a&b is:%d\n",x);
	int y=a&&b;
	printf("a&&b is:%d\n",y);
	return 0;}
