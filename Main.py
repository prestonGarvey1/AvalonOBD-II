import obd
import RPi.GPIO as GPIO
from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.lcd.device import hd44780

#GPIO Screen Setup

# Sets up GPIO mode (BCM or BOARD)
GPIO.setmode(GPIO.BCM)  
    
# Configure the screen interface (I2C or SPI). Adjust parameters as needed for your screen.
serial = i2c(port=1, address=0x27) # Example for I2C LCD

# Initialize the screen 
screen = hd44780(serial, cols=16, lines=2)

def print_to_screen(text):
    with canvas(screen) as draw:
        draw.text((0, 0), text, fill="white")

#Use OBD
connection = obd.OBD(portstr="/dev/rfcomm0")

print_to_screen(obd.commands.RPM)
