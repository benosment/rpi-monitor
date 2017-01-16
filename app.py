from flask import Flask, render_template
import datetime
import subprocess
app = Flask(__name__)

COMIC_QUERY_FILENAME = '../pycomic/pycomic/query.txt'

@app.route("/")
def main():
    now = datetime.datetime.now()
    time_string = now.strftime("%m-%d-%Y %H:%M:%S")
    all_processes = subprocess.check_output("ps -ef".split()).splitlines()
    pycomic_process = 'not found'
    uv_process = 'not found'
    for process in all_processes:
        if 'comic.py' in str(process):
            pycomic_process = process.decode('utf-8')
    if 'uv-code.py' in str(process):
            uv_process = process.decode('utf-8')
    hostname = subprocess.check_output('hostname').decode('utf-8')
    title_string = 'Monitoring %s' % hostname
    uptime = subprocess.check_output('uptime').decode('utf-8')
    template_data = {'title': title_string,
                     'uptime': uptime,
                     'time': time_string,
                     'pycomic_process': pycomic_process,
                     'uv_process': uv_process}
    return render_template('main.html', **template_data)


@app.route('/pycomic')
def pycomic():
    query_terms = []
    with open(COMIC_QUERY_FILENAME) as f:
        for line in f.readlines():
            if not line.startswith('#'):
                query_terms.append(line.strip())
    template_data = {'query_terms': query_terms}
    return render_template('pycomic.html', **template_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)