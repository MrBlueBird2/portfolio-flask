from flask import Flask, render_template

app = Flask(__name__)
@app.route('/<string>')
def not_found_error(string):
    return render_template("not-found.html")
    
@app.route('/')
def home_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000, host="localhost")