from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/todo')
def todo():
    return render_template('todo.html')

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template('register.html')

    if request.method == "POST":
        return render_template("register.html")
if __name__ == "__main__":
    app.run(debug=True)
