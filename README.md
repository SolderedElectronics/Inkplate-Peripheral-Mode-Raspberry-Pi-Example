# Inkplate Peripheral Mode Raspberry Pi Example

This repository contains an example Python script which can be run on a Raspberry Pi to drive any Inkplate board using peripheral mode.

To get started, you will need:
- Your Inkplate
- Any Raspberry Pi model 
- A USB cable

### What is peripheral mode?

Peripheral mode is a sketch which is included in the [_Inkplate Library_](https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master) and it actually comes pre-flashed on your Inkplate board when you receive it. You can find it under the _Diagnostics_ subfolder in the examples for your particular board. 

Peripheral mode lets the user run commands from the Inkplate library via UART. This way, you can print text, draw shapes and even images from SD card all from sending commands via USB Serial at 115200 baud.

### How to use peripheral mode?

To use peripheral mode with Raspberry Pi, follow these steps:
1. Upload peripheral mode to your Inkplate device using Arduino IDE. In the Inkplate Library, it's under the _Diagnostics_ subfolder in the examples for your particular board.
2. Transfer the `inkplate_peripheral_mode_example.py` script from this repository to your Raspberry Pi and place it in a working directory.
3. PySerial must be installed on the Raspberry Pi to enable Serial communication. To install it, simply run `sudo pip3 install pyserial` in the terminal.
4. Connect Inkplate via USB to the Raspberry Pi.
5. Run the Python script on Raspberry Pi by opening a terminal in the working directory and running the command `sudo python3 inkplate_peripheral_mode_example.py`.

### What are the available commands?

Some commands such as `display`, `clearDisplay` and `print` are demonstrated in `inkplate_peripheral_mode_example.py`.

For a detailed overview of all commands available for Peripheral mode, check [_the documentation_](https://inkplate.readthedocs.io/en/latest/peripheral-mode.html).

### About Soldered

<img src="https://raw.githubusercontent.com/e-radionicacom/Soldered-Generic-Arduino-Library/dev/extras/Soldered-logo-color.png" alt="soldered-logo" width="500"/>

At Soldered, we design and manufacture a wide selection of electronic products to help you turn your ideas into acts and bring you one step closer to your final project. Our products are intended for makers and crafted in-house by our experienced team in Osijek, Croatia. We believe that sharing is a crucial element for improvement and innovation, and we work hard to stay connected with all our makers regardless of their skill or experience level. Therefore, all our products are open-source. Finally, we always have your back. If you face any problem concerning either your shopping experience or your electronics project, our team will help you deal with it, offering efficient customer service and cost-free technical support anytime. Some of those might be useful for you:

- [Web Store](https://www.soldered.com/shop)
- [Tutorials & Projects](https://soldered.com/learn)
- [Community & Technical support](https://soldered.com/community)

### Open-source license

Soldered invests vast amounts of time into hardware & software for these products, which are all open-source. Please support future development by buying one of our products.

Check license details in the LICENSE file. Long story short, use these open-source files for any purpose you want to, as long as you apply the same open-source license to it and disclose the original source. No warranty - all designs in this repository are distributed in the hope that they will be useful, but without any warranty. They are provided "AS IS", therefore without warranty of any kind, either expressed or implied. The entire quality and performance of what you do with the contents of this repository are your responsibility. In no event, Soldered (TAVU) will be liable for your damages, losses, including any general, special, incidental or consequential damage arising out of the use or inability to use the contents of this repository.

## Have fun!

And thank you from your fellow makers at Soldered Electronics.
