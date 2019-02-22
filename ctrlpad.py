from flask import Flask, render_template, request, redirect
import libctrlpad
app = Flask(__name__, static_folder='./templates/assets',
            template_folder='./templates/')
KEY = libctrlpad.Key('pads.json')


@app.route('/', methods=['GET'])
def index():
    pad_count = list(range(len(KEY.pads)))
    return render_template('index.html', pads=KEY.pads, pad_count=pad_count)


@app.route('/tap', methods=['POST'])
def tap():
    pad_id = request.form.getlist('pad_id')[0]
    KEY.tap(pad_id)
    return redirect('/')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
