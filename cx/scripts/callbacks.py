# action += ctx -> func
# ^ subscribe to action 
# action -= ctx -> func
# ^ unsubscribe from action 

class Events:
    def __init__(self) -> None:
        self.callbacks = {}
        
    def remove_callback(self, event, callback):
        if event in self.callbacks:
            self.callbacks[event].remove(callback)
    
    def add_callback(self, event, callback):
        if event not in self.callbacks:
            self.callbacks[event] = []
        self.callbacks[event].append(callback)
    
    def trigger(self, event, context):
        if event in self.callbacks:
            for callback in self.callbacks[event]:
                callback(context)