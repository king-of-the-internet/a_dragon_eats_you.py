#!/usr/env/python
#A DRAGON EATS YOU VERSION 0.01A

from random import randint
from msvcrt import getch
enemynames = ["Vampire", "Werewolf", "Ogre", "Sphinx", "Emp", "Globlin", "Minotaur", "Harpee", "Banshee", "Cyclops", "Hydra", "Cerberus", "Demon", "Balrog", "Dragon", "Fire God", "Wind God", "Water God", "Earth God", "Cirno"]

def gameover(curenemy, dieresult):
	if curenemy <= 19:
		print "You roll the die, and it landed on 1... a dragon eats you."	
	else:
		print "Chorimod furiously rolls his die at you, and it lands on %s... A dragon eats you." % dieresult
	if curenemy == 1:
		print "You have survived 1 encounter."
	else:
		print "You have survived %i encounters." % curenemy
	exit();
	
def diecheck(curenemy):
	dieroll();
	if dieresult == 1:
		gameover(curenemy, dieresult);
	else:
		print "You roll the die, and it landed on %i. You defeated the %s!" % (dieresult, enemynames[curenemy])
		curenemy = curenemy + 1

def diecheck_ssw():
	dieroll();
	if dieresult == 1:
		gameover(curenemy, dieresult);
	else: #diecheck_ssw() usually passed all this to another function but memed the HP values and reset them to the original ones
		global kikkoman_hp
		kikkoman_hp = kikkoman_hp - dieresult
		if kikkoman_hp > 0:
			print "You roll the die, and it landed on %s. Chorimod has %s HP remaining!" % (dieresult, kikkoman_hp)
			dieroll();
			global your_hp
			your_hp = your_hp - dieresult
			if your_hp > 0:
				print "Chorimod furiously rolls his die at you, and it lands on %s. You have %s HP remaining! Press R to roll the die and fight!" % (dieresult, your_hp)
			else:
				gameover(curenemy, dieresult); 
		else:
			print "You roll the die, and it landed on %s. You have finally won!!!" % dieresult

def dieroll():
	global dieresult
	dieresult = randint(1,6)

def round():
	print "A %s approaches. Press R to roll." % enemynames[curenemy]
	await_r();
	diecheck(curenemy);
	
def await_r():
	ch = getch()
	while ch != "r":
		ch = getch()

def finalround():
	global kikkoman_hp
	global your_hp
	print "\nYou sure are a crazy motherfucker, huh? Covered in the blood of your foes you stand there, panting. You have 10HP remaining, when suddenly--!\n"
	print "A particularly autistic Chorimod approaches, sporting 15HP. Press R to fight for your life!"
	kikkoman_hp = 15
	your_hp = 10
	while kikkoman_hp > 0:
		await_r();
		diecheck_ssw();
	print "You have survived 21 encounters. Here is your prize:"
	print "It's fucking nothing!!!\n"
	exit();					

print "Welcome to A Dragon Eats You!"
for curenemy in range (0,20):
	round();
for curenemy in range (21):
	finalround();

exit();
