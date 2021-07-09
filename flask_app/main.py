from flask import Flask, request, make_response, render_template, redirect, url_for, jsonify
from adapter2 import call_adapter, sentence_adapter, saveFile, find_file, save_temp, hard_adapter
import mimetypes

mimetypes.add_type('application/javascript', '.js')
app = Flask(__name__)

names = {
        "id1": {"name": "Vasiliy", "password": "vang"},
        "id2": {"name": "Kyrshka", "password": "selkup"},
        "id3": {"name": "Daria", "password": "horaming"},
         }
registered = []

@app.route('/')
def index():
    print(registered)
    if len(registered) == 0:
        return redirect(url_for('login'))
    else:
        return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/auth', methods = ['GET', 'POST'])
def auth():
    data = request.get_json("name")
    for name in names:
        print(names[name]["name"], ' ', data)
        if data['name'] == names[name]["name"] and data['password'] == names[name]['password']:
            registered.append(names[name]["name"])
            registered.append(names[name]['password'])
        else:
            print("no!")
    if len(registered) == 0:
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
    file = find_file(file)
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

if __name__ == "__main__":
    app.run(debug=True)
