import sys
import random
from pyfiglet import Figlet

inp = sys.argv[1:]
figlet = Figlet()
fonts = figlet.getFonts()
if len(inp) == 0: # random font
    _ = random.shuffle(fonts)
    figlet.setFont(font=fonts[0])
    print(figlet.renderText(input('Input: ')))
elif len(inp) == 2:
    if (inp[0] == '-f' or inp[0] == '--font') and inp[1] in fonts: #user's font
        figlet.setFont(font=inp[1])
        print(figlet.renderText(input('Input: ')))
    else: sys.exit


