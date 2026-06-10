import requests
import yaml

vars = yaml.safe_load(open("../vars/vars_005D-11.yaml"))

base_url = f"https://{vars['router']['ip']}/restconf/data"
auth = (vars["router"]["usuario"], vars["router"]["password"])
headers = {"Accept": "application/yang-data+json"}

def get(endpoint, filename):
    r = requests.get(base_url + "/" + endpoint, auth=auth, headers=headers, verify=False)
    open("evidencias/responses/" + filename, "w").write(r.text)
    return r.text

print("=== VALIDACION RESTCONF ===")

h = get("Cisco-IOS-XE-native:native/hostname", "get_hostname.json")
l = get("ietf-interfaces:interfaces/interface=Loopback10", "get_loopback.json")
i = get("ietf-interfaces:interfaces/interface=GigabitEthernet1", "get_interfaces.json")
n = get("Cisco-IOS-XE-native:native/ntp", "get_ntp.json")

ok = 0

if vars["cliente"]["hostname"] in h:
    print("[OK] Hostname")
    ok+=1

if vars["router"]["loopback_ip"] in l:
    print("[OK] Loopback")
    ok+=1

if vars["router"]["descripcion_wan"] in i:
    print("[OK] WAN")
    ok+=1

if vars["router"]["ntp_server"] in n:
    print("[OK] NTP")
    ok+=1

print(f"\nResultado: {ok}/4")

if ok == 4:
    print("CONFORME")
else:
    print("NO CONFORME")
