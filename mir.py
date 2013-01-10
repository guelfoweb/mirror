#!/usr/bin/env python

# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# guelfoweb@gmail.com wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return Gianni 'guelfoweb' Amato
# ----------------------------------------------------------------------------

import sys, os

def help(code):
	if code == 1:
		print "File not found:", ifile
		exit()
	print "mir v1.0 - Reverses the bytes of a file"
	print "Author: Gianni 'guelfoweb' Amato"
	print "\nUSAGE:"
	print "\tmir [FROM FILE] [TO FILE]"
	exit()

# Arguments
if len(sys.argv) != 3:
	help(0)

ifile  = sys.argv[1]
ofile = sys.argv[2]

# File not exist
if os.path.isfile(ifile) == False:
	help(1)
	
fs = os.stat(ifile).st_size 
print "Mirroring", fs, "bytes..."

m = open(ofile, 'w+b')
f = open(ifile, 'rb')
for i in range(fs+1):
	f.seek(fs - i)
	byte = f.read(1)
	# print byte
	m.write(byte)
print "Ok"
f.close()
m.close()
