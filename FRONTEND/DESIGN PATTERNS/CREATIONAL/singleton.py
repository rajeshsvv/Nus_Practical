class Singleton():
    __instance=None

    @classmethod
    def Instance(cls):
        if cls.__instance==None:
            cls.__instance=Singleton()
        return cls.__instance

    def __init__(self):
        if self.__instance!=None:
            raise NotImplementedError("A Singleton instance is already existing")

    def setData(self,num):
        self.data=num

    def getData(self):
        return self.data


o=Singleton.Instance().setData(100)


print(f"Singleton data={Singleton.Instance().getData()}")
