#****************************************************************************
# Created for: MMw D
# Dev line: MMw D
# Last change: 31/07/2016
# Last change: 09/08/2016
#****************************************************************************/


from engine.config import *

from engine import webserver


#---------------------------------------------------------------------------

class Core:

	def __init__(self):
		q=0
		
	def __del__(self):
		q=0	


#---------------------------------------------------------------------------

	def start(self):

		print MMW_VERSION
		print
		print

		ows = webserver.WS()
		ows.initServer()


#---------------------------------------------------------------------------
