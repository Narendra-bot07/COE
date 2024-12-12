project = int(input("Enter the project marks: "))
internal = int(input("Enter the internal marks: "))
external = int(input("Enter the external marks: "))
if project<50:
    print("Failed in project\nscore ",project)
if internal < 50:
    print("Failed in internal \n score ", internal)
if external < 50:
    print("Failed in external \n score ", external)
else:
    project = 0.7*project
    internal = 0.1*internal
    external = 0.2*external
    total = project + internal + external
    if total>90:
        print("A grade")
    elif total>=80:
        print("B grade")
    elif total>=50:
        print("C grade")

