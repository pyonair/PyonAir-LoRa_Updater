import ttn
from base64 import b64encode


"""Enter application and device details here"""
app_id = "your application's name"
access_key = "your application's access key"
dev_id = "device id of the PyonAir you would like to update"

"""Command 0 - Reboot Device"""
# command = 0

"""Command 1 - Start update and reboot"""
# command = 1

"""Command 2 - Update wifi credentials"""
# command = 2
# ssid = "your network's SSID"
# password = "your network's password"

"""Command 3 = Update wifi credentials, start update and reboot"""
command = 3
ssid = "your network's SSID"
password = "your network's password"


# Construct message
msg = None
if command == 0 or command == 1:
    msg = str(command).encode()
else:
    msg = (str(command) + ":" + ssid + ":" + password).encode()

# Encode payload
hex_msg = b64encode(msg)
payload = hex_msg.decode()

# Create handler
handler = ttn.HandlerClient(app_id, access_key)
client = handler.data()

# Send payload
client.connect()
client.send(dev_id, payload, port=1, conf=False, sched="replace")
client.close()
