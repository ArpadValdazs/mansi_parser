from flask import Flask, request, make_response, render_template
from adapter2 import call_adapter, sentence_adapter, saveFile, find_file, save_temp, hard_adapter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parse', methods = ['GET', 'POST'])
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
    saveFile(file)
    resp = make_response({"success": "successed"})
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
    save_temp(file)
    resp = make_response({"response": "Файл добавлен!"})
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
