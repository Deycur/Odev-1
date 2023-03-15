students = ["Eyo Şen","Ahmet Aslan"]
print(students)
studentsNameSurname = input("Eklemek istediğiniz Öğrenci adını ve soyadını giriniz: ")
students.append(studentsNameSurname)
print(students)
# #Listeye Öğrenci ekleme


delateStudent = input("Silmek İstediğiniz Öğrenci adını ve soyadını giriniz: ")
students.remove(delateStudent)
print(students)
# #Listeye Öğrenci Silme

studensNumber = int(input("Kaçtane öğrenci eklemek istiyorsunuz ? : "))
students = ["Eyo Şen","Ahmet Aslan"]
i = 0
while i < studensNumber:
    newStudent = input("Eklemek İstediğiniz Örenci Adısoyadı: ")
    students.append(newStudent)
    i +=1
print(students)
#Birden fazla öğrenci ekleme

for student in students:
    print(student)
# Tüm öğrencileri tek tek yazdırma

i=0
while i< len (students):
        print( str(i) + ")" + students[i])
        i+=1

#Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan;

dleteStudensNumber = int(input("Kaçtane öğrenci silmek istiyorsunuz ? : "))
i = 0
while i < dleteStudensNumber:
    newDeleteStudent = input("Silmek İstediğiniz Örenci Adısoyadı: ")
    students.remove(newDeleteStudent)
    i +=1
print(students)
#Listeden Birden Fazla Öğrenci Silme