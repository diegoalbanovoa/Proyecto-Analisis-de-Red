from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Configurar el servidor FTP
authorizer = DummyAuthorizer()
authorizer.add_user('usuario', 'contraseña', r'C:\ftp', perm='elradfmwMT')
handler = FTPHandler
handler.authorizer = authorizer

# Iniciar el servidor FTP
server = FTPServer(('0.0.0.0', 21), handler)
server.serve_forever()