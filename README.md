# tomesh monitor

A small Flask-based status monitor for LCD-enabled Raspberry Pi-based nodes in the Toronto Mesh Network ([Tomesh](https://github.com/tomeshnet)) designed to report node status and run in kiosk mode on Chromium.
![screenshot](screenshot.png)

## To-Do:
- [x] Setup a working Flask app
- [x] Detect the name, IP and up/down status of all physical network interfaces
- [ ] Add third column for IPv6 addresses
- [ ] Detect the hostname (Usually tomesh-xxxx in the case of a tomesh node)
- [ ] Display the time in top right corner?
- [ ] Perform the same detections as the [status](https://github.com/tomeshnet/prototype-cjdns-pi/blob/master/scripts/status) bash script, and display the status of the following:
  - [ ] Mesh Point Interface
  - [ ] Yggdrasil
  - [ ] CJDNS
  - [ ] Mesh Adhoc
  - [ ] hostapd
  - [ ] IPFS
  - [ ] Node Explorer
  - [ ] Prometheus
  - [ ] Grafana
