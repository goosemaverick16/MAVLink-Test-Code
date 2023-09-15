from pymavlink import mavutil
from datetime import datetime
import tkinter as tk
import os
#Start a UDP connection. Note, the laptop should correct directly to the TBS tracer.
#Don't connect with COM9 and the 915 MHz radio! I get an Error 13 Permission denied if I do this.
#The IP Address comes from the connection IP, and the port is what I specified on TBS Agent Desktop.
#Please see notebook Entry 13 for more information.

def update_time():
    date =str(datetime.today().strftime("%I:%M %p"))
    date = date.replace('01:', '1:')
    date = date.replace('02:', '2:')
    date = date.replace('03:', '3:')
    date = date.replace('04:', '4:')
    date = date.replace('05:', '5:')
    date = date.replace('06:', '6:')
    date = date.replace('07:', '7:')
    date = date.replace('08:', '8:')
    date = date.replace('09:', '9:')
    return date

if __name__ == "__main__": 
    
    try:
        
        connection = mavutil.mavlink_connection('udpin:192.168.4.2:5760')
        connection.mav.request_data_stream_send(connection.target_system, connection.target_component, mavutil.mavlink.MAV_DATA_STREAM_ALL, 5 ,1)
        
        
        '''if os.path.getsize("TelemetryData.txt") > 0:
            window = tk.Tk()
            warning = tk.Label(text = "Warning! Telemetry exists in the file. Rewrite file?", font = ("Roboto",24))
            yes_button = tk.Button(window, text = "Yes", font = ("Roboto",24), command = lambda: [open_file_and_write(), window.destroy()])
            no_button = tk.Button(window, text = "No", font = ("Roboto",24), command = lambda: [open_file_and_append(), window.destroy()])
            warning.pack()
            yes_button.pack()
            no_button.pack()
            window.mainloop()'''
     
        file = open("TelemetryData.txt", "a")
        file.write("----------------------------------------------------------------------------------\n")

        file.write("Date and Time: " + update_time() + "\n")
        file.write("\n\n")

        #Wait for a heartbeat!
        connection.wait_heartbeat()
        print("Heartbeat from system (system %u, component %u)" %
            (connection.target_system,connection.target_component))

        while True:
            file = open("TelemetryData.txt", "a")
            #Lots of data will get printed beware!
            #To parse certain aspects of telemetry, you have to specify the type, which will be seen in all caps.
            #That is, if you print all the telemetry. 
            msg = connection.recv_match(type = 'ATTITUDE',blocking=True)
            print(msg)
            file.write(str(msg) +"\n")

            print("----------------------------------------------------------------------------------")
            file.write("----------------------------------------------------------------------------------\n")

            msg = connection.recv_match(type = 'VFR_HUD',blocking=True)
            print(msg)
            file.write(str(msg) +"\n")

            print("----------------------------------------------------------------------------------")
            file.write("----------------------------------------------------------------------------------\n")


            msg = connection.recv_match(type = 'BATTERY_STATUS',blocking=True)
            print(msg)
            file.write(str(msg) +"\n")

            print("----------------------------------------------------------------------------------")
            file.write("----------------------------------------------------------------------------------\n")


            msg = connection.recv_match(type = 'GLOBAL_POSITION_INT',blocking=True)
            print(msg)
            file.write(str(msg) +"\n")

        
            print("----------------------------------------------------------------------------------")
            file.write("----------------------------------------------------------------------------------\n")

            file.close()
            

        

    except OSError: #Handles no Address Error
    
        error_window = tk.Tk()
        error_window.title("Error.")
        error_label = tk.Label(text = "Invalid Address or Missing File.", font = ("Roboto", 24))
        error_label_2 = tk.Label(text = "Program terminated.", font = ("Roboto",24))
        error_button = tk.Button(error_window, text = "Ok", font = ("Roboto",24), command=error_window.destroy)
        error_label.pack()
        error_label_2.pack()
        error_button.pack()
        error_window.mainloop()
        


