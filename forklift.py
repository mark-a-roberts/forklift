#!/usr/bin/python3

import sys

from Grid.Grid import Grid
from Grid.Row import Row



def main():

    grid = Grid()
    # read into grid
    for line in sys.stdin:
        row = Row()
        for cell in line.strip():
            cell_value = 1 if cell == '@' else 0
            row.add_cell(cell_value)

        grid.add_row(row)

    # calculate removals
    result = grid.process()
    for row in result.rows:
         print(row.string())

    print("Removed stacks:" + str(result.removed()))

main()
