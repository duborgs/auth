from car import Car
from motorcycle import Motorcycle
from motorcycle_adapter import MotorcycleAdapter # Import the adapter class
import traceback

if __name__ == '__main__':
    car = Car()
    bike = Motorcycle()
    bike_adapter = MotorcycleAdapter(bike) # Create the adapter

    ...

    try:
        print("Attempting to call client methods with the service object using an adapter\n")
        bike_adapter.assign_driver("Robert")
        bike_adapter.accelerate()
        bike_adapter.apply_brakes()
    except AttributeError:
        print("Oops! bike object cannot access car methods")
        traceback.print_exc()