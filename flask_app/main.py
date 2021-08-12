from flask import Flask, request, make_response, render_template, redirect, url_for, jsonify, session
from adapter2 import call_adapter, sentence_adapter, saveFile, find_file, save_temp, hard_adapter
from UI_model import show_info
# from flask_wtf import FlaskForm
# from wtforms import StringField
# from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
import mimetypes, os

mimetypes.add_type('application/javascript', '.js')
app = Flask(__name__)
app.config['DB_FOLDER'] = '/database'
app.config['TEXT_FOLDER'] = '/text'
app.config['TEMP_FOLDER'] = '/temp'
app.config['SECRET_KEY'] = 'bdaf4rsfdfdsf4wsdc4w445tyry6552we'

serverURL = os.getcwd()

names = {
        "id1": {"name": "Truemansi", "password": "jomashotpa1956"},
         }
registered = []


@app.route('/')
def index():
    print(session)
    if len(session) == 0:
        return redirect(url_for('login'))
    else:
        return render_template('index.html')


# @app.route('/get_text')
# def get_text():
#     #print("LOL0")
#     print(registered[0])
#     dirlist = show_texts(session['username'], serverURL)
#     #print("LOL3", dirlist)
#     resp = make_response({"response": dirlist})
#     #print(resp)
#     return resp

@app.route('/get_name')
def get_name():
    return make_response({"name: ": session['username']})

@app.route('/get_info')
def get_info():
    dirlist = show_info(session['username'], serverURL)
    resp = make_response({"response": dirlist})
    return resp

@app.route('/kill_session')
def kill_session():
    session.pop('username', None)
    return jsonify({"redirect": "/"})

@app.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/auth', methods = ['GET', 'POST'])
def auth():
    data = request.get_json("name")
    for name in names:
        print(names[name]["name"], ' ', data)
        if data['name'] == names[name]["name"] and data['password'] == names[name]['password']:
            session['username'] = names[name]["name"]
        else:
            print("no!")
    if len(session) == 0:
        resp = make_response({"Error": "Тамле хōтпа ат хōнтавес!"})
        return resp
    else:
        return jsonify({"redirect": "/"})


@app.route('/parse', methods=['GET', 'POST'])
def parse():
    mode = request.get_json("mode")
    print(mode)
    print(mode["parse_mode"])
    # filename = "C:/Users/Пользователь/MorphParser/flask_app/texts/40/40_1.txt"
    # mode = 'nodiacritics'
    parsed = call_adapter(mode["text"], mode["parse_mode"])
    resp = make_response(parsed)
    print("parsed ", parsed)
    resp.headers['Content-Type'] = "application/json"
    return resp

@app.route('/sentence', methods = ['GET', 'POST'])
def sentence():
    # { 0: [ "word" : "ma" ], 1: [ "word" : "pu"] }
    word = request.get_json("word")
    words_to_parse = []
    print(type(word))
    print(word)
    print(range(len(word)))
    for i in range(len(word)):
        print(word[str(i)])
        words_to_parse.append(word[str(i)])
    print("qq", words_to_parse)
    string_to_parse = " ".join(words_to_parse)
    parsed = sentence_adapter(string_to_parse)
    resp = make_response(parsed)
    resp.headers['Content-Type'] = "application/json"
    return resp

@app.route('/saver', methods = ['GET', 'POST'])
def saver():
    file = request.get_json("word")
    result = saveFile(file)
    resp = make_response({"success": result})
    resp.headers['Content-Type'] = "application/json"
    return resp

@app.route('/get_file', methods = ['GET', 'POST'])
def get_file():
    file = request.get_json("link")
    print(file)
    file = find_file(file, session['username'])
    resp = make_response(file)
    resp.headers['Content-Type'] = "application/html"
    return resp

@app.route('/create_temp', methods = ['GET', 'POST'])
def create_temp():
    file = request.get_json("link")
    print(file)
    response = save_temp(file)
    resp = make_response({"response": response})
    resp.headers['Content-Type'] = "application/json"
    return resp

@app.route('/reparse_hard', methods = ['GET', 'POST'])
def reparse_hard():
    num = request.get_json("link")
    print(num)
    response = hard_adapter(num)
    print(response)
    resp = make_response(response)
    resp.headers['Content-Type'] = "application/json"
    return resp

@app.route('/upload_text', methods = ['GET', 'POST'])
def upload_text():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config["DB_FOLDER"]+session['username']+app.config["TEXT_FOLDER"], filename))
    return jsonify({"redirect": "/"})

if __name__ == "__main__":
    app.run(debug=True)
