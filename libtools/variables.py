"""
    Static assignments for universally used colors and variables

"""
import os
from libtools.colors import Colors
from libtools.colors import ColorMap

# globals
c = Colors()
cm = ColorMap()

os_type = 'Linux'
user_home = os.getenv('HOME')
splitchar = '/'                                     # character for splitting paths (linux)

# special colors - linux
text = c.BLUE

# universal colors
act = c.ORANGE
rd = c.RED
yl = c.YELLOW
fs = c.GOLD3
bd = c.BOLD
gn = c.BRIGHT_GREEN
title = c.BRIGHT_WHITE + c.BOLD
cyn = c.CYAN
bcy = c.BRIGHT_CYAN
bbc = bd + c.BRIGHT_CYAN
bbl = bd + c.BRIGHT_BLUE
bgr = c.BLUE_GRAY
highlight = bd + c.BRIGHT_BLUE
frame = text
btext = text + c.BOLD
bwt = c.BRIGHT_WHITE
bdwt = c.BOLD + c.BRIGHT_WHITE
ub = c.UNBOLD
url = c.URL
rst = c.RESET
