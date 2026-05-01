from Grid.Grid import *

def test_row():
    row = Row()
    assert not row.values

    row.addCell(1)
    assert row.values.length == 1
    assert row.adjacent(1) == 0

    row.addCell(0)
    assert row.values.length == 2
    assert  row.adjacent(0) == 1
    assert  row.adjacent(1) == 0

    string = row.string()
    assert string == "@."

def test_forklift():
    pass

