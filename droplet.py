class listsorter:
    def __init__(self,list):
        self.list = sorted(set(list))
    
    def __repr__(self):
        return str(self.list)
    
class sortcount():
    def __init__(self,list):
        self.list = sorted(set(list))
    
    def __repr__(self):
        return f"{int(len(self.list))}"

class count():
    def __init__(self,list):
        self.list = list
    def __repr__(self):
        return f"{int(len(self.list))}"