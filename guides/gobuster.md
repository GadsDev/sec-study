### Comando basico
```
gobuster dir -u http://<ip>:3333 -w <word list location>
```

### Exemplo de scan basico
```
gobuster dir -u http://10.10.28.119:3333/ -w /usr/share/wordlists/dirb/common.txt -t 50
```
##### Legenda
- dir faz o scan de diretorios
- -u rota http e porta
- -w wordlist
- -t número de palavras por quest(um número grande pode te bloquear do site)
