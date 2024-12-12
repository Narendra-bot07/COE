salary = int(input("Enter Salary "))
_bill1 = int(input("Enter Bill1 "))
_bill2 = int(input("Enter Bill2 "))
_bill3 = int(input("Enter Bill3 "))
total_bill = _bill1 + _bill2 + _bill3
print("Total Amount ", total_bill)
percentage = (total_bill/salary)*100
print("Percentage employee spent on shopping: ", percentage, "%")