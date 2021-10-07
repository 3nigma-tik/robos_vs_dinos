from robots import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        return 
    
    def create_fleet(self):
        robo_one = Robot("Chucky Chomper", 55, 300)
        robo_two = Robot("Sally Spikes", 45, 500)
        robo_three = Robot("Timmy Teeth", 50, 250)
        robo_four = Robot("Doug", 30, 250)
        return robo_one and robo_two and robo_three and robo_four 