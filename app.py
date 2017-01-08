from flask import Flask, render_template
import datetime
import subprocess
app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now()
    time_string = now.strftime("%m-%d-%Y %H:%M:%S")
    all_processes = subprocess.check_output("ps -ef".split()).splitlines()
    pycomic_process = 'not found'
    uv_process = 'not found'
    for process in all_processes:
        if 'comic.py' in str(process):
            print(process)
            pycomic_process = process.decode('utf-8')
    if 'uv-code.py' in str(process):
            print(process)
            uv_process = process.decode('utf-8')
    template_data = {'title': 'HELLO!',
                     'time': time_string,
                     'pycomic_process': pycomic_process,
                     'uv_process': uv_process}
    return render_template('main.html', **template_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)