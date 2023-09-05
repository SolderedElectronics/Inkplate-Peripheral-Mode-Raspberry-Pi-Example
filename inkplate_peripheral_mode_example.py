# This is an example on how to send commands to Inkplate via peripheral mode from Raspberry Pi
# Check the README for more info

# Import required libraries
# PySerial must be installed!
import serial
import serial.tools.list_ports

# This variable is for selecting your Inkplate model
# In this example, different commands are run for different Inkplate models
# This is due to different available peripheral mode functions, colors and screen size
# Uncomment the line which corresponds to your Inkplate model
inkplate_model = "Inkplate2"
#inkplate_model = "Inkplate4"
#inkplate_model = "Inkplate4Tempera"
#inkplate_model = "Inkplate5"
#inkplate_model = "Inkplate6"
#inkplate_model = "Inkplate6Plus"
#inkplate_model = "Inkplate6COLOR"
#inkplate_model = "Inkplate7"
#inkplate_model = "Inkplate10"

# Function to find the first USB Serial device on Raspberry Pi
def find_first_serial_device():
    ports = list(serial.tools.list_ports.comports())
    # In case you have more than one USB device connected, uncomment the next line and find Inkplate there
    # print("List of all the founds COM ports: " + ports)
    for p in ports:
        if "USB" in p.description or "USB" in p.device:
            return p.device
    return None

# Function to send a peripheral mode command via Serial
def send_command_to_inkplate(inkplate, command):
    # Note the baud rate, it's always 115200
    with serial.Serial(inkplate, 115200, timeout=1) as ser:
        ser.write((command + "\n\r").encode('utf-8'))

# Code runs from here
if __name__ == "__main__":
    # First, get Inkplate from the USB ports
    inkplate = find_first_serial_device()
    if inkplate:
        print("Found Inkplate on port " + str(inkplate))

        # Example stuff...
        # TODO edit this
        send_command_to_inkplate(inkplate, "#5(050,100,040,01)*")
    else:
        print("No USB serial device found!")