import unittest
from filecmp import cmp


class TestCmpMethod(unittest.TestCase):

    def test_true_short(self):
        self.assertTrue(cmp('secrets.txt', 'same_secrets.txt'))

    def test_false_short(self):
        self.assertFalse(cmp('secrets.txt', 'no_secrets.txt'))

    def test_true_long(self):
        self.assertTrue(cmp('secrets_long.txt', 'same_secrets_long.txt'))

    def test_false_long(self):
        self.assertFalse(cmp('secrets_long.txt', 'no_secrets_long.txt'))

    def test_shallow_false(self):
        self.assertTrue(cmp('secrets.txt', 'same_secrets.txt', shallow=False))

    def test_no_file(self):
        with self.assertRaises(OSError):
            cmp('no_file.txt', 'secrets.txt')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            cmp(0, 'no_secrets.txt')

    def test_invalid_args(self):
        with self.assertRaises(TypeError):
            cmp('no_secrets.txt', 'secrets.txt', 5, 55)

if __name__ == '__main__':
    unittest.main()