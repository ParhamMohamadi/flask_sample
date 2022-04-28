# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
import pandas as pd
# create the application object
app = Flask(__name__)


# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin' or request.form[
                'vehicle'] != 'Yes':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route("/table-page", methods=['GET'])
def table():
    data_dic = {
        'name': [100, 101, 102],
        'age': ['red', 'blue', "https://www.w3schools.com/"]}
    columns = ['name', 'age']
    index = ['a', 'b', 'c']

    df = pd.DataFrame(data_dic, columns=columns, index=index)

    def fun(path):
        f_url = 'test'
        # convert the path into clickable link
        return '<a href="{}">{}</a>'.format(path, f_url)

    df = df.style.format({'age': fun})

    table = df.to_html(render_links=True, index=False)

    return render_template(
        "at-leaderboard.html",
        table=table
    )

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
