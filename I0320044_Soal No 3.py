#Soal No 3
#Program menggunakan perintah pengulangan dan fungsi range ()

# menentukan bilangan prima dari 10 sampai 25
for num in range(10, 25):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "bukan prima")
                break
        else:
            print(num, "adalah bilangan prima")