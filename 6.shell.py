import os
import sys
import subprocess
import shutil


def ls():
    # get working directory
    loc = os.getcwd()
    c = os.listdir(loc)
    print(c)


def ls2(cmd):
    loc = cmd[1]
    c = os.listdir(loc)
    print(c)


def rm(cmd):
    if (len(cmd) == 2):
        file = cmd[1]
        if (file[0] != "/"):
            dir = os.getcwd()
            dirname = dir + "/" + file
            shutil.rmtree(dirname)
            print("remove " + dirname)
    else:
        pass


def cp(cmd):
    f1 = cmd[1]
    f2 = cmd[2]
    with open(f1, 'r') as file:
        data = file.read()
    with open(f2, 'w') as file:
        file.write(data)


def cd(cmd):
    loc = cmd[1]
    os.chdir(loc)


def wc(cmd, fname, option):
    num_lines = 0
    num_words = 0
    num_chars = 0
    line_length = []
    with open(fname, 'r') as f:
        for line in f:
            words = line.split()
            num_lines += 1
            num_words += len(words)
            num_chars += len(line)
            if (option == '-L'):
                line_length.append(len(line))
    if (option == 0):
        print(num_lines, " ", num_words, " ", num_chars, "", cmd[1])
    elif (option == '-c'):
        print(num_chars, " ", cmd[2])
    elif (option == '-l'):
        print(num_lines, " ", cmd[2])
    elif (option == '-w'):
        print(num_words, " ", cmd[2])
    elif (option == "-L"):
        print(max(line_length) - 1, " ", cmd[2])
    return


def mv(cmd):
    argc = len(cmd)
    if (argc != 3):
        sys.exit(216)
    try:
        src = os.path.abspath(cmd[1])
        des = os.path.abspath(cmd[2])
        os.rename(src, des)
    except Exception:
        sys.exit(216)


def pwd():
    currentDir = os.getcwd()
    print(currentDir)


def mkdir(cmd):
    if (len(cmd) == 2):
        os.mkdir(cmd[1])
    elif len(cmd) > 2:
        i = 1
        while (i != len(cmd)):
            try:
                os.mkdir(cmd[i])
                i = i + 1
            except IOError:
                sys.exit(216)


def rmdir(cmd):
    if (len(cmd) == 2):
        os.rmdir(cmd[1])
    elif len(cmd) > 2:
        i = 1
        while (i != len(cmd)):
            try:
                os.rmdir(cmd[i])
                i = i + 1
            except IOError:
                sys.exit(216)


def touch(cmd):
    path = cmd[1]
    if not os.path.exists(path):
        open(path, "w")


if __name__ == '__main__':
    while True:
        command = input("Enter your command line: \n")
        cmd = command.split(" ")
        print(cmd)
        if (cmd[0] == "cat"):
            fname = cmd[1]
            with open(fname, 'r')as file:
                data = file.read()
            print(data)
        elif cmd[0] == "ls" and len(cmd) == 1:
            ls()
        elif cmd[0] == "ls" and len(cmd) == 2:
            ls2(cmd)
        elif cmd[0] == "rm":
            rm(cmd)
        elif len(cmd) == 3 and cmd[0] == "cp":
            cp(cmd)
        elif len(cmd) == 2 and cmd[0] == "cd":
            cd(cmd)
        elif len(cmd) == 2 and cmd[0] == "wc":
            fname = cmd[1]
            option = 0
            wc(cmd, fname, option)
        elif len(cmd) == 3 and cmd[0] == "wc":
            option = cmd[1]
            fname = cmd[2]
            wc(cmd, fname, option)
        elif cmd[0] == "mv":
            mv(cmd)
        elif cmd[0] == "pwd":
            pwd()
        elif cmd[0] == "mkdir":
            mkdir(cmd)
        elif cmd[0] == "rmdir":
            rmdir(cmd)
        elif cmd[0] == "touch":
            touch(cmd)
        else:
            subprocess(cmd)
