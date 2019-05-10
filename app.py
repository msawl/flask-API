from flask import Flask, jsonify
      
app = Flask(__name__)
      
@app.route("/")
def home():
    return jsonify({"home" : "Hello World!"})
	
@app.route("/test_API")
def test_API():
    return jsonify({"home" : "test_API!"})
	
if __name__ == "__main__":
    app.run(debug=True)
