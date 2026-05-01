class Row:

    def __init__(self):
        self.values = []

    def addCell(self, cell):
        self.values.append(cell)
        return self

    def adjacent(self, index, check=True):
        count = 0
        # left
        if (index > 0) and (index - 1 < len(self.values)):
            if self.values[index - 1] is not 0:
                count += 1
        # center
        if check and (index >= 0) and (index < len(self.values)):
            if self.values[index] is not 0:
                count += 1
        # right
        if index < len(self.values) - 1:
            if self.values[index + 1] is not 0:
                count += 1
        return count


    def string(self):
        return "".join('x' if x == 2 else '@' if x == 1 else '.' for x in self.values)


class Grid:
    def __init__(self):
        self.rows = []

    def addRow(self, row):
        self.rows.append(row)
        return self

    def process(self):
        result = Grid()
        for i in enumerate(self.rows):
            row = self.rows[i]
            newRow = Row();
            for j in enumerate(row.values):
                count = -1
                if (row.values[j] == 1):
                    # current
                    count += row.adjacent(j, False) # add current row
                    # add previous
                    if i > 0:
                        count += self.rows[i - 1].adjacent(j, True)
                    # add next
                    if i < len(self.rows) - 1:
                        count += self.rows[i + 1].adjacent(j, True)

                newRow.addCell('x' if count > 4 else 'o' if count > -1 else '.' )

            result.addRow(newRow)

        return result
