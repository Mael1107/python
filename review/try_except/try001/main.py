from typing import Union

def safe_divide(a: int, b: int) -> Union[float, str]:
    try:
        result = a / b
        return result #claude recomendou retornar só o valor bruto ao invés de uma f-string bonitinha 
    except ZeroDivisionError:
        return "Not possible to divide by zero!"


print(safe_divide(10, 0))