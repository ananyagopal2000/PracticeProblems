"""
buy_and_sell_stock: While iterating through the array keep searching for the minimum element and check profit by subracting minimum element from prices[i].
Finally return the profit.
buy_and_sell_stock_II: Iterate through he prices array from prices[1], and keep updating profit by by subtracting prices[i-1] from
prices[i] when prices[i] is greater than prices[i-1]. Finally return the profit.
"""
class MaxProfit:
    def __init__(self, prices):
        self.prices=prices
        self.profit1=0
        self.profit2=0
        self.minimum=float('inf')

    def buy_and_sell_stock(self):            
        if len(self.prices)<2:
            return 0
        
        i=0 
        while i<len(self.prices):
            if self.prices[i]<self.minimum:
                self.minimum=self.prices[i]
            if self.prices[i]-self.minimum>self.profit1:
                self.profit1=self.prices[i]-self.minimum
            i+=1
        
        return self.profit1
    
    def buy_and_sell_stocks_II(self):

        if len(self.prices)<2:
            return 0
        
        self.profit2=0
        for i in range(1, len(self.prices)):
            if self.prices[i]>self.prices[i-1]:
                self.profit2+=self.prices[i]-self.prices[i-1]

        return self.profit2

        
        