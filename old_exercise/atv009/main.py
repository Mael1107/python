notes = []

for x in range(5):
    student_code = input("RM:")
    note = (input("Write your note:"))
    result = [student_code, note]
    # index = [    0      ,  1]
    notes.append(result)

print("The amount of notes is:", len(notes))

print("OThe RM",student_code, "took the note:", note)
