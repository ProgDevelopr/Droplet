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
    
class dropindex():
    def __init__(self,lst,indexnum):
        self.indexnum = indexnum
        self.lst = lst
    def drop(self):        
        self.lst.pop(self.indexnum)
    def __repr__(self):
        self.lst.pop(self.indexnum)
        return f"{self.lst}"
    
class addindex():
    def __init__(self,lst,numberorstr):
        self.lst = lst
        self.numberorstr = numberorstr
    def __repr__(self):
        self.lst.append(self.numberorstr)
        return f"{self.lst}"