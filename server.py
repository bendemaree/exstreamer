from cherrypy import wsgiserver
import web



server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', 8070), exstreamer-srv, server_name='exstreamer.srv')
server.start()
