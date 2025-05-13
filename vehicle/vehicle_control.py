import random
import time

from connection.SocketConnection import SocketConnection
from vehicle.Vehicle import Vehicle


class BinaryDataHandler:
    def __init__(self, vehicle: Vehicle, connection: SocketConnection):
        self.connection = connection
        self.vehicle = vehicle

    async def start_driving(self):
        self.example_2()

    def example_2(self):
        # первый параметр - мощность вращения левых колес в процентах, второй параметр - мощность вращения правых колес.
        # если значение положительное, то колесо вращается по часовой стрелке, если отрицательно, то против часовой стрелки.
        self.vehicle.setMotorPower(100, 100)
        time.sleep(0.5)
        self.vehicle.setMotorPower(-90, 90)
        time.sleep(1)
        self.vehicle.rotate(1)
        self.vehicle.setMotorPower(40, 100)
        time.sleep(1.5)
        self.vehicle.setMotorPower(-100, 100)
        time.sleep(1)
        self.vehicle.setMotorPower(5, 5)
        time.sleep(0.1)
        self.vehicle.setMotorPower(-100, 100)
        time.sleep(0.8)
        self.vehicle.setMotorPower(5, 5)
        time.sleep(0.1)
        self.vehicle.setMotorPower(-100, 100)
        time.sleep(0.1)
        self.vehicle.setMotorPower(0, 0)
        time.sleep(0.1)
        self.vehicle.setMotorPower(10, 10)
        time.sleep(0.2)
        self.vehicle.setMotorPower(-100, 100)
        time.sleep(0.1)
        self.vehicle.setMotorPower(0, 0)
        time.sleep(0.1)
        self.vehicle.setMotorPower(5, 5)
        time.sleep(0.1)
        self.vehicle.setMotorPower(-100, 100)
        time.sleep(1)
        self.vehicle.setMotorPower(0, 0)
        time.sleep(0.1)
        self.vehicle.setMotorPower(9, 9)
        time.sleep(0.3)
        self.vehicle.setMotorPower(-100, 100)
        time.sleep(1)
        self.vehicle.setMotorPower(0, 0)
        time.sleep(0.1)
        self.vehicle.setMotorPower(9, 9)
        time.sleep(0.3)
        self.vehicle.setMotorPower(100, -100)
        time.sleep(0.2)
        self.vehicle.setMotorPower(9, 9)
        time.sleep(0.3)
        self.vehicle.setMotorPower(100, -100)
        time.sleep(0.2)
        self.vehicle.setMotorPower(9, 9)
        time.sleep(0.1)

        self.vehicle.setMotorPower(100, -100)
        time.sleep(0.2)
        self.vehicle.setMotorPower(9, 9)
        time.sleep(0.1)
        self.vehicle.setMotorPower(100, -100)
        time.sleep(0.2)
        self.vehicle.setMotorPower(0, 0)
        time.sleep(0.1)
        self.vehicle.setMotorPower(50, 10)
        time.sleep(1)
        self.vehicle.setMotorPower(100, -100)
        time.sleep(1.3)

        self.vehicle.setMotorPower(100, 50)
        time.sleep(0.4)
        self.vehicle.setMotorPower(100, 100)
        time.sleep(0.3)
        self.vehicle.setMotorPower(-100, 100)
        time.sleep(0.3)

        self.vehicle.setMotorPower(100, 100)
        time.sleep(0.3)
        self.vehicle.setMotorPower(-100, 100)
        time.sleep(0.3)



        self.vehicle.setMotorPower(0, 0)
        time.sleep(10)

    def save_image(self, image_data):
        filename = f"{str(int(time.time()))}_{str(random.random())}.webp"

        with open(filename, 'wb') as f:
            f.write(image_data)


async def control_vehicle(vehicle: Vehicle, connection: SocketConnection):
    data_handler = BinaryDataHandler(vehicle, connection)
    await data_handler.start_driving()
