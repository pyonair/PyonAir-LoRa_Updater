# PyonAir-LoRa_Updater

Python script to send commands to the PyonAir over LoRaWAN to trigger a software update.

Fill in details, and run script (main.py) to schedule a message to the device corresponding to dev_id.
The message is likely to arrive shortly after the device has sent a message over LoRaWAN.
It is not recommended to set confirmation to True, because it is not assured that the device will have time to respond before it reboots, which may cause further messages sent by the gateway possibly overloading the network.

command 0 - reboot the device

command 1 - trigger software update

command 2 - update wifi credentials

command 3 - update credentials, trigger update and reboot the device
