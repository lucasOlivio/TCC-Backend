from shares import Shares
from pandas.tseries.offsets import BDay
import datetime

if __name__ == "__main__":
    today = datetime.datetime.now()
    week_ago = (today - BDay(7)).date()
    month_ago = (today - datetime.timedelta(days=31)).date()
    year_ago = (today - datetime.timedelta(days=365)).date()

    share = Shares('AAPL')

    stockClose_week = share.getClosing([week_ago, today])
    stockClose_month = share.getClosing([month_ago, today])
    stockClose_year = share.getClosing([year_ago, today])

    resp = True
    data = [
        stockClose_week,
        stockClose_month,
        stockClose_year,
    ]

    print(data)