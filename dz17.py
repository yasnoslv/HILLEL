grades = {
    'Alice': [100, 90, 80],
    'Bob': [60, 70, 80],
    'Charlie': [80, 80, 80],
    'Dave': [70, 70, 70],
    'Eve': [60, 60, 60],
    'Frank': [50, 50, 50],
    'Gina': [40, 40, 40],
    'Hannah': [30, 30, 30],
    'Igor': [20, 20, 20],
    'Jenny': [10, 10, 10]
}
finals = {}
def mark_average(final_grades):
    for student in grades:
        grade = grades[student]
        average = sum(grade)/len(grade)
        final_grades[student] = average
        # print(f'{student}: {average}')
    print(final_grades)
mark_average(finals)