
class DeliveryService:
    def deliver(self):
        pass
class BikeDelivery(DeliveryService):
    def deliver(self):
        print("Delivering food by Bike")
class CarDelivery(DeliveryService):
    def deliver(self):
        print("Delivering food by Car")

class DroneDelivery(DeliveryService):
    def deliver(self):
        print("Delivering food by Drone")
bike_delivery = BikeDelivery()
car_delivery = CarDelivery()
drone_delivery = DroneDelivery()
deliveries = [bike_delivery, car_delivery, drone_delivery]
for delivery in deliveries:
    delivery.deliver()


