import requests
import pandas as pd
import os
from bokeh.plotting import figure, output_file, save


def data_access(ticker, price_type):
    r=requests.get('https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json?ticker='+ticker+'&qopts.columns=date,'+price_type+'&api_key=ZqRzFiv9b9xtTx-Qs5xA')
    rj=r.json()
    data=rj['datatable']['data']
    if len(data)>0:
        df=pd.DataFrame(data,columns=['date',price_type])
        df['date'] = pd.to_datetime(df['date'])
        return df
    else:
        return False
    
def interactive_plot(df, ticker):
    p1 = figure(x_axis_type="datetime", title="Stock Data for "+ticker+" from QUANDLE WIKI Set")
    p1.grid.grid_line_alpha=0.3
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = df.columns[1]
    p1.line(df.ix[:,0], df.ix[:,1])
    output_file("./templates/stocks.html", title="Time Series Data for Stock "+ticker)
    save(p1)

def stockPlot(ticker_code, plot_type):    
    stock_data=data_access(ticker_code,plot_type)
    if not isinstance(stock_data, bool):
        interactive_plot(stock_data, ticker_code)
        return True
    else:
        return False
