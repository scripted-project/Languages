class Functions:
    def __init__(self):
        self.functions = {}
    
    def add(self, name, implementation):
        self.functions[name] = implementation
    
    def remove(self, name):
        if name in self.functions:
            del self.functions[name]
            
    def call(self, name, *args):
        if name in self.functions:
            return self.functions[name](*args)

class Events:
    def __init__(self) -> None:
        self.callbacks = {}
        
    def remove(self, event, callback):
        if event in self.callbacks:
            self.callbacks[event].remove(callback)
    
    def add(self, event, callback):
        if event not in self.callbacks:
            self.callbacks[event] = []
        self.callbacks[event].append(callback)
    
    def trigger(self, event, context):
        if event in self.callbacks:
            for callback in self.callbacks[event]:
                callback(context)