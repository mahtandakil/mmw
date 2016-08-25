#****************************************************************************
# Created for: MMw D
# Dev line: MMw D
# Last change: 09/08/2016
# Last change: 25/08/2016
#****************************************************************************/


GENML_BLOCK_OPEN = '<[GENML]>'
GENML_BLOCK_CLOSE = '<[/GENML]>'


import re
import os


#---------------------------------------------------------------------------

class GenML:
	
	def __init__(self):
		
		self.code = None
		self.values = {}
		
		self.loadValues()
		

	def __del__(self):
		q=0


#---------------------------------------------------------------------------

	def generateGenML(self, code):
	
		keep = True
		self.code = code

		while keep:
			
			block_def= self.searchBlock()
			keep = block_def[0]
			
			if block_def[0]:

				new_block = self.generation(block_def[1])
				self.code = self.code[:block_def[2]] + new_block + self.code[block_def[3]:]

		return self.code


#---------------------------------------------------------------------------

	def searchBlock(self):
		
		value = ""
		
		start = self.code.find(GENML_BLOCK_OPEN)
		end = self.code.find(GENML_BLOCK_CLOSE, start)

		if start > -1 and end > -1 and end > start:
			found = True
			value = self.code[start+len(GENML_BLOCK_OPEN):end]
		
		else:
			found = False
			
		return [found, value, start, end+len(GENML_BLOCK_CLOSE)]


#---------------------------------------------------------------------------

	def generation(self, code):

		code = self.generateCommands(code)
		
		return code
		

#---------------------------------------------------------------------------

	def loadValues(self):
		
		path = os.path.join('.', 'app', '.values.genml')
		
		f = open(path, 'r')
		
		line = f.readline()
		while line != "":
		
			line = line.replace('\n', '')
			values = line.split('=')

			if len(values) == 2:
				self.values[values[0]] = values[1]
				
			line = f.readline()

		f.close()
		

#---------------------------------------------------------------------------

	def generateCommands(self, code):
		
		re_value = 'VALUE\((.*)\)'
		re_value_r = re.search(re_value, code)
		if re_value_r:
			code = self.values[re_value_r.group(1)]

		return code
		

#---------------------------------------------------------------------------
