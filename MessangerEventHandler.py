import watchdog
from datetime import datetime

class MessangerEventHandler(watchdog.events.FileSystemEventHandler):
    
    def __init__(self, listener):
        self.listener = listener
        super(watchdog.events.FileSystemEventHandler, self).__init__()
    
    def on_any_event(self, event):
        print event.src_path, event.event_type
        self._notify_listener(event)
        
    def _notify_listener(self, event):
        msg = event.src_path + event.event_type \
            + str(datetime.utcnow()) + ' UTC' # change to json format 
        self.listener.receive(msg)
    
