from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = 'Hello, Flask!'
    message = 'This is a dynamic content example using Flask and Jinja2.'
    return render_template('index.html', greeting=greeting, message=message)

if __name__ == '__main__':
    app.run(debug=True)
