from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Home():
    text = 'Hello'
    return render_template('Home.html', title = text)

if __name__ == '__main__':
    app.run(debug=False, port=8555)