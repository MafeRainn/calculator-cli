class Calculator:
    def add(self, num1:float, num2:float) -> float:
        return num1 + num2
    def substract(self, num1:float, num2:float) -> float:
        return num1 - num2
    def multiply(self, num1:float, num2:float) -> float:
        return num1 * num2
    def divide(self, num1:float, num2:float) -> float:
        if num2 == 0:
            return "cannot divide by 0!"
        else:
            return num1 / num2