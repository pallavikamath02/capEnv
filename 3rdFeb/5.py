from flask import Flask
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Hello Admin!'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello, %s as Guest!' % guest

if __name__ == '__main__':
    app.run(debug=True)