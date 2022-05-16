import pstats
import unittest

from life import Life, CellList


class TestCellList(unittest.TestCase):
    def test_empty(self):
        c = CellList()
        assert list(c) == []

    def test_set_true(self):
        c = CellList()
        c.set(1, 2, True)
        assert c.has(1, 2)
        assert list(c) == [(1, 2)]
        c.set(500, 600, True)
        assert c.has(1, 2) and c.has(500, 600)
        assert list(c) == [(1, 2), (500, 600)]
        c.set(1, 2, True)  # make sure a cell can be set to True twice
        assert c.has(1, 2) and c.has(500, 600)
        assert list(c) == [(1, 2), (500, 600)]

    def test_set_false(self):
        c = CellList()
        c.set(1, 2, False)
        assert not c.has(1, 2)
        assert list(c) == []
        c.set(1, 2, True)
        c.set(1, 2, False)
        assert not c.has(1, 2)
        assert list(c) == []
        c.set(1, 2, True)
        c.set(3, 2, True)
        c.set(1, 2, False)
        assert not c.has(1, 2)
        assert c.has(3, 2)
        assert list(c) == [(3, 2)]

    # # def test_set_default(self):
    # #     c = CellList()
    # #     c.set(1, 2)
    # #     assert c.has(1, 2)
    # #     assert list(c) == [(1, 2)]
    # #     c.set(1, 2)
    # #     assert not c.has(1, 2)
    # #     assert list(c) == []

class TestLife(unittest.TestCase):
    def test_new(self):
        life = Life()
        assert life.survival == [2, 3]
        assert life.birth == [3]
        assert list(life.living_cells()) == []
        assert life.rules_str() == '23/3'

    # def test_new_custom(self):
    #     life = Life([3, 4], [4, 7, 8])
    #     assert life.survival == [3, 4]
    #     assert life.birth == [4, 7, 8]
    #     assert list(life.living_cells()) == []
    #     assert life.rules_str() == '34/478'


