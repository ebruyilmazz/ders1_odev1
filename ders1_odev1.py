#Pyton veri tipleri
#string metinsel veri tipi
metin="hello world"
print(metin)

#Sayısal veri tipleri : int = tam sayı veri, float = ondalıklı sayı 
sayi1=7
sayi2=12.5

#Boolean veri tipi : true7false çıktısı üreten veri tipi
print(sayi1 < sayi2) #true
print(sayi1 > sayi2) #false

# list = istenilen sayı da istenilen veri tiplerini içerir
list1=[7,"Elma,Cilek",12.5]
print(list1)
list2=[8,12.5,26]
print(list2)

fullName = "Ebru Yilmaz"
email = "ebruyilmaz@gmail.com"
password = 12345

fullName1 = input("Lütfen isim soyisim giriniz ")
email1 = input("Lütfen mail giriniz ")
password1 = input("Lütfen sifre giriniz ")

if email1 == email :
    print("Bu mail kayitli")
else :
    print("Kayit basariyla olusturuldu")
