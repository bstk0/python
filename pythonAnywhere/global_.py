#global.py
class Global:
    def __init__(self):
        self.__local = True
        
    def isLocal(self,url):
        if checkUrl(self,url):
            self.__local = True
        else:
            self.__local = False    
        return self.__local

def checkUrl(self,url):
    if url.__contains__("127") or url.__contains__("5000"):
        return True
    else:
        return False