#include <stdio.h>
#include <math.h>

int main()
{
    double x = 1;
    double xnew;

    for(int i = 0; i < 5; i++)
    {
        xnew = x - (exp(x) - 2) / exp(x);

        printf("x%d = %.3f\n", i + 1, xnew);

        x = xnew;
    }

    return 0;
}
