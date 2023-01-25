import unittest

from translator import english_french, french_english

class TestenglishToFrench_null(unittest.TestCase):
    def test1(self):
        #self.assertEqual(english_french("Hello"),"Bonjour")
        self.assertEqual(english_french(""),"")
      
class TestenglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_french("Hello"),"Bonjour")
        #self.assertEqual(english_french(""),"")

class TestfrenchToEnglish_null(unittest.TestCase):
    def test1(self):
        #self.assertEqual(french_english("Bonjour"),"Hello")
        self.assertEqual(french_english(""),"")        


class TestfrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_english("Bonjour"),"Hello")
        #self.assertEqual(french_english(""),"")
        

unittest.main()