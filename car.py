from abc import ABC, abstractmethod

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class Car(Serviceable):
    def __init__(self, last_service_date,engine,battery):
        self.last_service_date = last_service_date
        self.engine = engine
        self.battery = battery

    
    def needs_service(self):
        pass


class Battery:
    def __init__(self):
        self.engine = Car()

    def needs_service(self):
        pass


class Engine:
    def __init__(self):
        self.engine = Car()

    def needs_service(self):
        pass



