import netifaces as ni
import subprocess

from flask import Flask, request, render_template, json

app = Flask(__name__)

class Adapter():
    def __init__(self, name, ip, status):
        self.ip = ip
        self.name = name
        self.status = status

def interfaces():
    adapters = subprocess.getoutput("find /sys/class/net -type l -not -lname '*virtual*' -printf '%f\n'").split()
    result = []

    for name in adapters:
        try:
            ip = ni.ifaddresses(name)[ni.AF_INET][0]['addr']
        except:
            ip = "Not assigned."
        status = subprocess.getoutput("cat /sys/class/net/" + name + "/operstate")
        adapter = Adapter(name, ip, status)
        result.append(adapter)

    return result

@app.route('/interfaces')
def interfaces_as_json_string():
    return json.dumps([vars(interface) for interface in interfaces()])

@app.route('/')
def index():
    return render_template('index.html', adapters=interfaces())

if __name__ == '__main__':
    app.run(debug = False)
