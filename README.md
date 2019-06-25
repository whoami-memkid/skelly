# Skelly

This is a script that generates a basic skeleton for Binary exploitation.

Usage:

	./skelly.py -o <new_file>

	./skelly.py -h, --help


Skeleton:

	#!/usr/bin/python2.7
	
	from pwn import *

	elf             = ELF('')

	p               = elf.process()

	#p              = remote('', port)


	#p.recvuntil('')	 #Change this to whatever comes before the input

	payload = 'A' * 40 # Change Value

	"""
	with open('exploit.txt', 'w+') as f:
	    f.write(payload)
	    f.close()
	"""
	p.send()
	p.interactive()
