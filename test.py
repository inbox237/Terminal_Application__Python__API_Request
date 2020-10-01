from Average import Average
from Yahoo import Yahoo
from Color import Color
import unittest

class Testing(unittest.TestCase):
    def test_company_name(self):
        yahoo_master = Yahoo()
        result = yahoo_master.company_name("AAPL")
        expectation = "Apple Inc."
        
        self.assertEqual(result, expectation)
        
        
        