class Cell:
    def __init__(self, index, cells: list):
        self.index = index
        self.lines = []
        self.value = cells[index]
        self.weight = 1


class Line:
    def __init__(self, cells: list, indices: tuple):
        self.indices = indices
        self.line = (cells[self.indices[0]], cells[self.indices[1]], cells[self.indices[2]])
        self.win = self.line.count('A') == 2 and self.line.count(' ') == 1
        self.danger = self.line.count('X') == 2 and self.line.count(' ') == 1
        self.onex = 'X' in self.line and self.line.count(' ') == 2
        self.one = 'A' in self.line and self.line.count(' ') == 2


class Grid:
    def __init__(self, cells: list):
        self.space = cells.count(' ') - 1
        self.matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
        self.lines = [Line(cells, tpl) for tpl in self.matrix]
        self.g_cells = [Cell(i, cells) for i in range(1, 10)]
        for cell in self.g_cells:
            for line in self.lines:
                if cell.index in line.indices:
                    cell.lines.append(line)


class AI(Grid):
    def __init__(self, cells: list):
        super().__init__(cells)
        self.hard = False

    def check(self):
        if self.hard:
            case = ('X', 'A', 'X')
            special = (self.lines[6].line == case) or (self.lines[7].line == case)
            if self.space == 6 and special:
                for i in range(1, 8, 2):
                    self.g_cells[i].weight += 500

        for cell in self.g_cells:
            if cell.value != ' ':
                cell.weight = 0
                continue

            cell.weight += len(cell.lines)
            for line in cell.lines:
                if line.win:
                    cell.weight += 999999
                if line.danger:
                    cell.weight += 99999

                if self.hard:
                    if line.one:
                        cell.weight += 100
                    if line.onex:
                        cell.weight += 80
