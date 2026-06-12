# multilevel inheritance

class A:
    valA ="welcome to class A"

class B:
    valB ="welcome to class B"

class C(A,B):
    valC ="welcome to class C"

c1 =C()
print(c1.valA)
print(c1.valB)
print(c1.valC)
