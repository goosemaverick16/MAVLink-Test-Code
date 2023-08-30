#Nick Howard
#8/30/2023
# First UDP MAVLink Code for Eaglet III
from pymavlink import mavutil

#Start a UDP connection. Note, the laptop should correct directly to the TBS tracer.
#Don't connect with COM9 and the 915 MHz radio! I get an Error 13 Permission denied if I do this.
#The IP Address comes from the connection IP, and the port is what I specified on TBS Agent Desktop.
#Please see notebook Entry 13 for more information.

connection = mavutil.mavlink_connection('udpin:192.168.4.2:5760')

#Wait for a heartbeat!
connection.wait_heartbeat()
print("Heartbeat from system (system %u, component %u)" %
    (connection.target_system,connection.target_component))

while True:
    #Lots of data will get printed beware!
    msg = connection.recv_match(blocking=True)
    print(msg)