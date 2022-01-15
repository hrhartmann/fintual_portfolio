from read_data import read_stocks_data_file, get_date
from stock_class import Portfolio

STOCKS_DATA_FILE = "stocks_data.csv"


class Menu:
    '''Menu for this program'''

    def __init__(self, portfolio: Portfolio, valid_dates: list):
        self.portfolio = portfolio
        self.valid_dates = valid_dates

    def manual_dates(self):
        '''Select input manual dates'''

        condition = False
        while not condition:
            print("Date format: yyyy-mm-dd")
            print("First valid date: {}".format(self.valid_dates[0]))
            print("Last valid date: {}".format(self.valid_dates[-1]))
            print()
            init_date = input("Choose initial date: ")
            if init_date in self.valid_dates:
                end_date = input("Choose final date: ")
                if end_date in self.valid_dates:
                    init_date = get_date(init_date)
                    end_date = get_date(end_date)
                    if end_date < init_date:
                        print()
                        print("Final date must be after initial date")
                    else:
                        condition = True
                        return init_date, end_date
            print("Invalid dates")

    def max_min_dates(self):
        '''Select minimun and maximum dates'''

        init_date = get_date(self.valid_dates[0])
        end_date = get_date(self.valid_dates[-1])
        return init_date, end_date

    def show_profit(self):
        '''Show profit of the portfolio'''

        init_date, end_date = self.choose_dates_method()
        pprofit, year_return = self.portfolio.profit(init_date, end_date) 
        print()
        print("Portfolio Profit: {}".format(pprofit))
        print("Portfolio annualized return: {}".format(year_return))

    def choose_dates_method(self):
        '''Choose dates method'''

        self.show_options()
        options = ["1", "2"]
        x = input("Choose the option number: ")
        while x not in options:
            print("Invalid option, try again: ")
            print()
            self.show_options()
            x = input("Choose the option number: ")
        if x == "1":
            return self.manual_dates()
        elif x == "2":
            return self.max_min_dates()

    def show_options(self):
        '''Show dates method options'''

        print("Date options: ")
        print("1. Manually choose")
        print("2. first and last dates")

    def market_options(self):
        '''Show all stocks'''

        print("Which stock do you want to buy? ")
        market_options = []
        for i, stock in enumerate(self.portfolio.stocks):
            print(i, stock.name)
            market_options.append(str(i))
        return market_options

    def buy_stocks(self):
        '''Lets you buy a specific stock'''

        market_options = self.market_options()
        option = input("Choose the stock number: ")
        while option not in market_options:
            print("Wrong stock number, try again: ")
            print()
            self.market_options()
            option = input("Choose the stock number: ")

        amount = input("How many stocks do you want to buy? ")
        try:
            q = float(amount)
            self.portfolio.stocks[int(option)].amount = q
        except ValueError as Err:
            print(Err)

    def run(self):
        '''Menu possible actions'''

        while True:
            print()
            print("Available options: ")
            choose_option = self.available_options()
            possible = ["1", "2", "3"]
            if choose_option not in possible:
                return
            elif choose_option == "1":
                self.show_portfolio()
            elif choose_option == "2":
                self.buy_stocks()
            elif choose_option == "3":
                self.show_profit()

    def show_portfolio(self):
        '''Show portfolio stocks and shares'''

        for stock in self.portfolio.stocks:
            print(stock)

    def available_options(self):
        '''Available options'''
        
        print()
        print("1. Show portfolio")
        print("2. Buy stocks")
        print("3. Show portfolio return")
        print("Other. exit")
        print()
        return input("Choose option number: ")
        

if __name__ == "__main__":
    stocks_list, valid_dates = read_stocks_data_file(STOCKS_DATA_FILE)
    portfolio = Portfolio(stocks_list)
    stocks_menu = Menu(portfolio, valid_dates)
    stocks_menu.run()
    

