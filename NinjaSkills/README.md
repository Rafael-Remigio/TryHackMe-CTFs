# Ninja Skills

A machine to practice linux skills

I use 2>/dev/null a lot here. 2>/dev/null simply redirects the erros output of the command to /dev/null, and that is the same as not printing it. This is mostly because there are a lot of folder with that we don't have permissions to, so it will print a lot of errors. 

Files:
|File|Location|
|----|----|
| 8V2L | /etc/8V2L | 
| bny0 | don't know|
| c4ZX | /mnt/c4ZX |
| D8B3 | /mnt/D8B3 |
| FHl1 | /var/FHl1 |
| oiMO | /opt/oiMO |
| PFbD | /opt/PFbD|
| rmfX | /media/rmfX|
| SRSq | /etc/ssh/SRSq|
| uqyw | /var/log/uqyw|
| v2Vb | /home/v2Vb |
| X1Uy | /X1Uy |

## Which of the above files are owned by the best-group group(enter the answer separated by spaces in alphabetical order)

We can use the find command for this

```
$ find / -group best-group 2>/dev/null
/mnt/D8B3
/home/v2Vb
```

## Which of these files contain an IP address?

For this we can use the grep and lookup everyfile on the list

**Regex for IP Address:** ```([0-9]{1,3}[\.]){3}[0-9]{1,3}```

```
#!/bin/bash

FilesString="/etc/8V2L /mnt/c4ZX /mnt/D8B3 /var/FHl1 /opt/oiMO /opt/PFbD /media/rmfX /etc/ssh/SRSq /var/log/uqyw /home/v2Vb /X1Uy"

for file in $FilesString; do
        echo $file
        grep -Eo  "([0-9]{1,3}[\.]){3}[0-9]{1,3}" $file
done
```
```
[new-user@ip-10-10-241-240 ~]$ ./ex2.sh 
/etc/8V2L
/mnt/c4ZX
/mnt/D8B3
/var/FHl1
/opt/oiMO
1.1.1.1
/opt/PFbD
/media/rmfX
/etc/ssh/SRSq
/var/log/uqyw
/home/v2Vb
/X1Uy
```

## Which file has the SHA1 hash of 9d54da7584015647ba052173b84d45e8007eba94

```sha1sum filename```

```
#!/bin/bash

FilesString="/etc/8V2L /mnt/c4ZX /mnt/D8B3 /var/FHl1 /opt/oiMO /opt/PFbD /media/rmfX /etc/ssh/SRSq /var/log/uqyw /home/v2Vb /X1Uy"

for file in $FilesString; do
        echo $file
        sha1sum $file
done

```

```
./ex3.sh 
/etc/8V2L
0323e62f06b29ddbbe18f30a89cc123ae479a346  /etc/8V2L
/mnt/c4ZX
9d54da7584015647ba052173b84d45e8007eba94  /mnt/c4ZX
/mnt/D8B3
2c8de970ff0701c8fd6c55db8a5315e5615a9575  /mnt/D8B3
/var/FHl1
d5a35473a856ea30bfec5bf67b8b6e1fe96475b3  /var/FHl1
/opt/oiMO
5b34294b3caa59c1006854fa0901352bf6476a8c  /opt/oiMO
/opt/PFbD
256933c34f1b42522298282ce5df3642be9a2dc9  /opt/PFbD
/media/rmfX
4ef4c2df08bc60139c29e222f537b6bea7e4d6fa  /media/rmfX
/etc/ssh/SRSq
acbbbce6c56feb7e351f866b806427403b7b103d  /etc/ssh/SRSq
/var/log/uqyw
57226b5f4f1d5ca128f606581d7ca9bd6c45ca13  /var/log/uqyw
/home/v2Vb
7324353e3cd047b8150e0c95edf12e28be7c55d3  /home/v2Vb
/X1Uy
59840c46fb64a4faeabb37da0744a46967d87e57  /X1Uy
```

## Which file contains 230 lines?

```
#!/bin/bash

FilesString="/etc/8V2L /mnt/c4ZX /mnt/D8B3 /var/FHl1 /opt/oiMO /opt/PFbD /media/rmfX /etc/ssh/SRSq /var/log/uqyw /home/v2Vb /X1Uy"

for file in $FilesString; do
        echo $file
        wc -l $file
done
```

```
./ex4.sh 
/etc/8V2L
209 /etc/8V2L
/mnt/c4ZX
209 /mnt/c4ZX
/mnt/D8B3
209 /mnt/D8B3
/var/FHl1
209 /var/FHl1
/opt/oiMO
209 /opt/oiMO
/opt/PFbD
209 /opt/PFbD
/media/rmfX
209 /media/rmfX
/etc/ssh/SRSq
209 /etc/ssh/SRSq
/var/log/uqyw
209 /var/log/uqyw
/home/v2Vb
209 /home/v2Vb
/X1Uy
209 /X1Uy
```
Only one file is not here, so that file must have the 230 lines

## Which file's owner has an ID of 502?

We can use ```ls -n```

The output would be something like this: ```-rwxrwxr-x 1 501 501 13545 Oct 23  2019 /etc/8V2L```.
The first collumns is the number of links, the second is the user ID, the thrd is the group id.


```
#!/bin/bash

FilesString="/etc/8V2L /mnt/c4ZX /mnt/D8B3 /var/FHl1 /opt/oiMO /opt/PFbD /media/rmfX /etc/ssh/SRSq /var/log/uqyw /home/v2Vb /X1Uy"

for file in $FilesString; do
        echo $file
        ls -n $file
done
```

## Which file is executable by everyone?

We can reuse the script from the previous exercise. If the file has the last bit set to X then it is executable by everyone regardless of group or user.

```-rwxrwxr-x 1 501 501 13545 Oct 23  2019 /etc/8V2L```