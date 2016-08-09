#****************************************************************************
# Created for: MMw C
# Dev line: MMw D
# Creation day: 26/01/2015
# Last change: 31/07/2016
# ****************************************************************************/


from engine.config import *


import os


#---------------------------------------------------------------------------

def cleanScreen():


	enabled = True

	if enabled:
		
		if os.name == "posix" or os.name == "linux2" or os.name == "linux3" or os.name == "linux4":
			os.system('clear')
		
		elif os.name == "nt" or os.name == "windows":
			os.system('cls')

		else:
			os.system('cls')


#---------------------------------------------------------------------------

def debugOutput(value):
	
	if DEBUG_OUTPUT:
		
		if DEBUG_TYPE == "Console_Short":
	
			print value


#---------------------------------------------------------------------------
