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
import random

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


def colorprint(text, colorcode, repeat, linebreak):
    #print("{0}".format(bg(colorcode)), end = "")
    print((("{0}" + text).format(bg(colorcode))) * repeat, end = "")
    print("{0}".format(bg(0)), end = "")
    if linebreak:
        print("")

def centerline(percentage, colorcode):
    global width
    leng = int(width * percentage)
    print(" " * int((width - leng)/2))
    colorprint(" ", colorcode, leng, True)


print("\n" + leftphrase + " " * (width-len(leftphrase)-len(rightphrase)-1) + rightphrase + "\n")

# flag generator
flag = []
for n in range(0, int(width/2)):
    flag.append("{0} ".format(bg(232)))
    flag.append("{0} ".format(bg(231)))
flag = "".join(flag)
secflag = (" ".join(flag.split(" ")[1:]))

print(secflag)
print(flag)    
print(secflag)


colorprint(" ", 1, width, True)


colorprint(" ", 0, 10, False)
colorprint(" ", 1, 3, False)
colorprint(" ", 0, width-26, False)
colorprint(" ", 1, 3, False)
colorprint(" ", 0, 10, True)


colorprint(" ", 0, 10, False)
colorprint(" ", 1, 3, False)
phrase = "QuoteRace CLI"
colorprint(" ", 0, int((width-2*10-1-6-len(phrase))/2), False)
print(("{0}{1}{2}" + phrase + "{3}").format(attr(1), attr(4), attr(5), attr(0)), end = "")
colorprint(" ", 0, int((width-2*10-3-len(phrase))/2), False)
colorprint(" ", 1, 3, False)
colorprint(" ", 0, 8, True)

colorprint(" ", 0, 10, False)
colorprint(" ", 1, 3, False)
colorprint(" ", 0, width-26, False)
colorprint(" ", 1, 3, False)
colorprint(" ", 0, 10, True)


colorprint(" ", 1, width, True)




print(secflag)
print(flag)    
print(secflag + style.RESET, end = "\n\n")

def center_print(phrase): 
    print(" "*int((width-len(phrase))/2) + phrase)

center_print("Type the following quote as fast as you can:")


# Opening Quotesfile

with open("quotes.json", "r", encoding="utf-8") as f:
    # Print all Quotes: 
    # quotes = json.dumps(json.loads(f.read()), indent=2)
    # print(quotes)
    quotes = json.load(f)

rand_quote = random.choice(quotes)
line_length = int(width*0.6)
line_number = int(len(rand_quote["quote"]) / line_length) + 1
words = rand_quote["quote"].split(" ")
count = 0
line_index = 0
lines = {}
lines[0] = []
for word in words:
    count += len(word) + 1
    lines[line_index].append(word)
    if count >= line_length:
        line_index += 1
        count = 0
        lines[line_index] = []
    

print(line_number) 
for line_index in range(0, len(lines)):
    print("{0}".format(fg(random.randint(5,225))))
    center_print(" ".join(lines[line_index]))
print(" " * int(width/2 + width/10), "-",  rand_quote["author"])





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
                    typed_string = list(" ".join("".join(typed_string).split(" ")[:-1]) )
                    if len(typed_string) != 0:
                        typed_string.append(" ")
                    #print(typed_string)
                except Exception as e:
                    print(e)
        elif key == "Key.space":
            typed_string.append(" ")
        elif key == "Key.shift":
            pass
        elif key == "Key.ctrl_l":
            ctrl_pressed = True
        else:
            print("\r" + "".join(typed_string) + " " * (int(width/5 - len(typed_string)/2)) + key[4:] + "           \r" + "".join(typed_string) , end = " ")
    
    print("\r" + "".join(typed_string) + " " * (int((width - len(typed_string))/2)) + "\r" + "".join(typed_string), end = " ") # +16 Spaces


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

