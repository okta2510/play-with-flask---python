from flask import Flask, redirect, url_for, request, render_template,make_response
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('cookie.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST': user = request.form['nm']
   
   resp = make_response(render_template('setcookie.html'))
   resp.set_cookie('userID', user)
   
   return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return render_template('getcookie.html',name=name)

if __name__ == '__main__':
  app.debug = True
  app.run('localhost',8001)

  #  app.run(host, port, debug, options)