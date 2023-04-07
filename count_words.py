import unittest

def count_words(word):
    wordlist = word.split()
    wordq={}
    for i in wordlist:
        if i in wordq:
            wordq[i]+=1
        else: 
            wordq[i]=1
    return wordq



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