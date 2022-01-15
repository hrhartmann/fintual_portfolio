from datetime import date
# date format: yyyy-mm-dd

YEAR_DAYS = 365
BASE_STOCKS_AMOUNT = 1


class Stock:
    '''
    This class is a stock that has a dictionary of values in 
    a range of dates, keys are dates, values are the stock price for 
    the given date
    '''

    def __init__(self, 
                 name: str, 
                 values: dict, 
                 amount: float=BASE_STOCKS_AMOUNT):
        self.name = name
        self.values = values
        self.amount = amount

    def price(self, ddate: date):
        '''returns price of stock for given date'''

        return self.values[str(ddate)]

    def value(self, ddate: date):
        '''This function returns the value of a Stock'''

        return self.amount * self.price(ddate)

    def __str__(self):
        return "{}: {} share(s)".format(self.name, self.amount)


class Portfolio:
    '''
    This class has a list of Stocks
    '''

    def __init__(self, stocks: list):
        self.stocks = stocks

    def profit(self, init_date: date, end_date: date):
        '''
        Returns stocks profit between 
        given dates and annualized return
        '''
        
        stocks_profit = 0
        for stock in self.stocks:
            # We add each stock profit
            stocks_profit += self.get_stock_profit(stock, init_date, end_date) 
        # Annualized return with year = YEAR_DAYS days (365)
        annualized_return = stocks_profit * YEAR_DAYS / (end_date - init_date).days
        return stocks_profit, annualized_return

    def get_stock_profit(self, stock: Stock, init_date: date, end_date: date):
        '''return profit of stock for given dates'''

        return stock.value(end_date) - stock.value(init_date)



        

    



