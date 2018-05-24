import flask

app = flask.Flask(__name__)


@app.route("/")
def homepage():
    return "Hello world!222ww"






if __name__ == '__main__':
    app.run(debug=True)
