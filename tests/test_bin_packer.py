import unittest

from project_planner.bin_packer import BinPacker


class TestBinPacker(unittest.TestCase):
    def test_pack_item_does_not_fit(self):
        p = BinPacker[int](10)
        with self.assertRaises(ValueError):
            p.pack([12])

    def test_pack_item_does_fit(self):
        p = BinPacker[int](10)
        packed = p.pack([8])
        self.assertEqual(len(packed), 1)

    def test_pack_item_fits_exactly_without_padding(self):
        p = BinPacker[int](10)
        packed = p.pack([10])
        self.assertEqual(len(packed), 1)

    def test_pack_item_fits_exactly_with_padding(self):
        p = BinPacker[int](10, padding=1)
        packed = p.pack([10])
        self.assertEqual(len(packed), 1)

    def test_items_with_padding(self):
        p = BinPacker[int](10, padding=1)
        packed = p.pack([5, 5])
        self.assertEqual(len(packed), 2)
        packed = p.pack([6, 3])
        self.assertEqual(len(packed), 1)
