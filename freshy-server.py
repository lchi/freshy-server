import sys
import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: python freshy-server.py <files>'
        sys.exit(1)

    for arg in sys.argv[1:]:
        file_path = os.path.abspath(arg)
        if not os.path.exists(file_path):
            print file_path, 'does not exist\nExiting...'
            sys.exit(1)
    
    
        logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path=file_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print 'bye'
        sys.exit(1)
    observer.join()
            
        

        
