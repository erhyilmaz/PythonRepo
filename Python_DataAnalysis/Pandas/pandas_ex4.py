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
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("titanic")
df.info()
df.describe()
df.columns
df.head()

## drop unnecessary columns, these columns won't be useful in analysis and prediction
# df_new = df.drop(['PassengerId', 'Name', 'Cabin', 'Ticket'], axis=1)


# Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
male_count = df.groupby("sex").groups["male"].size
female_count = df.groupby("sex").groups["female"].size
print(f"male_count: {male_count} and female_cont: {female_count} \n")

male_passenger = df[df['sex'] == 'male']
female_passenger = df[df['sex'] == 'female']
kid_passenger = df[df['age'] < 16]
male_kid_passenger = kid_passenger[kid_passenger['sex'] == 'male']
female_kid_passenger = kid_passenger[kid_passenger['sex'] == 'female']
# Creating adult male and female dataframes by dropping kid passengers
adult_male_passenger = male_passenger.drop(male_kid_passenger.index[:])
adult_female_passenger = female_passenger.drop(female_kid_passenger.index[:])

print('Number of male passengers:', len(df.groupby('sex').groups['male']))
print('Number of female passengers:', len(df.groupby('sex').groups['female']))
print('Number of kid passengers:', df['age'].apply(lambda x: x < 16).sum())

if 0:
    # Visualization of percentages of passengers by sex on pie chart
    x = [len(male_passenger), len(female_passenger)]
    label = ['Male', 'Female']
    plt.pie(x, labels = label, autopct = '%1.01f%%')
    plt.title('Distribution of passengers by sex')
    plt.show()

    # We can also diversify age groups by defining a function:
    def age_distribution(x_in):
        if x_in >= 0 and x_in < 16:
            return 'Child'
        elif x_in >= 16 and x_in <= 24:
            return 'Young'
        else:
            return 'Adult'


    #Visualization of percentages of passengers by age
    df['age'].apply(age_distribution).value_counts().plot(kind='pie', autopct='%1.0f%%')
    plt.title('Distribution of passengers by age')
    plt.show()

    df['pclass'].value_counts().plot(kind='barh', color='green', figsize=[16, 4])
    plt.xlabel('Frequency')
    plt.ylabel('Passenger class')
    plt.show()

    #Creating dataframes by passenger class
    #first_class_passenger = df[df['pclass'] == [1]]
    #second_class_passenger = df[df['pclass'] == [2]]
    #third_class_passenger = df[df['pclass'] == [3]]

    df['embarked'].describe()

    #Filling the two missing values in 'Embarked' with the most occurred value, which is "S"
    df['embarked'] = df['embarked'].fillna('S')

    #Visualization of number of passengers by embarking ports
    df['embarked'].value_counts().plot(kind='bar')
    plt.title('Embarking ports')
    plt.ylabel('Frequency')
    plt.xlabel('S=Southampton, C=Cherbourg, Q=Queenstown')
    plt.show()

    #Number of surviveds and not-surviveds
    df['survived'].value_counts()

    df['survived'].value_counts().plot(kind='bar', title='Surviving')
    plt.xlabel('0= Not-survived  1= Survived')
    plt.ylabel('Frequency')
    plt.show()

    #Number of survivings by sex
    df.groupby('sex')['survived'].value_counts()
    #Visualization of survivings by sex
    df.groupby('sex')['survived'].value_counts().plot(kind='bar', stacked=True, colormap='winter')
    plt.show()

    #Better visualization of survivings by sex
    sex_survived = df.groupby(['sex', 'survived'])
    sex_survived.size().unstack().plot(kind='bar', stacked=True, colormap='winter')
    plt.ylabel('Frequency')
    plt.title('Survivings by sex')
    plt.show()

print('Mean of survived adult female passengers:', adult_female_passenger['survived'].mean())
print('Mean of survived adult male passengers:', adult_male_passenger['survived'].mean())

#Usage of size(),unstack() while examining survivings by passenger class
class_survived = df.groupby(['pclass', 'survived'])
#size() - to count number of rows in each grouping
print(class_survived.size())

#unstack() - to convert results into a more readable format.
print(class_survived.size().unstack())

#Visualization of survivings by passenger class
class_survived.size().unstack().plot(kind='bar', stacked=True, colormap='autumn')
plt.xlabel('1st = Upper,   2nd = Middle,   3rd = Lower')
plt.ylabel('Frequency')
plt.title('Survivings by passenger class')
plt.show()

#Numbers of survived/not survived passengers by sex and passenger class
print('Surviving numbers of male passengers by passenger class: \n', male_passenger.groupby(['pclass', 'survived']).size().unstack())
print('Surviving numbers of female passengers by passenger class:\n', female_passenger.groupby(['pclass', 'survived']).size().unstack())

#Visualization of male and female survivings by passenger class
fig, axes = plt.subplots(nrows=2, ncols=1)
male_passenger.groupby(['pclass','survived']).size().unstack().plot(kind='bar', title='Surviving of male passengers by class',
                                                                    stacked=True, colormap='summer', ax=axes[0])
female_passenger.groupby(['pclass','survived']).size().unstack().plot(kind='bar', title='Surviving of female passengers by class',
                                                                      stacked=True, colormap='summer', ax=axes[1])
plt.tight_layout()
plt.show()


#Fares varies widely. Therefore I used pandas.qcut for discretizing fares into equal buckets.
#Firstly, filling missing values of 'Fare'
df['fare'].fillna(df['fare'].dropna().median(), inplace=True)

#Discretizing fares of passengers in 4 equal buckets with .qcut
df['fareBand'] = pd.qcut(df['fare'], 4)
print(df['fareBand'].value_counts().sort_values(ascending= False))

#Mean of survived passengers by fares
print(df[['fareBand', 'survived']].groupby(['fareBand'], as_index=False).mean().sort_values(by='fareBand', ascending=True))



# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.



# Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.