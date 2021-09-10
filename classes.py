# Classes

class Asset:
    '''
    Parent Asset Class
    '''
    
    def __init__(self, price=0, marketcap=0):
        '''
        
        Parameters
        ----------
        price : TYPE
            DESCRIPTION.
        marketcap : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''

        self.price = price
        self.marketcap = marketcap
        

class Stock(Asset):
    '''
    Inheritance Class Stock
    '''
    
    def __init__(self, price, marketcap):
        '''
        

        Parameters
        ----------
        price : TYPE
            DESCRIPTION.
        marketcap : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        
        Asset.__init__(self, price, marketcap)