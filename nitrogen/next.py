#!/usr/bin/python
import os
import re
import random

# Cycle library, in here because i dont wanna worry bout custom imports:
class cycle:
	def __init__(self, user_string, counter=0):
		self.u_str = user_string
		self.u_str_len = len(self.u_str)
		self.u_str_buff = None

		self.counter = counter


	def __next__(self):
		"""
		Replaces the character in the buffer (u_str_buff) by the next character
		Increases the counter by 1 
		OR resets it to 0 if the counter is at the maximum number
		else it would throw: IndexError: string index out of range
		
		Example usage:
		x = cycle(['foo', 'bar'])
		print(next(x))
		output:
		foo
		bar
		foo
		"""
		self.u_str_buff = self.u_str[self.counter]

		if self.counter < self.u_str_len:
			self.counter += 1

		if self.counter >= self.u_str_len:
			self.counter = 0

		return self.u_str_buff


	def next_item(self):
		"""
		== Updated version for this is __next__() ==
		Replaces the character in the buffer (u_str_buff) by the next character
		Increases the counter by 1 
		OR resets it to 0 if the counter is at the maximum number
		else it would throw: IndexError: string index out of range
		"""
		if self.counter >= self.u_str_len:
			self.counter = 0

		self.u_str_buff = self.u_str[self.counter]

		if self.counter < self.u_str_len:
			self.counter += 1

		return self.u_str_buff


	def get_counter(self):
		"""
		Returns the integer counter
		"""
		return self.counter


# Update cp to ~/.local
# You will have to change this depending on your name
# and there you have your nitrogen config
# my wallpapers are also in this directory
NITROGEN_PATH = "/home/sain/.config/nitrogen/"
bg_saved_cfg = NITROGEN_PATH + "bg-saved.cfg"

# False - No output | True - Debug output
debug = True

def get_current_bg():
	with open(bg_saved_cfg, 'r') as f:
		f.readline()
		current = f.readline()
		f.close()
	return current.split('/')[-1].strip()

def set_new_bg(bg_filename):
	os.popen( "nitrogen --set-auto %s" % NITROGEN_PATH + bg_filename )
	with open(bg_saved_cfg, 'w+') as f:
		f.write("[xin_-1]\n")
		f.write("file=/home/sain/.config/nitrogen/%s\n" % bg_filename)
		f.write("mode=0\n")
		f.write("bgcolor=#000000\n")
		f.close()

def main():
	# list all files fron ~/.config/nitrogen/
	# Load any files starting with bgx, x being any number
	bgs = os.popen("ls " + NITROGEN_PATH).read()
	bgs = bgs.split("\n")

	b = [i for i in bgs if i[-3:]=="jpg"]

	del(bgs)
	current_bg = get_current_bg()
	#print("bgs: " + bgs)
	if debug:
		print("Available backgrounds: ")
		print(b)
		print("Current background: '%s'" % current_bg)

	b.remove(current_bg)
	n = int(current_bg[-5])
	b.sort()

	cy = cycle(b, counter=n)
	new_bg =  cy.next_item()
	print "new bg", new_bg

	set_new_bg(new_bg)
	#rnd = random.randint(0, len(b) -1)

	#if debug:
		#print("RNG:", rnd)
		#print("new B:", b)


if __name__ == "__main__":
	main()
