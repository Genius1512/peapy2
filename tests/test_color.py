import unittest

import peapy2


class TestColor(unittest.TestCase):
    def test_hex(self):
        self.assertEqual(
            str(peapy2.Color("ffffff")),
            "#ffffffff"
        )
        self.assertEqual(
            str(peapy2.Color("#00ffffaf")),
            "#00ffffaf"
        )
        self.assertEqual(
            str(peapy2.Color("#ff")),
            "#ffffffff"
        )
        self.assertEqual(
            str(peapy2.Color("#0f0")),
            "#00ff00ff"
        )

    def test_tuple_3(self):
        self.assertEqual(
            str(peapy2.Color(255, 255, 255)),
            "#ffffffff"
        )
        self.assertEqual(
            str(peapy2.Color(0, 255, 255)),
            "#00ffffff"
        )

    def test_tuple_4(self):
        self.assertEqual(
            str(peapy2.Color(255, 255, 255, 255)),
            "#ffffffff"
        )
        self.assertEqual(
            str(peapy2.Color(0, 255, 255, 255)),
            "#00ffffff"
        )


if __name__ == '__main__':
    unittest.main()
