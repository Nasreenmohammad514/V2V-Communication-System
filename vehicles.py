import random

class Vehicle:
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.position = random.randint(0, 100)   # Road lo position
        self.speed = random.randint(40, 100)     # Speed km/h
        self.message = None                      # Last received message

    def move(self):
        # Vehicle forward move avutundi
        self.position += self.speed * 0.1

    def send_message(self, msg):
        self.message = f"{msg} (Sent by V{self.vehicle_id})"
    
    def receive_message(self, msg):
        self.message = msg
