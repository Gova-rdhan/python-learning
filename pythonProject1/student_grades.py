marks = {
    "nani":90,
    "ravi":80,
    "upendar":70,
    "mnr":70
}
grades = {}
for i in marks:
    if marks[i] > 90:
        grades[i] = 'A'
    elif marks[i] > 80:
        grades[i] = 'b'
    elif marks[i] > 70:
        grades[i] = 'C'
    else:
        grades[i]='D'
print(marks)
print(grades)