from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html',data=[{'name':'open'}, {'name':'close'},{'name':'high'}, {'name':'low'},{'name':'volume'}])

@app.route('/post_stock',methods=['POST'])
def post_stock():
  request.form['stock_ticker']
  request.form.get('type_select')
  return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(port=33507)
