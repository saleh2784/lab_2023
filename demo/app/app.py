from flask import Flask, render_template
import os

app = Flask(__name__)

host = os.getenv('HOSTNAME')
var = os.getenv('MYVAR')
secret = os.getenv('MYSECRET')
env = os.getenv('env')

@app.route('/')
def index():
    return render_template('index.html', host=host, var=var, secret=secret, env=env)

if __name__ == '__main__':
    app.run(host='0.0.0.0')