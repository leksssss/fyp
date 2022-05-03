from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("captcha.html")

@app.route('/verify', methods=["GET", "POST"])
def verify():
    return "success"
    #return redirect(url_for("index"))

if __name__ == '__main__':
    app.run()