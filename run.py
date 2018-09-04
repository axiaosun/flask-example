from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    items = ['item one', 'item two', 'item three', 'item four']
    return(render_template("index.html", address="VARIABLE!", items=items))

if __name__ == "__main__":
    app.run("127.0.0.1", debug=True)
