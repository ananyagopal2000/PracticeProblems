import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
                                
import unittest
from buy_and_sell_stocks import MaxProfit

class TestBuyandSellStocks(unittest.TestCase):
    def test_decreasing_prices(self):
        print('hey1')
        prices=[9,7,4,2,1]
        max_profit = MaxProfit(prices)
        self.assertEqual(max_profit.buy_and_sell_stock(), 0)
    
    def test_increasing_prices(self):
        prices=[4,6,7,9,10]
        max_profit = MaxProfit(prices)
        self.assertEqual(max_profit.buy_and_sell_stock(), 6)

    def test_empty(self):
        prices=[]
        max_profit = MaxProfit(prices)
        self.assertEqual(max_profit.buy_and_sell_stock(), 0)

class TestBuyandSellStocks_II(unittest.TestCase):
    def test_decreasing_prices(self):
        print('hey2')
        prices=[9,7,4,2,1]
        max_profit = MaxProfit(prices)
        self.assertEqual(max_profit.buy_and_sell_stocks_II(), 0)
    def test_increasing_prices(self):
        prices=[4,6,7,9,10]
        max_profit = MaxProfit(prices)
        self.assertEqual(max_profit.buy_and_sell_stocks_II(), 6)

    def test_empty(self):
        prices=[]
        max_profit = MaxProfit(prices)
        self.assertEqual(max_profit.buy_and_sell_stocks_II(), 0)

if __name__ == 'main':
    unittest.main()
