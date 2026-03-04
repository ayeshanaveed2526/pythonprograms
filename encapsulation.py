
class SmartDevice:
    def __init__(self, device_name):
        self.__device_name = device_name
        self.__device_status = "Off"

    def turn_on(self):
        self.__device_status = "On"
        print(f"{self.__device_name} is now {self.__device_status}.")

    def turn_off(self):
        self.__device_status = "Off"
        print(f"{self.__device_name} is now {self.__device_status}.")

    def get_status(self):
        print(f"{self.__device_name} is currently {self.__device_status}.")
smart_light = SmartDevice("Living Room Light")
try:
    print(smart_light.__device_status)
except AttributeError as e:
    print("Error: Cannot access private variable directly.")
smart_light.get_status()
smart_light.turn_on()
smart_light.get_status()
smart_light.turn_off()
smart_light.get_status()