# Maze Solver 🐢

Esse é um projeto simples para resolver labirintos usando Python e a biblioteca `turtle`. Ele lê um arquivo `maze.txt`, desenha o labirinto e usa uma busca recursiva para encontrar o caminho até a saída.

## Como funciona?
- O labirinto é lido de um arquivo de texto onde:
  - `+` representa paredes
  - `S` é o ponto de início
  - `M` é a saída
- O programa desenha o labirinto na tela usando a `turtle`.
- Ele tenta encontrar um caminho válido usando backtracking.
- Se encontrar a saída, o caminho correto fica verde. Se for um beco sem saída, marca de vermelho.

## Como rodar o projeto?
1. Tenha o Python instalado (3.x).
2. Salve seu labirinto no arquivo `maze.txt`.
3. Rode o script:
   ```sh
   python maze_solver.py
   ```

## Exemplo de labirinto (`maze.txt`)
```
+++++++++
+S      +
+ ++++ +
+ +  + +
+ ++ +M+
+++++++++
```
Esse projeto foi feito para a disciplina de Inteligência Computacional. 🚀

