import netifaces as ni
import subprocess
import os 
import socket
from shutil import which

from flask import Flask, request, render_template, json, jsonify

app = Flask(__name__)

def is_installed(name):
    return which(name) is not None

class Adapter():
    def __init__(self, name, ipv4, status, iface_type):
        self.ipv4 = ipv4
        self.name = name
        self.status = status
        self.iface_type = iface_type

class Service():
    def __init__(self, name, status):
        self.name = name
        self.status = status

def interfaces():
    adapters = subprocess.getoutput("find /sys/class/net -type l -not -lname '*virtual*' -printf '%f\n'").split()
    result = []

    for name in adapters:
        try:
            ipv4 = ni.ifaddresses(name)[ni.AF_INET][0]['addr'] or "Not assigned"
        except:
            ipv4 = "Unassigned."
        status = subprocess.getoutput("cat /sys/class/net/" + name + "/operstate")

        # If the adapter is wireless, check the type of the interface (meshpoint, adhoc, etc) 
        if os.path.exists("/sys/class/net/" + name + "/wireless"):
            iface_type = subprocess.getoutput("iw dev " + name + " info | grep \"type\" | awk '{print $2}'").strip().capitalize()

        adapter = Adapter(name, ipv4, status, iface_type)
        result.append(adapter)
        iface_type = None

    return result

def services():
    service_list = ["cjdns", "yggdrasil", "hostapd", "ipfs", "ssb", "process-stream", 
                    "prometheus-node-exporter", "prometheus-server", "grafana-server", "yrd"]
    services = []
    
    for service in service_list:
        status = subprocess.getoutput("systemctl status " + service + ".service | grep 'Active: ' | awk '{ print $2}'")
        if status == "active" or status == "inactive":
            # IPFS Streaming must have ffmpeg installed
            if name == "process-stream.service" and is_installed('ffmpeg'):
                status = "active" 
        else:
            status = "unknown"

        service = Service(service, status)
        services.append(service)

    return services

@app.route("/services")
def services_as_json_string():
    return json.dumps([vars(service) for service in services()])

@app.route("/hostname")
def hostname():
    return socket.gethostname()

@app.route("/interfaces")
def interfaces_as_json_string():
    return json.dumps([vars(interface) for interface in interfaces()])

@app.route("/")
def index():
    return render_template("index.html", adapters=interfaces(), hostname=hostname(), services=services())

if __name__ == '__main__':
    app.run(debug = False)