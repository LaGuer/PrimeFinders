import unittest

import primefinders


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(primefinders.fermat(1697), ":)")


if __name__ == '__main__':
    unittest.main()
