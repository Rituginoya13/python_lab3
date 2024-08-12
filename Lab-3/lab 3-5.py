class Calculator:
    def __init__(self, value1=0, value2=0):
        self.__value1 = value1
        self.__value2 = value2
    def set_values(self, value1, value2):
        self.__value1 = value1
        self.__value2 = value2
    def get_value1(self):
        return self.__value1
    def get_value2(self):
        return self.__value2
    def add(self):
        return self.__value1 + self.__value2
    def subtract(self):
        return self.__value1 - self.__value2
calculator = Calculator()
calculator.set_values(10, 5)
# print("Value 1:", calculator.get_value1())
# print("Value 2:", calculator.get_value2())
print("Addition:", calculator.add())
print("Subtraction:", calculator.subtract())
