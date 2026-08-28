# def make_profile(**data):
#     final_string = ""
#     for key, value in data.items():
#         string = f"{key}: {value}, "
#         final_string += string
#     return final_string.rstrip(", ")

# print(make_profile(name = "Ismael", age = 19))


def make_profile(**data):
    parts = []
    for key, value in data.items():
        parts.append(f"{key}: {value}")
    return ", ".join(parts)

print(make_profile(name = "Ismael", age = 19))