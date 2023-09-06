# This is an example on how to send commands to Inkplate via peripheral mode from Raspberry Pi
# Check the README for more info

# Import required libraries
# PySerial must be installed!
import serial
import serial.tools.list_ports
import time # For waiting

# Function to find the first USB Serial device on Raspberry Pi
def find_first_serial_device():
    ports = list(serial.tools.list_ports.comports())
    # In case you have more than one USB device connected, uncomment the next line and find Inkplate there
    print("List of all the founds COM ports:")
    # Print the ports separated by a comma
    print(*ports, sep = ", ")
    for p in ports:
        if "USB" in p.description or "USB" in p.device:
            return p.device
    return None

# Function to send a peripheral mode command via Serial
def send_command_to_inkplate(inkplate, command):
    # Note the baud rate, it's always 115200
    with serial.Serial(inkplate, 115200, timeout=1) as ser:
        ser.write((command + "\n\r").encode('utf-8'))
        time.sleep(0.2) # Wait a bit, this ensures Inkplate has time to interpret the command

# Code runs from here
if __name__ == "__main__":
    # First, get Inkplate from the USB ports
    inkplate = find_first_serial_device()
    if inkplate:
        print("Found Inkplate on port " + str(inkplate)+"!")

        # Let's send some commands!
        # This is just a really basic example which will run on any Inkplate
        # For a full list of available commands, please refer to the documentation:
        # inkplate.readthedocs.io/en/latest/peripheral-mode.html

        # First, clear the image buffer, then, display the clear image
        send_command_to_inkplate(inkplate, "#K(1)*") # clearDisplay
        time.sleep(2) # Wait two seconds
        send_command_to_inkplate(inkplate, "#L(1)*") # display
        # The display should refresh at this moment!
        time.sleep(2) # Wait two seconds

        # Set the cursor for printing text to position x=50, y=50
        send_command_to_inkplate(inkplate, "#E(050,050)*")
        # Print a message
        # This is "Hello Raspberry Pi!" encoded in HEX Char
        # Note the quotation marks
        send_command_to_inkplate(inkplate, '''#C("48692052617370626572727920506921")*''')
        send_command_to_inkplate(inkplate, "#L(1)*") # Display it
    else:
        # In case there was an error, inform the user
        print("No USB serial device found!")