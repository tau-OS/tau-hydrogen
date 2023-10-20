# find all symlinks in this directory

import os
import sys

# walk through all files in Hydrogen/

arg = sys.argv[1]

for file in os.listdir(arg):
    if os.path.islink(file):
        # check if the link is broken
        if not os.path.exists(file):
            print(file, "->", os.readlink(file), "*** BROKEN ***")

            # get the link destination
            # change the readlink destination
            # replace /home/lains/Projects/tau-OS/tau-hydrogen with /home/cappy/Projects/tau-hydrogen in symlink destination
            # delete the old symlink
            os.system("ln -srf " + os.readlink(file).replace("/home/lains/Projects/tau-OS/tau-hydrogen", "/home/cappy/Projects/tau-hydrogen") + " " + file)
        else:
            print(file, "->", os.readlink(file))
