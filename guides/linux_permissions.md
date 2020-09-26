# Permissões

# Tipos
- Leitura -> r
- Gravação -> w
- Execução -> x

# Niveis de acesso: são 4 digitos
- 1 Permissões especiais
- 2 Permissão da pessoa que criou
- 3 Permissões de membros do mesmo grupo de quem criou
- 4 Permissão dos outros users

# Exemplo

Executando o ls -l no arquivo discord-0.0.12.deb  com o user therion

```
-rw-r--r-- 1 therion therion 68328818 Sep 26 12:59 discord-0.0.12.deb
```

- Bloco 1(Tipo de arquivo): - -> É um arquivo normal, caso seja um diretorio seria d
- Bloco 2(Quem criou): rw- -> Pode lêr e escrever
- Bloco 3(Grupo): r-- -> Só pode lêr
- Bloco 4(O restante): r-- -> Só pode lêr

# Alterando isso com chmod
Legendas:
- u usuario
- g grupo
- O outros
- a todos
- r leitura
- w gravação
- x execução

Esse comando vai adicionar a permissão w para o grupo
```
chmod g+w discord-0.0.12.deb
```
Agora temos a permissão do arquivo assim
```
-rw-rw-r-- 1 therion therion 68328818 Sep 26 12:59 discord-0.0.12.deb
```