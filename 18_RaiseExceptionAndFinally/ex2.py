# Userdeifined Exception  (Exception is basically an instance/object of a class)  
# user defiend exceptions are always derieved from Exception base class
class Accident(Exception):
    def __init__(self,msg):
        self.msg = msg
    def handle(self):
        print(f"Accident Occured: {self.msg}")

try:
    raise Accident("Crash between two cars")  # you can write only Exception Class here because Accident is a subclass of Exception
except Accident as e:
    e.handle()
