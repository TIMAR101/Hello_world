def gradingStudents(grades):
    # Write your code here

    for ind, gr in enumerate(grades):

        #print(ind, gr)

        if gr < 38:
            continue
        else:

            rem = gr%5

            if rem >= 3:

                grades[ind] += 5-rem
            else:
                continue

    return grades


print(gradingStudents([86, 51, 84]))
