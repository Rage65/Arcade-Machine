
from digitalio import DigitalInOut, Pull, Direction   # pyright: ignore[reportMissingImports] (used for vscode to not show yellow squiggles)
import board  # pyright: ignore[reportMissingImports]
from adafruit_hid.keyboard import Keyboard # pyright: ignore[reportMissingImports]
from adafruit_hid.keycode import Keycode  # pyright: ignore[reportMissingImports]
import usb_hid # pyright: ignore[reportMissingImports]
import time

#defining keyboard
kbd = Keyboard(usb_hid.devices)

#Defining Buttons

#left alt+f4 (exit game button)
exit_button = DigitalInOut(board.GP16)
exit_button.direction = Direction.INPUT
exit_button.pull = Pull.UP # pulls up pin with an internal resistor

#ENTER key (used in many games )
ENTER_button = DigitalInOut(board.GP17)
ENTER_button.direction = Direction.INPUT
ENTER_button.pull = Pull.UP

#s key (used in doom to shoot)
shoot_button = DigitalInOut(board.GP18)
shoot_button.direction = Direction.INPUT
shoot_button.pull = Pull.UP
#x key (used in doom to use items and open doors)
use_button = DigitalInOut(board.GP19)
use_button.direction = Direction.INPUT
use_button.pull = Pull.UP

# Todo: on first powerup wait 3 minutes, then enter menu, put in kid mode, then exit conferming. 

#if loop to to press key when buttons are pressed, 
while True:
    if not exit_button.value: # using if not because button is pulled high
        kbd.press(Keycode.LEFT_ALT, Keycode.F4)
        time.sleep(0.65)
        kbd.release(Keycode.LEFT_ALT, Keycode.F4)
        time.sleep(1)
        
    elif not ENTER_button.value:
        kbd.press(Keycode.ENTER)
        time.sleep(0.05)
        kbd.release(Keycode.ENTER)
        time.sleep(0.2)
        
    elif not shoot_button.value:
        kbd.press(Keycode.S)
        time.sleep(0.05)
        kbd.release(Keycode.S)
        time.sleep(0.2)
        
    elif not use_button.value:
        kbd.press(Keycode.X)
        time.sleep(0.05)
        kbd.release(Keycode.X)
        time.sleep(0.2)
        
        