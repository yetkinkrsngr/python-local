# tek satır yapılı yorum satırı
"""
birden fazla yorum yapmamızı 
sağlayan yorum satırı
"""
# numeric veri yapıları

x = 4
y = 4.9
d = 4j
"""
yukarıdaki veri türleri 
1.int
2.float
3.complex olarak verildi 
buradaki nokta ise 2. floatda nokta kullanmamız 
3.satırda j olarak belirmemiz
"""
print(type(x))
print(type(y))
print(type(d))

# string metinsel veri türleri
txt = "Merhaba Dünya "
print(type(txt))
print(txt)


# birden fazla değeri birden fazla değişkene atama
x, y, z = "cherry", "banana", "lemon"
print(x)
print(y)
print(z)


# yada birden dğişken tek değer atama
x = y = "banana"
print(x)
print(y)

# yada koleksion varsa buna ek olarak birden fazla değişkene atana bilir
fruits = ["apple", "lemon"]
x, y = fruits
print(x)
print(y)


"""
yukarıda yazdığımız tüm değişkenler hepsi globaldedir her yerden ulaşabilriz lakin if else yapısı
içinde yada herhangi bir fonsiyonda yazdığımız değişkenlere ulaşmak için global key'i kullanmayız
"""


def myfunc():
    local = "bu bir local değişkendir"
    global lol
    lol = "buda globala alacağımız değişkendir"


myfunc()
print(lol)
# print(local) name 'local' is not defined


# tip döünüşümü farklı tiplerdeki veriler aynı metotda çağrılamaz örn str int
derece = 5
metin = "bugun hava "
metin2 = " derece"
print(metin+str(derece)+metin2)
# print(metin+derece) TypeError hatası


x = 2
print(float(x))
print(x)
