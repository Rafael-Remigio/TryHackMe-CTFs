# Compiled


First i tried to run string on the file but this was not the solution

I decompiled the code using **Ghidra**

### Code

```
undefined8 main(void)

{
  int iVar1;
  char local_28 [32];
  
  fwrite("Password: ",1,10,stdout);
  __isoc99_scanf("DoYouEven%sCTF",local_28);
  iVar1 = strcmp(local_28,"__dso_handle");
  if ((-1 < iVar1) && (iVar1 = strcmp(local_28,"__dso_handle"), iVar1 < 1)) {
    printf("Try again!");
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
```

We can see a lot of hardcoded string already. The program start by create 2 varibles.

ScanF reads the input with the format "DoYouEven%sCTF", this means that if the input is DoYouEvenSomething, local28 will have the value of Something. You can test this by changing and recompiling the code.

The code then compares the local_28 var with the string "__dso_handle", if it is equal to "__dso_handle" then its prints "Try Again"

If not the code then compares to the local_28 and the "_init" string, if it is the same then the password is correct. 

Knowing this, we can see that the password is DoYouEven_init. This is because we want the value of local_28 to be "_init".
