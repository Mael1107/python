# Desafio 029 em CursoemVideo

velocity= float(input("How many km/h were you driving? "))

if velocity> 80:
    fine = 7 * (velocity - 80)
    print(f"You have exceeded the maximum speed of 80km/h and were fined in R${fine:.2f}")
else:
    print("Very well, you are within the limit, keep it up!!")