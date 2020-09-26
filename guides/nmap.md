### Services

```
nmap -sV ip
```
### Filtrar por portas
Scaneia da primeira porta até a 400
```
nmap -sV ip -p-400
```

### Parametro -n
Não resolve DNS

### Escanenado outras portas
O nmap sem parametros scaneia até a porta 1000
Existem 65535 portas
Para faer um scan em todas com o -T4 agilia o scan
```
nmap -sS -p1-65535 10.10.47.26 -T4
```
