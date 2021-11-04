
class Asset:
    '''
    Parent Class Asset
    '''
    
    def __init__(self, price, marketcap):
        '''
        Attributes
        ----------
        price
        marketcap
        '''

        self.price = price
        self.marketcap = marketcap
        

class Stock(Asset):
    '''
    Inheritance Class Stock
    '''
    
    def __init__(self, price, marketcap, isin, amount):
        '''
        Attributes
        ----------
        price : price of one share
        marketcap :marketcap of the company
        isin : Isin number of the stock
        amount : Number of Stocks in Portfolio

        '''
        
        Asset.__init__(self, price, marketcap)
        self.isin = isin
        self.amount = amount
        
    def stocksplit(self, splitfactor):
        '''
        Changes Stock amount and Stock price according to splitfactor
        
        arguments: splitfactor
        return: None
        '''
        
        self.amount = self.amount * splitfactor
        self.price = self.price/ splitfactor
        
    
        
class Gold(Asset):
    '''
    Inheritance Class Gold
    '''
    
    def __init__(self, price, marketcap, quality, amount):
        '''
        Attributes
        ----------
        price : price for one ounce
        marketcap :marketcap of Gold
        quality : Quality label of the Gold
        amount : Number of ounces
        '''
        Asset.__init__(self, price, marketcap)
        self.quality = quality
        self.amount = amount
                