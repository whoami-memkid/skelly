#!/usr/bin/python2.7
import sys

"""
from pwn import
elf             = ELF('./badchars')
p               = elf.process()




p.close()
"""
def write_file(f, filename):
    skelly =   "from pwn import *\n"
    skelly +=  "elf             = ELF('./{}')\n".format(filename)
    skelly +=  "p               = elf.process()\n"
    skelly +=  "#p              = remote('', port)\n"
    skelly +=  "\n\n"
    skelly +=  "#p.recvuntil('')\n"
    skelly +=  "\n\n"
    skelly +=  "payload = 'A' * 40 # Change Value\n"
    skelly +=  "\n\n"
    skelly +=  '"""\n'
    skelly +=  "with open('exploit.txt', 'w+') as f:\n"
    skelly +=  "    f.write(payload)\n"
    skelly +=  "    f.close()\n"
    skelly +=  '"""\n'
    skelly +=  "p.send()\n"
    skelly +=  "p.close()\n"
    skelly +=  "p.interactive()\n"
    f.write(skelly)
    f.close()

def create_file(filename):
    try:
        with open('{}'.format(filename), 'a') as f:
            write_file(f, filename)
    except:
        print "Error occurred - create_file"
    return filename

def use_file(filename):
    try:
        with open('{}'.format(filename), 'a') as f:
            write_file(f, filename)
    except:
        print "Error occurred - use_file"
    return filename

def main():
    for v in range(len(sys.argv)):
        if sys.argv[v] == "-o":
            filename = create_file(sys.argv[v+1])
        elif sys.argv[v] == "-f":
            filename = use_file(v+1)


if __name__ == '__main__':
    main()
