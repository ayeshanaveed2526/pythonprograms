student1 ={
     "name": "Ayesha naveed",
     "Marks" : 90
}
student2={
     "name": "Anwashah zaheer khan mughal abbtabadi",
     "Marks" : 90
}
student3 ={
     "name": "kashish shapatar",
     "Marks" : 90
}

if student1["Marks"] >= 90 or student2["Marks"] >= 90 or student3["Marks"] >= 90:
    print("A+")
elif student1["Marks"] >= 80 or student2["Marks"] >= 80 or student3["Marks"] >= 80:
    print("A")
elif student1["Marks"] >= 70 or student2["Marks"] >= 70 or student3["Marks"] >= 70:
    print("B")
elif student1["Marks"] >= 60 or student2["Marks"] >= 60 or student3["Marks"] >= 60:
    print("C")
elif student1["Marks"] >= 50 or student2["Marks"] >= 50 or student3["Marks"] >= 50:
    print("F")
