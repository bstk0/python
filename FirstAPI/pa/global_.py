#global.py
class Global:
    def __init__(self):
        self.__local = True
        
    def isLocal(self,url):
        if self.__checkUrl(self,url):
            self.__local = True
        else:
            self.__local = False    
        return self.__local

    def __checkUrl(self,url):
        if url.__contains__("127"):
            return True
        else:
            False
            