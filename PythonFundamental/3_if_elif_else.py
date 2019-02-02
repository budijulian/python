# operator if
harga = 600
if harga <=400:
    print("Belanja Anda Kurang",harga)
    
elif harga >=401 and harga <=1000:
    print("Belanja Anda Berlebih",harga)
else:
    print("Anda Royal Sekali")

print(20*"=")

nilai =80
if nilai is 60:
    print("Nilai Anda",nilai)
elif nilai is 70: # squal
    print("Nilai Anda",nilai)
elif nilai is not 70: #not squal
    print("Nilai Anda",nilai)
else:
    print("tidak ditemukan")

print(20*"=")
print("operator logika untuk list dan string")
print("\n")
kota =["jakarta","bali","lombok","padang","bandung","banten"]
tinggal ="bali"
huruf ="l"
# mencari string didalam lists
if tinggal in kota:
    print("anda dari indonesia, kota :",tinggal)
elif not tinggal in kota:
    print("anda bukan dari indonesia kota :",tinggal)
# mencari huruf di dalam string
if huruf in tinggal:
        print("karakter",huruf)
else:
    print("tidak ditemukan karakter")
