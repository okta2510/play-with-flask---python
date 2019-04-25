from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html',name="oktaviardi")

@app.route('/cek/<int:score>')
def cek(score):
   return render_template('index.html',marks=score)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success post for',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success get for',name = user))

if __name__ == '__main__':
  app.debug = True
  app.run('localhost',8001)

  #  app.run(host, port, debug, options)