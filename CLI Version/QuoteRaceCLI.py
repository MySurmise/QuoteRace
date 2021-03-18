"""from termcolor import colored
import os
os.system("color")
print(colored('hello', 'red'), colored('world', 'green'), end="\r")
print("\n")
from colorama import Fore
from colorama import Style

print(f'This is {Fore.GREEN}color{Style.RESET_ALL}!')   
"""

from pynput import keyboard
import os
from colored import fg, bg, attr



def terminal_width():
    try:
        size = os.get_terminal_size(1)
        term_num = 1
        return size[0]
    except:
        try:
            size = os.get_terminal_size(0)
            term_num = 0
            return size[0]
        except Exception as e:
            print(e, "That didn't work. Choosing Default-Value of 145. WARNING: Application could not work")
            return 145

# Get Terminal Size.
print("Getting Terminal Size... ", end="")
width = int(terminal_width())
print("found:", width)


print(" "*10 + "{0}".format(bg(1)) + " "*(width-2*10-1))
phrase = "QuoteRace CLI"
print("{0}".format(bg(0)) + " "*10 + "{0}   ".format(bg(1)) + "{0}".format(bg(0))  +  " "*(width-2*10-1-6) + "{0}   ".format(bg(1)))
print("{0}".format(bg(0)) + " "*10 + "{0}   ".format(bg(1)) + "{0}".format(bg(0))  +  " "*int((width-2*10-1-6-len(phrase))/2) + phrase + " "*int((width-2*10-6-len(phrase))/2) +  "{0}   ".format(bg(1)))
print("{0}".format(bg(0)) + " "*10 + "{0}   ".format(bg(1)) + "{0}".format(bg(0))  +  " "*(width-2*10-1-6) + "{0}   ".format(bg(1)))
print("{0}".format(bg(0))  + " "*10 + "{0}".format(bg(1)) + " "*(width-2*10-1) + "{0}".format(bg(0)))
print("\n\n")
phrase = "Type the following quote as fast as you can:"
print(" "*int((width-len(phrase))/2) + phrase)
typed_string = []

def on_press(key):
    global typed_string
    try:
        typed_string.append(key.char)
    except AttributeError:
        key = str(key)
        if key == "Key.backspace":
            try:
                typed_string.pop()
            except:
                pass
        elif key == "Key.space":
            typed_string.append(" ")
        elif key == "Key.shift":
            pass
        else:
            print("\r" + "".join(typed_string) + "\t\t\t\t" + key[4:] + "           \r" + "".join(typed_string) , end = " ")
    
    print("\r" + "".join(typed_string) + "                " + "\r" + "".join(typed_string), end = " ") # +16 Spaces


def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        listener.stop()
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

"""# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()"""

