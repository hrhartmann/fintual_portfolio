from stock_class import Stock
from datetime import date


def read_stocks_data_file(filename: str):
    '''
    This function read stocks data file
    returns stocks list and valid dates
    '''

    with open(filename, "r") as file:
        first_line = file.readline()
        stock_names = first_line.split(",")[1:]
        stocks = [{} for _ in stock_names]
        valid_dates = []
        for line in file:
            info = line.split(",")
            # ddate = get_date(info[0])
            valid_dates.append(info[0])
            values = info[1:]
            for i in range(len(stock_names)):
                stocks[i][info[0]] = float(values[i])

        stock_class = []
        for s in range(len(stock_names)):
            NewStock = Stock(stock_names[s], stocks[s])
            stock_class.append(NewStock)
        return stock_class, valid_dates
            

def get_date(str_date: str):
    '''This functrion gets the date class for string date'''

    y, m, d = str_date.split("-")
    return date(int(y), int(m), int(d))


if __name__ == "__main__":
    read_stocks_data_file("stocks_data.csv")