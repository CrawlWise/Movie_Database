from flask import Flask, render_template

app = Flask(__name__)

def movieapi():
    pass

@app.route('/')
def home():
    return render_template('home.html', data="im here")

if __name__ == '__main__':
    app.run(debug=True)
