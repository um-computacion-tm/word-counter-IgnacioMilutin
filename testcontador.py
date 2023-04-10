import unittest
from count_words import count_words
class TestCountLetters(unittest.TestCase):

    def test_simple(self):
        result = count_words('hola')
        self.assertEqual(result, {'hola': 1})
    def test2(self):
        result = count_words('hola como hola estas')
        self.assertEqual(
            result,
            {
                'hola':2,
                'como':1,
                'hola':2,
                'estas':1
            }
        )

if __name__ == '__main__':
    unittest.main()