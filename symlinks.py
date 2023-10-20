# find all symlinks in this directory

import os
import sys

# walk through all files in Hydrogen/
# get pwd

pwd = os.getcwd()

args = sys.argv

dirlist = []

# if extra args are only 1 (directory) then generate list of 1
for arg in args:
    if arg != args[0]:
        dirlist.append(arg)

print(dirlist)
# accept multiple args


def fixsymlink(dirs: list[str]):
    for dir in dirs:
        os.chdir(dir)
        for file in os.listdir("."):
            # print(file)
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

        os.chdir(pwd)


fixsymlink(dirlist)