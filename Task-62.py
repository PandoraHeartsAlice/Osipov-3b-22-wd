class Robot:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def movement(self, time):
        distance = self.speed * time
        print(
            f"The robot {self.name} has traveled {distance} meters in {time} seconds.")


class CaterpillarRobot(Robot):
    def __init__(self, name, speed, territory):
        super().__init__(name, speed)
        self.territory = territory


class WheelRobot(Robot):
    def __init__(self, name, speed, car_brand):
        super().__init__(name, speed)
        self.car_brand = car_brand


robot1 = Robot("Robot 1", 10)
robot1.movement(5)  # The robot Robot 1 has traveled 50 meters in 5 seconds.

caterpillar_robot = CaterpillarRobot("Caterpillar Robot", 5, "Land")
# The robot Caterpillar Robot has traveled 50 meters in 10 seconds.
caterpillar_robot.movement(10)
print(caterpillar_robot.territory)  # Land

wheel_robot = WheelRobot("Wheel Robot", 20, "Sedan")
# The robot Wheel Robot has traveled 160 meters in 8 seconds.
wheel_robot.movement(8)
print(wheel_robot.car_brand)  # Sedan
