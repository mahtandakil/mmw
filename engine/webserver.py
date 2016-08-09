#****************************************************************************
# Created for: MMw D
# Dev line: MMw D
# Last change: 31/07/2016
# Last change: 09/08/2016
#****************************************************************************/


from engine.config import *


from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from urlparse import parse_qs


from os import curdir, sep
import os


########################################################################

class WSH(BaseHTTPRequestHandler):

#---------------------------------------------------------------------------

	def do_GET(self):
		
		sendvars = {}
		
		response = WSHWComposer(self.path, self.headers, parse_qs(self.path), sendvars)
		
		self.send_response(response['status'])
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write(response['content'])
		return
		

########################################################################

class WS:

#---------------------------------------------------------------------------

	def startServer(self):

		self.server = HTTPServer(('', SERVER_PORT), WSH)
		self.openBrowser()
		self.server.serve_forever()


#---------------------------------------------------------------------------

	def openBrowser(self):
				
		if os.path.isfile(WEB_BROWSER_WINDOWS):
			os.system("\"" + WEB_BROWSER_WINDOWS + "\" http://localhost:" + str(SERVER_PORT) + "/" + SERVER_INDEX_URL)
		
		elif os.path.isfile(WEB_BROWSER_LINUX):
			os.system(WEB_BROWSER_LINUX + " http://localhost:" + str(SERVER_PORT) + "/" + SERVER_INDEX_URL)
		
		else:
			print "Serving http://localhost:" + str(SERVER_PORT) + "/" + SERVER_INDEX_URL


#---------------------------------------------------------------------------

	def initServer(self):

		if SERVER_FAILSAFE:

			try:		
				self.startServer()

			except:
				print "[!]SERVER FAILURE"

				if not self.server == None:
					self.server.socket.close()

		else:
			self.startServer()
			

########################################################################

def WSHWComposer(url, headers, params, sendvars):
	
	response = {'status':404, 'headers': [], 'content': ''}
	
	if url == "/" or url == "":
		url = 'index.wiz'

	if url[-4:] == ".wiz":
		WSHWServeURL(url, headers, params, sendvars, response)
		
	return response


#---------------------------------------------------------------------------

def WSHWServeURL(url, headers, params, sendvars, response):

	response['headers'].append(['Content-type','text/html'])
	
	path = os.path.join (APP_FOLDER, url[1:].replace('.wiz', ''))
	
	fHtml = os.path.exists(path + '.html')
	fPyml = os.path.exists(path + '.py')

	if fHtml:
		f = open(path + '.html')
		response['status'] = 200
		response['content'] = f.read()
		f.close()

	if fPyml:
		response['status'] = 200
		pyml = path + 'py'
		opyml = importlib.import_module(pyml)
		response['content'] = opyml.process(url, headers, params, sendvars, response)

	return response


########################################################################
