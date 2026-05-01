import sys

from Grid.Grid import *

def main():

    grid = Grid()
    # read into grid
    for line in sys.stdin:
        row = Row()
        for cell in line.strip():
            cell_value = 1 if cell == '@' else 0
            row.addCell(cell_value)

        grid.addRow(row)

    # calculate removals
    result = grid.process()
    for row in result:
         print(row.string())
