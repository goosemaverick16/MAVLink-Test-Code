from pymavlink import mavutil

'''
The heartbeat protocol is used to advertise the existence of a system on the MAVLink network, along with its system and component id, vehicle type, flight stack, component type, and flight mode.

The heartbeat allows other components to:

discover systems that are connected to the network and infer when they have disconnected. A component is considered to be connected to the network if its HEARTBEAT message is regularly received, and disconnected if a number of expected messages are not received.
handle other messages from the component appropriately, based on component type and other properties (e.g. layout a GCS interface based on vehicle type).
route messages to systems on different interfaces.

'''

#Start a UDP connection. Note, the laptop should correct directly to the Radiomaster.
#Don't connect with COM9 and the 915 MHz radio! I get an Error 13 Permission denied if I do this.
#The IP Address comes from the connection IP, and the port is what I specified on TBS Agent Desktop.
#Please see notebook Entry 13 for more information.

connection = mavutil.mavlink_connection('udpin:192.168.4.2:5760')

while True:
    #Wait for a heartbeat!
    connection.wait_heartbeat()
    print("Heartbeat from system (system %u, component %u)" %
        (connection.target_system,connection.target_component))
    