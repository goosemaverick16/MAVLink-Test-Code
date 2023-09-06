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
    #To parse certain aspects of telemetry, you have to specify the type, which will be seen in all caps.
    #That is, if you print all the telemetry. 
    msg = connection.recv_match(type = 'ATTITUDE',blocking=True)
    print(msg)
    print("----------------------------------------------------------------------------------")
    msg = connection.recv_match(type = 'VFR_HUD',blocking=True)
    print(msg)
    print("----------------------------------------------------------------------------------")
    msg = connection.recv_match(type = 'BATTERY_STATUS',blocking=True)
    print(msg)
    print("----------------------------------------------------------------------------------")
    msg = connection.recv_match(type = 'GLOBAL_POSITION_INT',blocking=True)
    print(msg)
    print("----------------------------------------------------------------------------------")
  