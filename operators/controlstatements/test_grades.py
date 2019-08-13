approved = True
maths = int(input("Enter a Maths grade:"))
physics = int(input("Enter a Physics grade:"))
chemistry = int(input("Enter a Chemistry grade:"))

if (maths > 100 or physics > 100 or chemistry > 100):
    print("The major value is 100")
    approved=False

if maths < 35:
    approved = False
elif physics < 35:    
    approved = False
elif chemistry < 35:
    approved = False
 
if(approved):
    average=(maths+physics+chemistry)/3;
    if average <= 59: grade="C"
    elif average <= 69: grade="B"
    else: grade="A"
    print("Average:", average, " Grade:",grade)
else:
    print("Not approved")    