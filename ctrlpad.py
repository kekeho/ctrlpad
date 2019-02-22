from flask import Flask, render_template
import libctrlpad
app = Flask(__name__, static_folder='./templates/assets',
            template_folder='./templates/')
KEY = libctrlpad.Key()


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
