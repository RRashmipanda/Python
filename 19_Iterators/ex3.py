#implement Remote Control Class allows you to press "next" button to get next channel

class RemoteControl ():
    def __init__(self):
        self.channels = ["HBO", "CNN", "ESPN", "DISCOVERY"]
        self.index = -1 # to start from the first channel when next is pressed

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1  
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]

r = RemoteControl()
itr=iter(r)  # called __iter__ returns the object itself
print(next(itr)) # called __next__ method
print(next(itr))            
print(next(itr))
print(next(itr)) 
print(next(itr)) # StopIteration     