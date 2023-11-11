#include <stdio.h>


int main(void)

{
  int iVar1;
  char local_28 [32];
  
  printf("Password: ");
  __isoc99_scanf("DoYouEven%sCTF",local_28);
  printf(local_28);
  iVar1 = strcmp(local_28,"__dso_handle");
  if ((-1 < iVar1) && (iVar1 = strcmp(local_28,"__dso_handle"), iVar1 < 1)) {
    printf("here Try again!");
    return 0;
  }
  iVar1 = strcmp(local_28,"_init");
  if (iVar1 == 0) {
    printf("Correct!");
  }
  else {
    printf("Try again!");
  }
  return 0;
}

