class Row:

    def __init__(self, values= None):
        """
        initialize the row
        :param values:
        """
        if values is None:
            values = []
        self.values = values

    def add_cell(self, cell):
        """
        Add a cell to the row
        :param cell: int, 0 = empty, 1 = current, 2 = accessible
        :return:
        """
        self.values.append(cell)
        return self

    def adjacent(self, index, check=True):
        """
        Determine the number of adjacent cells that are not empty
        :param index: the index of the cell on the row
        :param check: boolean, if true, check including the current cell
        :return:
        """
        count = 0
        test = [index - 1 , index, index + 1 ] if check else [ index - 1, index + 1]
        # left
        for x in test:
            if (x >= 0) and (x < len(self.values)):
                if self.values[x] != 0:
                    count += 1

        return count

    def removed(self):
        """
        Determine the number of cells that can be removed in this row
        :return: int
        """
        return self.values.count(2)

    def string(self):
        """
        return a string representation of the row
        :return: string
        """
        return "".join('x' if x == 2 else '@' if x == 1 else '.' for x in self.values)
