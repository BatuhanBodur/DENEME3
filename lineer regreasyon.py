# import numpy as np
# import matplotlib.pyplot as plt

# #x değerleri aralığı
# x = np.linspace(0, 10, 100)

# #y değerleri: örneğin, sinüs fonksiyonu
# y = np.sin(x)

# #Grafik oluşturma
# plt.plot(x, y)

# #Grafik başlığı ve eksen etiketleri ekleme
# plt.title('Sinüs Fonksiyonu')
# plt.xlabel('x')
# plt.ylabel('sin(x)')

# #Grafiği gösterme
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# #Verileri tanımlama
# horsepower = np.array([200, 300, 350, 450]).reshape(-1, 1)  # Ev alanları m^2 cinsinden
# prices = np.array([500000, 700000, 890000, 1000000])  # Ev fiyatları TL cinsinden

# #Lineer regresyon modelini oluşturma
# model = LinearRegression()
# model.fit(horsepower, prices)

# #Modeli kullanarak 700 m^2 lik bir evin fiyatını tahmin etme
# horsepower_700 = np.array([[200]])
# predicted_price_700 = model.predict(horsepower_700)

# print("700 beygirlik bir arabanın tahmini fiyatı:", predicted_price_700[0], "TL")

# #Gerçek verileri ve regresyon çizgisini görselleştirme
# plt.scatter(horsepower, prices, color='blue', label='Gerçek Veriler')
# plt.plot(horsepower, model.predict(horsepower), color='red', label='Lineer Regresyon')
# plt.xlabel('Beygirgücü (HP)')
# plt.ylabel('Araç Fiyatı(TL)')
# plt.title('Beygirgücü ve Araç Fiyatı Arasındaki İlişki')
# plt.legend()
# plt.show()
