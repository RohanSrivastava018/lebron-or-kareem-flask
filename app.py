from email import message
from flask import Flask, render_template, request
from values import getValues

# to enter environment (lebron-or-kareem)
# run: $ pipenv shell

# to exit environment
# run: $ pipenv exit


app = Flask(__name__)

env = 'prod'
if env == 'dev':
    app.debug = True
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://rujrefyupyfsio:b7d82ccd891d09ed84f67c62f065791f756be93264097e0fd994f431ff286c1f@ec2-44-208-88-195.compute-1.amazonaws.com:5432/dcgb519pqjsoic'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sumbit', methods=['POST'])
def submit():
    if request.method == 'POST':
        player_name = request.form['player-name']
        data = getValues(player_name)
        if data == None:
            return render_template('index.html', message='Please check your spelling!')
        if data['diff'] > 0 :
            return render_template('not-passed.html', data=data)
        return render_template('passed.html', data=data)

if __name__ == '__main__':
    app.run()