from flask import Flask, render_template

app = Flask(__name__, static_folder='Static', static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sessions')
def sessions():
    return render_template('sessions.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)