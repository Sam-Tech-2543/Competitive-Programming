def gradingStudents(grades):
    # Write your code here
    ans = []
    for i in grades:
        if i < 40:

            if i + (5 - (i % 5)) - i < 3 and i + (5 - (i % 5)) >= 40:
                ans.append(i + (5 - (i % 5)))
            else:
                ans.append(i)
        else:
            if i + (5 - (i % 5)) - i < 3:
                ans.append(i + (5 - (i % 5)))
            else:
                ans.append(i)

    return ans


print(
    gradingStudents(
        [29, 35, 36, 37, 38, 39, 40, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
    )
)
