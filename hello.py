from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
  app.debug = True
  app.run('localhost',8001)

  #  app.run(host, port, debug, options)