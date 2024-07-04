import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import turtle
# x=np.array([[1,2,3],[3,4,5]])
# print(x)
# print(type(x))
# print(x.shape)#satır,sütun sayısını döner.
# print(x.ndim)#Kaç boyutlu olduğunu döner.
# print(x.size)#Eleman sayısını döner.
# print(x.dtype)#Veri tipini döner
# print(x.nbytes)#Kaç bytelık alan kapladığını döner.

# x=np.array([[[1,2,3],[2,2,2]],[[5,5,6],[7,9,8]]])
# print(x)
# print(type(x))
# print(x.shape)#satır,sütun sayısını döner.
# print(x.ndim)#Kaç boyutlu olduğunu döner.
# print(x.size)#Eleman sayısını döner.
# print(x.dtype)#Veri tipini döner
# print(x.nbytes)#Kaç bytelık alan kapladığını döner.


# x=np.array([1,2,3,4,5],dtype=complex)#dtype ile arrayin veri tipi değiştirilebilir.
# print(x)
# print(x.dtype)

# x=np.array([x],dtype=int)
# print(x.dtype)
# x=np.array([1,2,3,4,5],dtype=complex)
# x=x.astype(np.float16)#verinin tipini değiştirir.
# print(x.dtype)

# x=np.sqrt(np.array([2,4,9]),dtype=complex)#sqrt arrayin karekökünü alır.
# print(x)
# print(x.dtype)
# print(x.real)#karmaşık sayıların reel kısmını gösterir.
# print(x.imag)#kompleks sayıların karmaşık kısmını gösterir.
# np.save("kaydetmek istenilen isim",x)#arrayi kaydeder.
# y=np.load("ndarray deneme.npy")#arrayi yükler
# print(y)


#np.zeros(x,y)--->>>Tüm elemanları sıfır olan bir array oluşturur.X satır sayısını, y sütun sayısını verir.
#np.ones(x,y)--->>>Tüm elemanları bir olan bir array oluşturur.X satır sayısını, y sütun sayısını verir.
#np.full--->>>Sadece verilen değerlerden oluşan bir array oluşturur.

# x=np.zeros((2,3))
# print(x)

# x=np.ones((2,3))
# print(x)

# x=np.full((3,3),4)
# print(x)

# x=10*np.ones((2,3))
# y=10+np.zeros((2,3))
# print(x)
# print(y)


#np.empty()--->>>Boş bir array oluşturur.
#np.fill()--->>>Arrayi istediğimiz değerle doldurur.

# x=np.empty((2,3))
# x.fill(5)
# print(x)


#np.eye(x,k)--->>>Birim matris oluşurur.X kaç satır ve sütundan oluşacağını belirtir.k parametresi köşegeni ileri veya geri almak için kullanılır.
# x=np.eye(5)
# print(x)


#np.diag--->>>Köşegene sırasıyla istediğimiz değeri yerleştirir.
# x=np.diag((4,7,5))
# print(x)


#np.arange(x,y,z)--->>>X başlangıç noktasını belirler.Y bitiş noktasıdır ve dahil edilmez.Z artış miktarıdır.
# x=np.arange(3,10,3)
# print(x)


# np.linspace(x,y,z)--->>>X başlangıç noktasıdır.Y bitiş noktasıdır ve dahil edilir.Z X-Y aralığındaki almak istediğimiz veri sayısıdır.
# x=np.linspace(5,20,8)
# print(x)


#x.np.reshape(4,5)--->>>X şeklini değiştirmek istediğimiz arrayin adıdır.(4,5) arrayin yeni şeklidir , 4 satır ve 5 sütundan oluşur.
# x=np.arange(32)
# y=x.reshape((2,4,4))
# print(y)


# x=np.arange(32).reshape(2,4,4)
# print(x)


#np.random.random(x,y)--->>>X satır sayısını y sütun sayısını verir.0,1 aralığında rastgele sayılar  oluşturur.
# x=np.random.random((2,3))
# print(x)


#np.random.randint(x,y,size=(a,b))--->>>X başlangıç noktasını , y bitiş noktasını verir.(a,b) şeklini verir.3 ve 12 arasında random integer değerler atanır.
# x=np.random.randint(1,15,size=(2,3))
# print(x)


#np.delete(array adı,silinecek verinin indeksi)--->>>Veriyi indeksten siler.
# x=np.arange(3,13,3).reshape(2,2)
# x=np.delete(x,[[1,0],[0,0]])
# print(x)


