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


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        # View
        return render_template('add.html')

    else:
        # request.method = POST
        # add pad to settings
        name = request.form.getlist('name')[0]
        keys = request.form.getlist('keys')[0].split()
        KEY.add_pad(name, *keys)
        return redirect('/')


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'GET':
        # View
        return render_template('index.html', pads=KEY.pads, del_mode=True)

    else:
        # POST
        pad_id = request.form.getlist('pad_id')[0]
        KEY.del_pad(pad_id)
        return redirect('/delete')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8099, debug=True)
