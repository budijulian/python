#lists  = array yaitu untuk menampung data
data_list = [10,20,30,35,45,38,88,96]
subdata1  = data_list[5] # data ke-5
subdata2  = data_list[0:5] #data dari 0 to data 5
subdata3  = data_list[0:] #data ke 0 -> max data
a="aku adalah string"
data_list1 = [50,34,66,99,100]
#menambahkan lists
gabung = data_list +data_list1



#pemanggilan perintah
print(subdata1)
print(subdata2)
print(subdata3)

print(gabung)
print(5*"\n Next")

print(type(data_list)) #melihat tipe data
print(type(a)) #melihat tipe data

#mengubah isi list
data_list[1:3] =[55,90]
print(data_list[:])

#methods untuk list 
data_list1.append(65) # untuk menambah / add data ke list
print(data_list1)

#data_list = [10,20,30,35,45,38,88,96]
#function yang bisa digunalan didalam list
panjang_list = len(data_list)
print(panjang_list)

