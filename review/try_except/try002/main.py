def safe_sum(a, b):
    try:
        result = a + b
        return result
    except TypeError:
        return "Incompatible types for sum"


print(safe_sum(19, "1"))