#axis=0 satır ; axis=1 sütun
# x=np.arange(16).reshape(4,4)
# x=np.delete(x,1,axis=0)#Birinci indeksteki satırı tamamen siler
# print(x)
# y=np.arange(16).reshape(4,4)
# y=np.delete(y,1,axis=1)#Birinci indeksteki sütunu tamamen siler.
# print(y)


#np.append(x,y)--->>>X eklemek istediğimiz arrayin adı, y eklemek istediğimiz veridir.Birden fazla veri eklenmek istenirse köşeli parantez kullanılmalıdır.
# x=np.arange(10)
# x=np.append(x,[10,11])
# print(x)


# x=np.arange(9).reshape(3,3)
# x=np.append(x,[[10,20,30]],axis=0)
# print(x)


# x=np.arange(9).reshape(3,3)
# x=np.append(x,[[10],[20],[30]],axis=1)
# print(x)


#x=np.insert(array adı,eklenecek indeks,eklenecek sayı,eğer çok boyutluysa eklenecek axis)--->>>Append den farkı konuma ekleme yapmasdır.
# x=np.arange(5)
# x=np.insert(x,1,12)
# print(x)


#sütuna ekleme yapar.
# x=np.arange(9).reshape(3,3)
# x=np.insert(x,0,[10,20,30],axis=1)
# print(x)


#satıra ekleme yapar
# x=np.arange(9).reshape(3,3)
# x=np.insert(x,0,[10,20,30],axis=0)
# print(x)


#np.vstack((x,y))--->>>x'i y'nin üzerine ekler.vstack=vertical stack.
# x=np.arange(9).reshape(3,3)
# y=np.arange(3)
# z=np.vstack((y,x))
# print(z)


#np.hstack((x,y))--->x'i y'nin yanına yerleştirir.hstack=horizontal stack.
# x=np.arange(8)
# y=np.arange(3)
# z=np.hstack((x,y))
# print(z)


# x=np.arange(10)
# print(x[2:6])#x'in 2. indeksteki elemanından başlayarak 6. elemana kadar yazdırır ama 6'ı dahil etmez.


# x=np.arange(25).reshape(5,5)
# print(x[0:3,0:4])#x matrisinin x eksenini 0 dan 3 e kadar y ekseninide 0 dan 4 e kadar yazdırır ve 3 e 4 lük bir matris haline getirir.

# x=np.arange(9).reshape(3,3)
# y=np.copy(x[0:2,1:3])#Belirtilen arrayi kopyalar.
# print(y)


#FANCY İNDEXİNG--->>>Başka bir arrayla oluşturlan arrayler birbirinden etkilenmez.
# x=np.arange(25).reshape(5,5)
# y=np.array([1,2])
# print(x[:,y])#Başka bir arrayi satır ve sütun belirtmek  için kullanabiliriz.


#BOOLEAN İNDEXİNG
# x=np.arange(11)
# print(x[(x%2==0)])#X arrayinde 2 ile bölümünden 0 kalan sayıları bastırır.

# x=np.random.randint(10,size=10)
# y=np.random.randint(10,size=10)
# print(x)
# print(y)
# print(x>y)


#Maskeleme--->>>Sadece koşulun sağlandığı veriler maskelemeye atanır ve True ya da False döner.Sayı dönmesi için x i indeksleriz.
# x=np.linspace(1,21,11)
# print(x)
# maskeleme=(x%3==0)
# print(x[maskeleme])



#np.intersect1d(x,y)--->>>iki arrayi karşılaştırır ve ortak olan elemanları da bir array şeklinde dönderir.Küçükten büyüğe sıralanır.
# x=np.random.randint(1,15,10)
# y=np.random.randint(1,15,10)
# print(x)
# print(y)
# print(np.intersect1d(x,y))


# #np.setdiff1d(x,y)--->>>İki arrayi karşılaştırıp x de olup y de olmayan elemanları bastırır.Küçükten büyüğe sıralanır.
# x=np.random.randint(1,15,10)
# y=np.random.randint(1,15,10)
# print(x)
# print(y)
# print(np.setdiff1d(x,y))
# print(np.setdiff1d(y,x))


# #np.union1d(x,y)--->>>İki arrayin birleşim kümesini döner.Aynı elemanlar iki defa yazılmaz.Küçükten büyüğe sıralanır.
# x=np.random.randint(1,15,10)
# y=np.random.randint(1,15,10)
# print(x)
# print(y)
# print(np.union1d(x,y))


