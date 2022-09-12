maths = int(input("Math: "))
english = int(input("English: "))
bengali = int(input("Bengali: "))
history = int(input("history: "))
geo = int(input("Geography: "))
ls = int(input("Life Sc: "))
ps = int(input("Phi Sc: "))

av = (maths+english+bengali+history+geo+ls+ps)/7

if av >= 90:
   print("Result is A++")
elif av >= 80:
   print("Result is A+")
elif av >= 70:
   print("Result is A")
elif av >= 60:
   print("Result is B+")
elif av >= 50:
   print("Result is B")
elif av >= 40:
   print("Result is C")
else:
   print("Result is F")

