print("Program Python Menghitung Nilai Rata-Rata")
print()
x = 0
y = 0
z = 1

while (z == 1):
    r = input("Masukkan nilai = ")
    
    b = x
    t = b + x
    y += 1
    
    if (r == "A"):
        x = 4.00
        print("Nilai = ",x)
    elif (r == "A-"):
        x = 3.75
        print("Nilai = ",x)
    elif (r == "B+"):
        x = 3.50
        print("Nilai = ",x)
    elif (r == "B"):
        x = 3.00
        print("Nilai = ",x)
    elif (r == "B-"):
        x = 2.75
        print("Nilai = ",x)
    elif (r == "C+"):
        x = 2.50
        print("Nilai = ",x)
    elif (r == "C"):
        x = 2.00
        print("Nilai = ",x)
    elif (r == "C-"):
        x = 1.75
        print("Nilai = ",x)
    elif (r == "D"):
        x = 1.50
        print("Nilai = ",x)
    elif (r == "E"):
        x = 1.25
        print("Nilai = ",x)
    else :
        z = 0
        
A = t/(y-1)
print("Rata-ratanya adalah = ", A)