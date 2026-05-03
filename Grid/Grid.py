from Grid.Row import Row
import sys

class Grid:

    def __init__(self):
        self.rows = []

    def add_row(self, row):
        self.rows.append(row)
        return self

    def removed(self):
        count = 0
        for row in self.rows:
            count += row.removed()
        return count

    def process(self):
        result = Grid()
        for i, row in enumerate(self.rows):
            new_row = Row()
            for j, value in enumerate(row.values):
                count = -1
                if value == 1:
                    # current
                    count = row.adjacent(j, False)
                    # add previous
                    if i > 0:
                        count += self.rows[i - 1].adjacent(j, True)
                    # add next
                    if i < len(self.rows) - 1:
                        count += self.rows[i + 1].adjacent(j, True)

                new_cell = 0 if count < 0 else 2 if count < 4 else 1
                new_row.add_cell(new_cell)

            result.add_row(new_row)

        return result
