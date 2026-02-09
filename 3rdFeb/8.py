from flask import Flask, request, render_template, redirect, url_for, flash
app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return 'This is the Index Page. <a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error=None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.secret_key = 'supersecretkey'
    app.run(debug=True)