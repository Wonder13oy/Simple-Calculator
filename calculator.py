def add(num1, num2):
    result = float(num1) + float(num2)
    return result

def subtract(num1, num2):
    result = float(num1) - float(num2)
    return result

def multiply(num1, num2):
    result = float(num1) * float(num2)
    return result

def divide(num1, num2):
    if num2 == 0:
        raise ValueError('Can not divide by zero')
    result = float(num1) / float(num2)
    return result


