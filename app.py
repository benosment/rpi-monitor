from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now()
    time_string = now.strftime("%m-%d-%Y %H:%M:%S")
    template_data = {'title': 'HELLO!',
                     'time': time_string}
    return render_template('main.html', **template_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)