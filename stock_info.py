# Stock 클래스는 key value로 회사명 과 심볼의 구조를 가지는 클래스이다. yfinance 를 이용함
import yfinance as yf
import pandas as pd
class Stock:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.ticker = yf.Ticker(symbol)
    
    def get_basic_info(self):
        """Return basic information about the stock."""
        basic_info = pd.DataFrame.from_dict(self.ticker.info, orient='index', columns=['Value'])
        return basic_info.loc[['longName', 'industry', 'sector', 'marketCap', 'sharesOutstanding']].to_markdown()
    
    def get_financials_statements(self):
        """Return financial statements of the stock."""
        financials = {
            'Income Statement': self.ticker.financials,
            'Balance Sheet': self.ticker.balance_sheet,
            'Cash Flow': self.ticker.cashflow
        }
        return {key: df.to_markdown() for key, df in financials.items()}

# Example usage:  main
if __name__ == "__main__":
    stock = Stock('005930.KS') 
    print(stock.get_basic_info())
    print(stock.get_financials_statements())


    