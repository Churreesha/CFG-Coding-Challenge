# Define a function to round up a grade and report the result
#Should We Round up The final Grade?
def round_grade(grade):
    # Calculate the difference between the grade and the next multiple of 5
    difference = 5 - (grade % 5)
    # If the difference is less than 3 and the grade is not less than 40, round up the grade
    if difference < 3 and grade >= 40:
        grade = grade + difference
    # If the grade is less than 40, report fail
    if grade < 40:
        report = "fail"
    # If the grade is between 40 and 80, report pass
    elif grade <= 80:
        report = "pass"
    # If the grade is more than 80, report distinction
    else:
        report = "distinction"
    # Return the rounded grade and the report
    return grade, report

# Test the function with some examples
print(round_grade(93)) 
print(round_grade(38))
print(round_grade(47)) 