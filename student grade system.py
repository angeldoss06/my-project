english=int(input("enter english marks:"))
maths=int(input("enter maths marks:"))
tamil=int(input("enter tamil marks:"))
social=int(input("enter social marks:"))
science=int(input("enter science marks:"))
total=english+maths+tamil+social+science
average=total/5
print("you total is",total)
print("your average is",average)
if average>=90:
    print("your grade is A")
elif average>=80:
    print("your grade is B")
elif average>=70:
    print("your grade is C")
elif average>=60:
    print("your grade is D")
else:
    print("your grade is F")
