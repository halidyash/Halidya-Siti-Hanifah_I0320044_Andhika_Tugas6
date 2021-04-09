#Soal No 2
#Program menghitung nilai rata-rata dari nilai yang diinput user

#input banyaknya nilai
bnilai = int(input("Total banyaknya nilai yang di input : "))
print()
data = []

#proses pengulangan saat input nilai
i = 1
while i <= bnilai:
    datanilai = int(input("Nilai %d : " %i))
    data.append(datanilai)
    i = i + 1
print()

#rumus menghitung nilai rata-rata
totalrataan = sum(data)/bnilai
print("Hasil nilai rata-rata dari nilai tersebut ialah : %d" %totalrataan)