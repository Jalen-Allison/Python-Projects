# protected acts more as a warning to other developers and basically states that “this is protected - don't use outside of this class”
class Protected:
    def __init__(self):
        self.__privateVar = 32

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

# Obj gets the data of the private variable, but then we also set the privateVar a new value. We then ask for that to be retrieved.
obj = Protected()
obj.getPrivate()
obj.setPrivate(40)
obj.getPrivate()