from flask import Flask, request
app = Flask(__name__)

@app.route('/cgi/sum', methods=['POST', 'GET'])
def sum():
  a=request.args.get("a",0)
  b=request.args.get("b",0)
  return(str(int(a)+int(b)))

app.run(debug=True, port=5000)
