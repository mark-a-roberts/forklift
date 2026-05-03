class Row:

    def __init__(self, values= None):
        if values is None:
            values = []
        self.values = values

    def add_cell(self, cell):
        self.values.append(cell)
        return self

    def adjacent(self, index, check=True):
        count = 0
        test = [index - 1 , index, index + 1 ] if check else [ index - 1, index + 1]
        # left
        for x in test:
            if (x >= 0) and (x < len(self.values)):
                if self.values[x] != 0:
                    count += 1

        return count

    def removed(self):
        return self.values.count(2)

    def string(self):
        return "".join('x' if x == 2 else '@' if x == 1 else '.' for x in self.values)
