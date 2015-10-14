from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route('/')
def index():
  return "kjhgvjhfghjdghfjhfhjg"

@app.route('/user/<username>')
def profile(username):
  return "Hello " + username + "\n"

@app.route('/post/<post>')
def post(post):
  return "Post "+ post

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


