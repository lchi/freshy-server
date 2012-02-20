from datetime import datetime
import json
import string

import watchdog

class MessangerEventHandler(watchdog.events.FileSystemEventHandler):
    
    def __init__(self, listener, base_dir):
        self.listener = listener
        self.base_dir = base_dir
        super(watchdog.events.FileSystemEventHandler, self).__init__()
    
    def on_any_event(self, event):
        print event.src_path, event.event_type
        self._notify_listener(self._jsonize_event(event))

    def _notify_listener(self, msg):
        self.listener.receive(msg)
        
    def _jsonize_event(self, event):
        rel_path = string.replace(event.src_path, self.base_dir, '')
        return json.dumps(
            {'event':event.event_type,
             'obj':rel_path,
             'time':str(datetime.utcnow()) + ' UTC'})
        