#np.in1d(x,y)--->>>X de olan elemanları sırayla gezip Y de var mı diye bakar varsa True yoksa False döner.
# x=np.random.randint(1,15,10)
# y=np.random.randint(1,15,10)
# print(x)
# print(y)
# print(np.in1d(x,y))


#np.unique--->>>Birbirinden farklı her elemanı bir kere olacak şekilde yazdırır. Küçükten büyüğe sıralar.
# x=np.random.randint(1,15,10)
# print(np.unique(x))


#np.sort(x)--->>>np.sort anlık olarak küçükten büyüğe sıralar ancak bellekte kaydetmez.
# x=np.random.randint(1,15,10)
# print(x)
# print(np.sort(x))
# print(x)


#x.sort--->>>Sortingin metod olarak kullanılmasıdır .Küçükten büyüğe sıralar ve bellekte kaydeder.
# x=np.random.randint(1,15,10)
# print(x)
# x.sort()
# print(x)


# x=np.random.randint(1,10,size=(3,3))
# print(x)
# print()
# print(np.sort(x,axis=0))#Sütunlara göre küçükten büyüğe sıralar.


# x=np.random.randint(1,10,size=(3,3))
# print(x)
# print()
# print(np.sort(x,axis=1))


#////////////////////////////////ARİTMETİK İŞLEMLER///////////////////////////
#TOPLAMA
#np.add(x,y)--->>>X ve Y i toplar.
# x=np.array([3,5,4,8,6,4,12])
# y=np.array([1,5,6,8,2,3,19])
# print(x+y)
# print(np.add(x,y))


#ÇIKARMA
#np.subtract(x,y)--->>>X den Y i çıkarır.
# x=np.array([3,5,4,8,6,4,12])
# y=np.array([1,5,6,8,2,3,19])
# print(x-y)
# print(np.subtract(x,y))


#ÇARPMA
#np.multiply(x,y)--->>>X ve Y i çarpar.
# x=np.array([3,5,4,8,6,4,12])
# y=np.array([1,5,6,8,2,3,19])
# print(x*y)
# print(np.multiply(x,y))


#BÖLME
#np.divide(x,y)--->>>X i Y e böler.
# x=np.array([3,5,4,8,6,4,12])
# y=np.array([1,5,6,8,2,3,19])
# print(x/y)
# print(np.divide(x,y))


#Arrayin her elemanını sabit sayıyla çarpma
# x=np.array([3,5,4,8,6,4,12])
# print(x)
# print(x+3)
# print(x-3)
# print(x*3)
# print(x/3)


# Importing necessary libraries
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# Generating sample data
# np.random.seed(0)
# X = 2 * np.random.rand(100, 1)  # Generate 100 random values between 0 and 2
# y = 3 * X + 4 + np.random.randn(100, 1)  # Generate y values with noise

# Creating a linear regression model
# model = LinearRegression()

# Training the model
# model.fit(X, y)

# Making predictions
# X_new = np.array([[0], [2]])  # New data points for prediction
# y_pred = model.predict(X_new)

# Plotting the data and the linear regression line
# plt.scatter(X, y, label='Original data')
# plt.plot(X_new, y_pred, 'r-', label='Linear Regression Line')
# plt.xlabel('X')
# plt.ylabel('y')
# plt.title('Linear Regression Example')
# plt.legend()
# plt.show()

#Eşitlik sorugular.
# x=np.random.randint(1,15,10)
# print(x)
# y=np.random.randint(1,15,10)
# print(y)
# print(x==y)

#np.array.equal--->>> arraylerin eşitliğini sorgular.
# a=np.array([1,2,3])
# b=np.array([1,2,3])
# print(np.array_equal(a,b))


#x=np.array([9,16,64,81])
#print(np.sqrt(x))#arrayin elemanlarının kökünü alır.
# print(np.power(x,3))#x'in küpünü alır.ikinci parametre üs değeridir.
# print(np.exp(x))#x in doğal logaritmasını alır.


t=turtle.Turtle()
turtle.bgcolor("black")
t.speed(5)
colors=["red","yellow","blue","green","purple","orange"]
for i in range(300):
    t.pencolor(colors[i%6])
    t.forward(i*2)
    t.right(61)
turtle.done()    