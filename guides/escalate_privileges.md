# Users

## Qual meu user
```
whoami
```
## Listar users
```
cd /home
ls -al
```

# Permissões especiais

## Bit SUID

Ele é executado com as permissões de seu dono, com o dono sendo um admin podemos nos aproveitar da permissão dele
O Bit Suid é o 4 ou s 

Como o exemplo do arquivo para alterar sua senha, ele deve alterar ela em um arquivo que você não tem permissão.

## Proucurando arquivos com essa permissão
Legenda
- find -> Proucura
- / -> diretorio base do sistema
- -perm parametro de filtrar por permissão
- 4000 binario da permissão buscada
- 2>/dev/null não trazer error
```
find / -perm -4000 2>/dev/null
```

