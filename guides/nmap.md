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

### Tipos de scan
Scan Furtivo -sS
Scan UDP -sU
Scan operating system -O
Scan Services Version
Show verbose -v
Show Very Verbose -vv
Save response in xml -oX
Agressive Scan -A
Insane Scan Speed -T5
Scan port -p1-1000  Scan 1 at 1000 have 65535
Scan all ports -p-
Ping in Sacn -Pn
tcp OR udp

