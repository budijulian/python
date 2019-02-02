# merupakan looping di dalam lists/ array
kota =["jakarta","bali","lombok","padang","bandung","banten"]
#cara lain menampilkan data di lists
for a in kota:
    print(a)
    print(len(a)) # mencari panjang karakter
#string sebagai karakter
saya = "Budi Julian"
for b in saya:
    print(b+"")
kota2 =["LOMBOK","ACEH","SUMATRA","JAWA"]
c = [kota,kota2] # gabungkan 2 lists
for d in c:
    print(d)

print(20*"=")    
#for - else
angka =8
for e in range(0,10): # LOOP nilai e
   print(e)
   #if -else
   if e is 5: # operator if didalam for
        print("angka ditemukan",e)
        break
   else:
        print("tidak ditemukan didalam for")
else:
    pass
   

