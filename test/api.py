from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/api", methods = ['GET'])
def returnascii():
    d = {}
    input = str(request.args['query'])
    ans = str(ord(input))
    d['output'] = ans
    return d

if __name__ =="__main__":
    app.run()

# print(ord('a'))