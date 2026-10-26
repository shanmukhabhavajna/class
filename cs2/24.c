#include<stdio.h>
#include<stdbool.h>
int main(){int  a,b,c,X;
         printf("%c %c %c %c\n",'a','b','c','X');
      for(a=0;a<=1;a++){for(b=0;b<=1;b++){for(c=0;c<=1;c++){


	      X=(a&b)||(b&c)||(c&a);
	      printf("%d %d %d %d",a,b,c,X);
	      printf("\n");}}}
      return 0;}
