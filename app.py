from flask import Flask, render_template
from forms import Registration, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b7318d5b51927a4dc8f7fad696408fc4'

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/login')
def login():

    form = LoginForm()

    return render_template('login.html', form=form)


@app.route('/register')
def register():

    form = Registration()

    return render_template('register.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)