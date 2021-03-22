"""from termcolor import colored
import os
os.system("color")
print(colored('hello', 'red'), colored('world', 'green'), end="\r")
print("\n")
from colorama import Fore
from colorama import Style

print(f'This is {Fore.GREEN}color{Style.RESET_ALL}!')   
"""
# Website mit Farbcodes: https://pypi.org/project/colored/
# Keyboard Listener: https://pynput.readthedocs.io/en/latest/keyboard.html#monitoring-the-keyboard

from pynput import keyboard
import os
from colored import fg, bg, attr, style
import json
 
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
width = int(terminal_width())
if width < 50:
    print("Width of Terminal only", width, "characters. Must be at least 50. Exiting.")
    exit()
leftphrase = "    Terminal Size: " + str(width)
rightphrase = "Exit with ESC    "



print("\n" + leftphrase + " " * (width-len(leftphrase)-len(rightphrase)-1) + rightphrase + "\n")
flag = []
for n in range(0, int(width/2)):
    flag.append("{0} ".format(bg(232)))
    flag.append("{0} ".format(bg(231)))
flag = "".join(flag)
secflag = (" ".join(flag.split(" ")[1:]))

print(secflag)
print(flag)    
print(secflag)


print("{0}".format(bg(1)) + " "*10 + "{0}".format(bg(1)) + " "*(width-2*10-1 + 10))
phrase = "QuoteRace CLI"
print("{0}".format(bg(0)) + " "*10 + "{0}   ".format(bg(1)) + "{0}".format(bg(0))  +  " "*(width-2*10-1-6) + "{0}   ".format(bg(1)) + "{0}".format(bg(0)) + " "*11)
print("{0}".format(bg(0)) + " "*10 + "{0}   ".format(bg(1)) + "{0}".format(bg(0))  +  " "*int((width-2*10-1-6-len(phrase))/2) + ("{0}{1}{2}" + phrase + "{3}").format(attr(1), attr(4), attr(5), attr(0)) + " "*int((width-2*10-6-len(phrase))/2) +  "{0}   ".format(bg(1)) + "{0}".format(bg(0)) + " "*10)
print("{0}".format(bg(0)) + " "*10 + "{0}   ".format(bg(1)) + "{0}".format(bg(0))  +  " "*(width-2*10-1-6) + "{0}   ".format(bg(1)) + "{0}".format(bg(0)) + " "*10)
print("{0}".format(bg(0))  + " "*10 + "{0}".format(bg(1)) + " "*(width-2*10-1) + "{0}".format(bg(0)) + " "*10 + style.RESET)


print(secflag)
print(flag)    
print(secflag + style.RESET, end = "\n\n")

phrase = "Type the following quote as fast as you can:"
print(" "*int((width-len(phrase))/2) + phrase)


# Opening Quotesfile

with open("quotes.json", "r", encoding="utf-8") as f:
    # Print all Quotes: quotes = json.dumps(json.loads(f.read()), indent=2)
    # print(quotes)
    print(json.load(f))

# Go on here




typed_string = []
ctrl_pressed = False


def on_press(key):
    global typed_string
    global ctrl_pressed
    try:
        typed_string.append(key.char)
        """if ctrl_pressed and key.char == "'\\x03'":
            if input("Noticed CTRL + c. Exit? (y|n): ") == "y":
                exit()"""
    except AttributeError:
        key = str(key)
        if key == "Key.backspace":
            try:
                typed_string.pop()
            except:
                pass
            if ctrl_pressed:
                try:
                    typed_string = " ".join("".join(typed_string).split(" ")[:-1])
                except:
                    pass
        elif key == "Key.space":
            typed_string.append(" ")
        elif key == "Key.shift":
            pass
        elif key == "Key.ctrl_l":
            ctrl_pressed = True
        else:
            print("\r" + "".join(typed_string) + "\t\t\t\t" + key[4:] + "           \r" + "".join(typed_string) , end = " ")
    
    print("\r" + "".join(typed_string) + "                " + "\r" + "".join(typed_string), end = " ") # +16 Spaces


def on_release(key):
    global ctrl_pressed
    if key == keyboard.Key.esc:
        # Stop listener
        listener.stop()
        return False
    if key == keyboard.Key.ctrl_l:
        ctrl_pressed = False

    

# Collect events until released
with keyboard.Listener(
        on_press=on_press, on_release=on_release) as listener:
    listener.join()

"""# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()"""

