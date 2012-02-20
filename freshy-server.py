import logging
import sys
import os
import time

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

from MessangerEventHandler import MessangerEventHandler
from DummyListener import DummyListener

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
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        for obs in observers:
            obs.stop()
        print '\nbye'
        sys.exit(1)

            
        

        
