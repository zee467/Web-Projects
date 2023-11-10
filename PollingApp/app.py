from flask import Flask, render_template

# application instance that receives client requests
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")