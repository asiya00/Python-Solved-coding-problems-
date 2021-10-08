#include <stdio.h>

int main()
{
   char dst[12] = "pre_";
   itoa(i, dst+4, 10);
   strcat(dst, "_suff");
   printf("%s\n",dst);
}