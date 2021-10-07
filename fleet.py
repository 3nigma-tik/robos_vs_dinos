from robots import Robot
from robots import Robot
from weapons import Weapon


class Fleet:
    def __init__(self):
        self.robots = [] 
    
    def create_fleet(self):
        robo_one = Robot("Debrabot 5000", 350, Weapon())
        robo_two = Robot("Paranoid Marvin", 200, Weapon())
        robo_three = Robot("Hal", 400, Weapon())
        robo_four = Robot("Siri", 250, Weapon())
        return robo_one and robo_two and robo_three and robo_four 
        
        