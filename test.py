from Average import Average
from Yahoo import Yahoo
import unittest
import numpy
import pandas


class Testing(unittest.TestCase):
    def test_company_name(self):
        y_mast = Yahoo()
        result = y_mast.company_name("AAPL")
        expectation = "Apple Inc."
        self.assertEqual(result, expectation)

    def test_price(self):
        y_mast = Yahoo()
        result = y_mast.price("AAPL")
        expectation = numpy.float64
        self.assertIsInstance(result, expectation)

    def test_ticker_days(self):
        y_mast = Yahoo()
        result = y_mast.t_data("AAPL")
        expectation = pandas.core.frame.DataFrame
        self.assertIsInstance(result, expectation)

    def test_get_stats(self):
        y_mast = Yahoo()
        result = y_mast.get_stats("AAPL")
        expectation = pandas.core.frame.DataFrame
        self.assertIsInstance(result, expectation)

    def test_average(self):
        av_mast = Average()
        y_mast = Yahoo()
        result = av_mast.ticker_average(y_mast.t_data("AAPL"))
        expectation = numpy.float64
        self.assertIsInstance(result, expectation)
