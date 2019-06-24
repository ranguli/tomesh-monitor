import netifaces as ni
import subprocess
import socket

from flask import Flask, request, render_template, json

app = Flask(__name__)

class Adapter():
    def __init__(self, name, ipv4, status):
        self.ipv4 = ipv4
        self.name = name
        self.status = status

def interfaces():
    # Only retrieve *physical* network interfaces
    adapters = subprocess.getoutput("find /sys/class/net -type l -not -lname '*virtual*' -printf '%f\n'").split()
    result = []

    for name in adapters:
        try:
            ipv4 = ni.ifaddresses(name)[ni.AF_INET][0]['addr'] or "Not assigned"
        except:
            ipv4 = "Unassigned."
        status = subprocess.getoutput("cat /sys/class/net/" + name + "/operstate")
        adapter = Adapter(name, ipv4, status)
        result.append(adapter)

    return result

@app.route('/hostname')
def hostname():
    return socket.gethostname()

@app.route('/interfaces')
def interfaces_as_json_string():
    return json.dumps([vars(interface) for interface in interfaces()])

@app.route('/')
def index():
    return render_template('index.html', adapters=interfaces(), hostname=hostname())

if __name__ == '__main__':
    app.run(debug = False)
