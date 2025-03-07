import turtle

# Definição dos símbolos do labirinto
PART_OF_PATH = 'O'  # Caminho correto
TRIED = '.'          # Tentativa
OBSTACLE = '+'       # Parede
DEAD_END = '-'       # Caminho sem saída
FINISH = 'M'         # Destino

class Maze:
    def __init__(self, mazeFileName):
        """Inicializa o labirinto a partir de um arquivo."""
        self.mazelist = []
        with open(mazeFileName, 'r') as mazeFile:
            for row, line in enumerate(mazeFile):
                rowList = list(line.strip())  # Converte a linha em uma lista
                if 'S' in rowList:
                    self.startRow = row
                    self.startCol = rowList.index('S')
                self.mazelist.append(rowList)
        
        self.rowsInMaze = len(self.mazelist)
        self.columnsInMaze = len(self.mazelist[0])
        self.xTranslate = -self.columnsInMaze / 2
        self.yTranslate = self.rowsInMaze / 2
        
        self.t = turtle.Turtle()
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-(self.columnsInMaze-1)/2-.5, 
                                     -(self.rowsInMaze-1)/2-.5, 
                                     (self.columnsInMaze-1)/2+.5, 
                                     (self.rowsInMaze-1)/2+.5)

    def drawMaze(self):
        """Desenha o labirinto na tela."""
        self.t.speed(0)
        self.wn.tracer(0)
        for y, row in enumerate(self.mazelist):
            for x, cell in enumerate(row):
                if cell == OBSTACLE:
                    self.drawCenteredBox(x, y, 'black')
                elif cell == FINISH:
                    self.drawCenteredBox(x, y, 'red')
        self.wn.update()
        self.wn.tracer(1)

    def drawCenteredBox(self, x, y, color):
        """Desenha um quadrado preenchido na posição especificada."""
        self.t.up()
        self.t.goto(x + self.xTranslate - 0.5, -y + self.yTranslate - 0.5)
        self.t.down()
        self.t.fillcolor(color)
        self.t.begin_fill()
        for _ in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def updatePosition(self, row, col, val=None):
        """Atualiza a posição do cursor e marca o caminho."""
        if val:
            self.mazelist[row][col] = val
        self.t.up()
        self.t.goto(col + self.xTranslate, -row + self.yTranslate)
        self.t.down()
        
        colors = {PART_OF_PATH: 'green', TRIED: 'black', DEAD_END: 'red'}
        if val in colors:
            self.t.dot(10, colors[val])

    def isExit(self, row, col):
        """Verifica se a posição atual é uma saída."""
        return row in {0, self.rowsInMaze-1} or col in {0, self.columnsInMaze-1}
    
    def __getitem__(self, idx):
        return self.mazelist[idx]


def searchFrom(maze, row, col):
    """Busca recursivamente um caminho no labirinto."""
    maze.updatePosition(row, col)
    
    if maze[row][col] in {OBSTACLE, TRIED, DEAD_END}:
        return False
    
    if maze[row][col] == FINISH:
        maze.updatePosition(row, col, PART_OF_PATH)
        return True
    
    maze.updatePosition(row, col, TRIED)
    
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if searchFrom(maze, row + dr, col + dc):
            maze.updatePosition(row, col, PART_OF_PATH)
            return True
    
    maze.updatePosition(row, col, DEAD_END)
    return False

# Executando a busca no labirinto
myMaze = Maze('maze.txt')
myMaze.drawMaze()
searchFrom(myMaze, myMaze.startRow, myMaze.startCol)
