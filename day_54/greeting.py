from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return  ('<h1 style="text-align: center">Goto /name/enter your name/ enter your age</h1>'
             '<p>This is a paragraph</p>'
             '<iframe src="https://giphy.com/embed/sTczweWUTxLqg" width="480" height="346" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/happy-friday-sTczweWUTxLqg"></a></p>')

def make_it_bold(function):
    def bold_wraper():
        return "<b>" + function() + "</b>"
    return bold_wraper

def make_it_emphasis(function):
    def emphasis_wrapper():
        return "<em>" + function()+ "</em>"
    return emphasis_wrapper

def make_it_underlined(function):
    def underlined():
        return "<u>" + function() + "</u>"
    return underlined


@app.route("/bye")
@make_it_bold
@make_it_emphasis
@make_it_underlined
def bye():
    return  "Bye!"
@app.route("/name/<name>/<int:age>")
def greeting(name, age):
    return f"<h1> how are you {name}? you are{age} </h1>"

if __name__ == "__main__":
    app.run(debug=True)