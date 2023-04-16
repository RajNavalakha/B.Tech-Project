#from flask import Flask
#app = Flask(__name__)

#@app.route("/")
#def home():
    #return "Hello, Flask!"

from flask import *
app = Flask(__name__)  
@app.route('/')  
def message():  
      return render_template('web.html') 
if __name__ == '__main__':  
   app.run(debug = True)