class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.odometer_reading = 22 # 초기값 설정

    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model}"
        return long_name.title() # 문자열 반환

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.") # 현재 주행거리 출력

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading: # 주행거리 갱신
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!") # 주행거리 감소 방지

    def increment_odometer(self, miles):
        self.odometer_reading += miles # 주행거리 증가

my_new_car = Car('audi', 'a4')

print(my_new_car.get_descriptive_name()) # 차량 정보 출력

my_new_car.update_odometer(23) # 주행거리 갱신
my_new_car.read_odometer() # 주행거리 출력