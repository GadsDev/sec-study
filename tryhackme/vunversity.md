- IP 10.10.51.34

### nmap 
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

### Servidor Web
Apache 2.4.18 rodando na porta 3333/tcp

deb https://http.kali.org/kali kali-rolling main non-free contrib
