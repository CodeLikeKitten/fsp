import asyncio

from connection.SocketConnection import SocketConnection
from vehicle.Vehicle import Vehicle
from vehicle.vehicle_control import control_vehicle


async def start():
    connection = SocketConnection()
    vehicle = Vehicle(connection)
    await connection.set_connection()

    connection_status = connection.receive_data()
    print("connection status:", connection_status)

    await control_vehicle(vehicle, connection)

if __name__ == "__main__":
    asyncio.run(start())
