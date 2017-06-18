from flask import Flask, render_template, request, redirect, url_for
from stock_plot import stockPlot

app = Flask(__name__)
#app.debug=True
@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html',data=[{'name':'open'}, {'name':'close'},{'name':'high'}, {'name':'low'},{'name':'volume'}],adj=[{'name':'default'},{'name':'adjusted'}])


@app.route('/post_stock',methods=['POST'])
def post_stock():
  ticker=str(request.form['search'])
  price=str(request.form.get('type_select'))
  adjust_or_not=str(request.form.get('adj_select'))
  if adjust_or_not=='default':
    found_or_not=stockPlot(ticker,price)
  else:
    found_or_not=stockPlot(ticker,'adj_'+price)
  if found_or_not:
    return render_template('stocks.html')
  else:
    return render_template('errorpage.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0')

