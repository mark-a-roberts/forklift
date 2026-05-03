from Grid.Row import Row

# test empty row
def test_row_none():
    row = Row()
    assert len(row.values) == 0
    assert row.adjacent(0, False) == 0
    assert row.adjacent(1, False) == 0

# test row with one cell
def test_row_one():
    row = Row()
    row.add_cell(1)
    assert len(row.values) == 1
    assert row.adjacent(0, False) == 0
    assert row.adjacent(1, False) == 1

    assert row.string() == "@"

# test row with two cells
def test_row_two():
    row = Row([1,0])
    assert len(row.values) == 2
    assert row.adjacent(0, False) == 0
    assert row.adjacent(1, False) == 1

    assert row.string() == "@."

def test_row():
    row = Row([1,0,1, 1])
    assert len(row.values) == 4
    assert row.adjacent(0, False) == 0
    assert row.adjacent(1, False) == 2
    # check false/true
    assert row.adjacent( 2, False) == 1
    assert row.adjacent(2, True) == 2

    assert row.string() == "@.@@"
