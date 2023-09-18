'''
LIST COMPREHENSIONS & PANDAS

TASK-4:
Görev 1: Seaborn kütüphanesi içerisinden 'Titanic' veri setini tanımlayınız.
Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.
Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
Görev 12: who değişkenini dataframe’den çıkarınız.
Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri
setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
'''

import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.columns
df.head()

# Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
male_count = df.groupby("sex").groups["male"].size
female_count = df.groupby("sex").groups["female"].size
print(f"male_count: {male_count} and female_cont: {female_count} \n")

male_passenger   = df[df['sex'] == 'male']
female_passenger = df[df['sex'] == 'female']


# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.



# Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.