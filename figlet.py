"""
import sys
import random
import argparse
import pyfiglet
#THERE IS NO MODULE NAMED 'PYFIGLET'

# define command line arguments parser
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--font', help='name of the font to use')

# parse command line arguments
args = parser.parse_args()

# if font is provided, use it
if args.font:
    # check if font exists
    if args.font not in pyfiglet.FigletFont.getFonts():
        sys.exit('Error: Font not found.')
    font = args.font
else:
    # select a random font
    font = random.choice(pyfiglet.FigletFont.getFonts())

# prompt the user for input
text = input('Enter text to display: ')

# create the FIGlet object with the chosen font
fig = pyfiglet.Figlet(font=font)

# display the output
print(fig.renderText(text))
"""