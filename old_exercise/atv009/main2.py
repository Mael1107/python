notes = []

cont = 0

while cont <5:
    student_code = input("RM:")
    note = input("Note:")
    result = [student_code, note]
    notes.append(result)

    # notes = [result, (student_code, note), result]

    cont = cont + 1

print("Amount notes:", len(notes))

