from abc import ABC, abstractmethod
class lbs(ABC):
    def addedWeight(self, amount):
        print("New weight: ",amount)
#this function is telling us to pass in an argument, but we won't tell you how or what kind of data it will be
    @abstractmethod
    def lbs_entered(self, amount):
        pass

class WeightEntered(lbs):
# here we've defined how to implement the payment function from its parents addedWeight class.
    def lbs_entered(self, amount):
        print('Your gained weight of {} is more than the recoomened 1-2 pound weekly gain'.format(amount))

obj = WeightEntered()
obj.addedWeight("190lb")
obj.lbs_entered("5lb")