#!/usr/bin/python3

"""
Captures the rendered output from the X11 display and screenshots it, saving it as a image

Once execed, the script will wait for 1 second, capture a screenshot and close the process.

Parameters:
    * The only required parameter is the python3 script to run

Required packages:
    * X11
    * xvfb
    * imagemagick

Python packages:
    * xvfbwrapper

"""

from sys import argv, exit
from subprocess import Popen, run, PIPE
from xvfbwrapper import Xvfb

if len(argv) != 2:
    print(argv[0] + " <python_script_to_run>")
    exit(1)

TIMEOUT = 1

script_name = argv[1]

with Xvfb() as display:
    # Launch the tkinter problem
    args = "python3 " + script_name
    with Popen(args, shell=True, executable="/bin/bash", stdout=PIPE, stderr=PIPE) as p:
        try:
            p.wait(TIMEOUT)
        except:
            # Capture the screen
            display_num = display.new_display
            run("DISPLAY=:{} import -window root test.png".format(display_num), shell=True)

            # Kill the child if it doesn't exit automaticallyj
            p.kill()
