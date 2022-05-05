from flask import *
from flask_recaptcha import ReCaptcha

app = Flask(__name__)
app.config['RECAPTCHA_SITE_KEY'] = '6Lc7ULofAAAAAMloaPomViWK77IsiM-RgzohLD72'
app.config['RECAPTCHA_SECRET_KEY'] = '6Lc7ULofAAAAAIcqko0ahowaGEWDRmfF0G2OK8l-'
recaptcha = ReCaptcha(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = '' 
    if request.method == 'GET':
        return render_template('captcha.html', message=message)
    if request.method == 'POST':
        if recaptcha.verify(): 
            message = 'Captcha verification passed!' 
        else:
            message = 'Please fill out the Captcha!'
        return render_template('captcha.html', message=message)

if __name__ == '__main__':
    app.run()