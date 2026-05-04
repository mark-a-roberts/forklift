from Grid.Grid import Grid
from Grid.Row import Row

def test_grid():
    """
    Unit test for a full grid with uneven rows
    The test builds a grid
    :return:
    """
    row1 = Row([1, 0, 1, 1])
    row2 = Row([1, 0, 1, 1 ])
    row3 = Row([1, 0, 1, 1, 1])
    grid = Grid()
    assert len(grid.rows) == 0

    grid.add_row(row1)
    assert len(grid.rows) == 1

    grid.add_row(row2)
    assert len(grid.rows) == 2

    grid.add_row(row3)
    assert len(grid.rows) == 3

    processed = grid.process()
    assert processed.rows[0].values == [2, 0, 2, 2]
    assert processed.rows[1].values == [2, 0, 1, 1]
    assert processed.rows[2].values == [2, 0, 2, 1, 2]

