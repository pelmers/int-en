import unittest
from int2en import int2en

class TestInt2En(unittest.TestCase):
    def test_zeros(self):
        self.assertEqual(int2en(0), "zero")
        self.assertEqual(int2en('0'), "zero")
        self.assertEqual(int2en('1'), "one")
        self.assertEqual(int2en('0001'), "one")
        self.assertEqual(int2en('1.000'), "one")

    def test_simple(self):
        self.assertEqual(int2en('12'), 'twelve')
        self.assertEqual(int2en('-12'), 'negative twelve')

    def test_sci_not(self):
        self.assertEqual(int2en('1e261'), 'one sexoctogintillion')
        self.assertEqual(int2en('1e3705'), 'one milliquattuortrigintaducentillion')
        self.assertEqual(int2en('1.9e3000004'), 'nineteen millinillinillion')
        self.assertEqual(int2en('1e-3'), 'one thousandth')
        self.assertEqual(int2en('1.5e-303'), 'fifteen ten centillionths')
        self.assertEqual(int2en('1.23e1'), 'twelve and three tenths')

    def test_decimals(self):
        self.assertEqual(int2en('1.1'), 'one and one tenth')
        self.assertEqual(int2en('-0067.13'), 'negative sixty-seven and thirteen hundredths')

    def test_negative(self):
        self.assertEqual(int2en('-100'), 'negative one hundred')
        self.assertEqual(int2en('100'), 'one hundred')
        self.assertEqual(int2en('-----1000'), 'negative one thousand')
        self.assertEqual(int2en('----1000'), 'one thousand')

    def test_eval(self):
        self.assertEqual(int2en('(-100+101)**300'), 'one')

if __name__=='__main__':
    unittest.main()
