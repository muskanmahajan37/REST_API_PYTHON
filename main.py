
from flask import Flask ,jsonify

# Flask constructor takes the name of  
# current module (__name__) as argument. 
app = Flask(__name__) 
  

@app.route('/') 
# ‘/’ URL is bound with hello_world() function. 
def hello_world(): 
    return 'Hello World'

@app.route('/sub/<int:a>/<int:b>/')
def sub(a,b):
    if (a > 0 and b>0):
        result_1 = a-b
        result = {
            "first number":a,
            "second number":b,
            "subtraction of them is " : result_1
        }
        return jsonify(result)
    else:
        return jsonify("Cant subtract")

@app.route('/sum/<int:c>/<int:d>/')
def sum(c,d):
    if (c > 0 and d > 0):
        result_2 = c+d
        result_na = {
            "first number":c,
            "second number":d,
            "sum of them is " : result_2,
            "dumb": [1,2,3,4]
        }
        return jsonify(result_na)
    else:
        return jsonify("whats the use of adding")
# main driver function 
if __name__ == '__main__': 

    app.run(debug=True) 