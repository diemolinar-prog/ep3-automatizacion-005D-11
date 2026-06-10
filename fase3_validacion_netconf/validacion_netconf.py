from ncclient import manager
import yaml
from datetime import datetime
import socket

# Cargar variables
vars = yaml.safe_load(open("../vars/vars_005D-11.yaml"))

print("=== VALIDACION NETCONF ===")
print("Alumno:", vars["alumno"]["nombre"])
print("Fecha:", datetime.now())
print("Host:", socket.gethostname())

# Conexión NETCONF
with manager.connect(
    host=vars["router"]["ip"],
    port=830,
    username=vars["router"]["usuario"],
    password=vars["router"]["password"],
    hostkey_verify=False,
    allow_agent=False,
    look_for_keys=False
) as m:

    filter = """
    <filter>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"/>
    </filter>
    """

    config = m.get_config("running", filter)
    xml = config.xml

    # Guardar evidencia
    open("evidencias/rpc_reply_raw.xml", "w").write(xml)

    checks = 0

    def check(nombre, valor):
        global checks
        if valor in xml:
            print(f"[OK] {nombre}")
            return 1
        else:
            print(f"[FAIL] {nombre}")
            return 0

    checks += check("Hostname", vars["cliente"]["hostname"])
    checks += check("Loopback IP", vars["router"]["loopback_ip"])
    checks += check("Mascara", vars["router"]["loopback_mask"])
    checks += check("WAN Desc", vars["router"]["descripcion_wan"])
    checks += check("NTP", vars["router"]["ntp_server"])

    print(f"\nResultado: {checks}/5")

    if checks == 5:
        print("CONFORME")
    else:
        print("NO CONFORME")
