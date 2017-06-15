from flask import Flask, render_template, request, redirect, url_for
from .stock_plot import stockPlot

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html',data=[{'name':'open'}, {'name':'close'},{'name':'high'}, {'name':'low'},{'name':'volume'}])


@app.route('/post_stock',methods=['POST'])
def post_stock():
  found_or_not=stockPlot(request.form['stock_ticker'], request.form.get('type_select'))
  if found_or_not:
    return render_template('stocks.html')
  else:
    return render_template('errorpage.html')

if __name__ == '__main__':
  app.run(port=33507)
