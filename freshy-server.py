import logging
import sys
import os
import time

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from twisted.internet import reactor
from autobahn.websocket import WebSocketServerFactory, WebSocketServerProtocol, listenWS

from MessangerEventHandler import MessangerEventHandler
from DummyListener import DummyListener

class EchoServerProtocol(WebSocketServerProtocol):
 
   def onMessage(self, msg, binary):
      self.sendMessage(msg, binary)
 
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: python freshy-server.py <dirs>'
        sys.exit(1)

    observers = []

    for arg in sys.argv[1:]:
        dir_path = os.path.abspath(arg)
        if not os.path.exists(dir_path):
            print dir_path, 'does not exist.'
            sys.exit(1)
        if not os.path.isdir(dir_path):
            print dir_path, 'is not a directory.'
            sys.exit(1)
    
        event_handler = MessangerEventHandler(DummyListener(), os.getcwd())
        observer = Observer()
        observer.schedule(event_handler, path=dir_path, recursive=True)
        observer.start()
        observers.append(observer)

    factory = WebSocketServerFactory("ws://localhost:1658")
    factory.protocol = EchoServerProtocol
    listenWS(factory)
    reactor.run()
    print 'asdkjskfjaf'
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        for obs in observers:
            obs.stop()
        print '\nbye'
        sys.exit(1)
    

