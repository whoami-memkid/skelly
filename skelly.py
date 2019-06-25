#!/usr/bin/python2.7
import sys
import os

"""
from pwn import
elf             = ELF('./badchars')
p               = elf.process()




p.close()
"""

def write_file(f, filename):
    skelly =   "#!/usr/bin/python2.7\n"
    skelly +=  "from pwn import *\n\n"
    skelly +=  "elf             = ELF('')\n"
    skelly +=  "p               = elf.process()\n"
    skelly +=  "#p              = remote('', port)\n"
    skelly +=  "\n\n"
    skelly +=  "#p.recvuntil('')    #Change this to whatever comes before the input\n"
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

def set_perm(file_path, filename):
    os.chmod("{}".format(file_path), 0o744)


def append_file(filename):
    try:
        with open('{}'.format(filename), 'a') as f:
            write_file(f, filename)

    except:
        print "Error occurred in append_file"
    return filename


def usage():
    print "{} -o <new_file>".format(sys.argv[0])
    print "{} -h, --help".format(sys.argv[0])
    exit(0)


def main():
    if len(sys.argv) != 3:
        usage()
    for v in range(len(sys.argv)):
        if sys.argv[v] == "-o":
            filename = append_file(sys.argv[v+1])
            set_perm(sys.argv[v+1], filename)
        elif v >= len(sys.argv):
            print "Error occurred in main_for_else\n\n"
            usage()


if __name__ == '__main__':
    main()
