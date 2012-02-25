'''
Parts of this code is reused from the samples at 
http://www.tavendo.de/autobahn/tutorial/broadcast.html
and is Copyright 2011 Tavendo GmbH
'''

import logging
import sys
import os
import time

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from twisted.internet import reactor
from autobahn.websocket import WebSocketServerFactory, WebSocketServerProtocol, listenWS, WebSocketProtocol, ConnectionRequest

from MessangerEventHandler import MessangerEventHandler

from twisted.python import log

class FreshyServerProtocol(WebSocketServerProtocol):
    def connectionMade(self):
        print 'connection made'
        WebSocketServerProtocol.connectionMade(self)

    def onOpen(self):
        WebSocketServerProtocol.onOpen(self)
        self.factory.register(self)
        print 'Connection opened to', self.peerstr
    
    def sendFSEvent(self, json):
        WebSocketProtocol.sendMessage(self, json)
        print 'to', self.peerstr

    def onClose(self, wasClean, code, reason):
        print 'closed', self.peerstr
        WebSocketServerProtocol.onClose(self, wasClean,
                                        code, reason)
        self.factory.unregister(self)


class FreshyServerFactory(WebSocketServerFactory):
    protocol = FreshyServerProtocol

    def __init__(self, url='ws://localhost', port=4444):
        addr = url + ':' + str(port)
        print 'listening on', addr
        WebSocketServerFactory.__init__(self, addr)
        self.clients = []

    def register(self, client):
        if not client in self.clients:
            print 'registered client', client.peerstr
            self.clients.append(client)

    def unregister(self, client):
        if client in self.clients:
            print 'unregistered client', client.peerstr
            self.clients.remove(client)
        self._printConnected()

    def _printConnected(self):
        print 'connected clients:[',
        for client in self.clients:
            print client.peerstr + ',',
        print ']'

    # broadcasts a json msg to all clients
    def notify_clients(self, message):
        print 'broadcasting ', message
        for c in self.clients:
            c.sendFSEvent(message)
 
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: python freshy-server.py <dirs>'
        sys.exit(1)

    observers = []

    log.startLogging(sys.stdout)
    ffactory = FreshyServerFactory("ws://localhost", 4444)
    ffactory.protocol = FreshyServerProtocol
    listenWS(ffactory)
    
    for arg in sys.argv[1:]:
        dir_path = os.path.abspath(arg)
        if not os.path.exists(dir_path):
            print dir_path, 'does not exist.'
            sys.exit(1)
        if not os.path.isdir(dir_path):
            print dir_path, 'is not a directory.'
            sys.exit(1)
    
        event_handler = MessangerEventHandler(ffactory, reactor, os.getcwd())
        observer = Observer()
        observer.schedule(event_handler, path=dir_path, recursive=True)
        observer.start()
        observers.append(observer)
        
    try:
        reactor.run()
    except KeyboardInterrupt:
        for obs in observers:
            obs.stop()
        reactor.stop()
        print '\nbye'
        sys.exit(1)
    

