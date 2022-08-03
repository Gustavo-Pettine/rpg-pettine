<h1 align="center">
  RPG Pettine
</h1>

<h4 align="center">Linguagem baseada em RPGs de turno e feita com <a href="https://www.python.org/">Python</a>.</h4>

<p align="center">
  <a href="#introdução">Introdução</a> •
  <a href="#funcionalidades">Funcionalidades</a> •
  <a href="#como-usar">Como usar</a> •
  <a href="#exemplo">Exemplo</a> •
  <a href="#produções-e-ações-semânticas">Produções e Ações Semânticas</a> •
  <a href="#apresentação">Apresentação</a> •
  <a href="#créditos">Créditos</a> •
  <a href="#license">License</a>
</p>

![cefet](https://i.imgur.com/K0E5iFC.jpg)

## Introdução
O RPG Pettine é uma linguagem feita para um trabalho acadêmico cujo objetivo é simular uma batalha de RPG em turno.

## Funcionalidades

- Shell - Shell interativo
  - Faça programas curtos, checagens rápidas ou aprendizado dinâmico.
- Parse de Arquivos
  - Para programas longos e complexo
- Simulação de batalha RPG
  - Carrega jogadores com propriedades aleatórias
  - Simula batalha através de fórmulas aleatórias

## Como usar

Link para o Vídeo da Apresentação --> https://www.youtube.com/watch?v=RcL7FJspytk.

Para clonar e rodar essa aplicação, você irá precisar [Git](https://git-scm.com), [Python](https://www.python.org/). Pelo seu terminal:

```bash
# Clone o repositório
git clone https://github.com/Gustavo-Pettine/rpg-pettine

# Entre no repositório
cd rpg-pettine

# Rode a aplicação
py main.py
```

## Exemplo

```txt
player_1 = LOAD
player_2 = LOAD
BATTLE player_1 player_2
```

Rodando o exemplo no terminal:

```bash
py main.py .\example\battle.rpg
```

## Produções e Ações Semânticas

```txt
Grammar                                         Action
------------------------                        ---------------------------------
statement : PRINT expr                          lf.print(expr.val)
          | ID = expr                           ID.val = expr.val
          | expr

expr0     : ID                                  expr0.val = self.ids[ID.val]
          | ID = expr1                          ID.val = expr1.val
          | LOAD                                expr0.val = lf.load()
          | LOAD STRING                         expr0.val = lf.load(STRING.val)
          | BATTLE expr1 expr2                  lf.battle(expr1.val, expr2.val)

select    : SELECT STRING FROM expr             lf.select_from(STRING.val, expr.val)
```

## Apresentação

### Linguagem Escolhida

A linguagem escolhida foi o python por ser dinâmicamente tipada (simples), multi-plataforma e não há necessidade de compilar para executar o projeto.

### Modificações Realizadas

No código dessa linguagem, todos os comandos básicos do exemplo da documentação do pacote escolhido (no caso uma calculadora) foram retirados. Como tokens temos as palavras reservadas ```PRINT``` que serve para printar um jogador na tela, ```LOAD``` que serve para carregar um novo jogador aleatório na memória e ```BATTLE``` que serve para iniciar uma batalha entre dois jogadores. Fora esses comandos também tem o ```ID``` que guarda o identificador da variável e a ```STRING``` que serve para auxiliar nos comandos.

Fora isso, o template do código foi retirado de [um repositório aberto](https://github.com/cassiofb-dev/pandasscript) de um aluno de compiladores fornecido pela professora em aula, onde foram realizadas diversas modificações nos arquivos, em especial nos arquivos base da linguagem (```lexer.py``` e ```parser.py```) foram alterados completamente.

### Definicições Léxicas e Gramaticais

As definições léxicas e gramaticais podem ser conferidas na Seção <a href="#produções-e-ações-semânticas">Produções e Ações Semânticas</a>. As definições de expressões regulares utilizadas para gerar os tokens podem ser encontradas no trecho de código abaixo:

```py
tokens = { ID, ASSIGN, STRING, PRINT, LOAD, BATTLE, SELECT, FROM }

  PRINT   = r"PRINT"
  LOAD    = r"LOAD"
  BATTLE  = r"BATTLE"
  SELECT  = r"SELECT"
  FROM    = r"FROM"
  ASSIGN  = r'='
  ID      = r"[a-zA-Z_]\w*"

@_(r'".*"')
def STRING(self, t):
  t.value = t.value.strip('\"')
  return t
```

### Exemplo de Árvore de Derivação

Árvore de derivação da execução de ```BATTLE player_1 player_2```:

![arvore_pettine](https://i.imgur.com/hCPNUfC.png)

### Principais Dificuldades

1. Inicialmente, escolha da linguagem e pacote.
2. Criatividade para sair do exemplo da documentação (calculadora).

## Créditos

Essa aplicação utiliza os seguintes projetos de código aberto:

- [Python](https://www.python.org/)
- [SLY](https://github.com/dabeaz/sly)
- [Pandas Script](https://github.com/cassiofb-dev/pandasscript)

## License

MIT
