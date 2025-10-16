
###############################################################
# RFM ile Müşteri Segmentasyonu (Customer Segmentation with RFM)
###############################################################

###############################################################
# İş Problemi (Business Problem)
###############################################################
# FLO müşterilerini segmentlere ayırıp bu segmentlere göre pazarlama stratejileri belirlemek istiyor.
# Buna yönelik olarak müşterilerin davranışları tanımlanacak ve bu davranış öbeklenmelerine göre gruplar oluşturulacak..

###############################################################
# Veri Seti Hikayesi
###############################################################

# Veri seti son alışverişlerini 2020 - 2021 yıllarında OmniChannel(hem online hem offline alışveriş yapan) olarak yapan müşterilerin geçmiş alışveriş davranışlarından
# elde edilen bilgilerden oluşmaktadır.

# master_id: Eşsiz müşteri numarası
# order_channel : Alışveriş yapılan platforma ait hangi kanalın kullanıldığı (Android, ios, Desktop, Mobile, Offline)
# last_order_channel : En son alışverişin yapıldığı kanal
# first_order_date : Müşterinin yaptığı ilk alışveriş tarihi
# last_order_date : Müşterinin yaptığı son alışveriş tarihi
# last_order_date_online : Muşterinin online platformda yaptığı son alışveriş tarihi
# last_order_date_offline : Muşterinin offline platformda yaptığı son alışveriş tarihi
# order_num_total_ever_online : Müşterinin online platformda yaptığı toplam alışveriş sayısı
# order_num_total_ever_offline : Müşterinin offline'da yaptığı toplam alışveriş sayısı
# customer_value_total_ever_offline : Müşterinin offline alışverişlerinde ödediği toplam ücret
# customer_value_total_ever_online : Müşterinin online alışverişlerinde ödediği toplam ücret
# interested_in_categories_12 : Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi

###############################################################
# GÖREV 1: Veriyi Anlama (Data Understanding) ve Hazırlama
###############################################################

import pandas as pd
import numpy as np
import seaborn as sns

pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
pd.set_option("display.float_format", lambda x: '%.3f' % x)

# 1. flo_data_20K.csv verisini okuyunuz.

df_ = pd.read_csv("flo_data_20k.csv")
df = df_.copy()
df.head()

# 2. Veri setinde

# a. İlk 10 gözlem,
df.head(10)
# b. Değişken isimleri,
df.columns
# c. Betimsel istatistik,
df.describe().T
# d. Boş değer,
df.isnull().sum()
# e. Değişken tipleri, incelemesi yapınız.
df.info()

#3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir. Herbir müşterinin toplam
# alışveriş sayısı ve harcaması için yeni değişkenler oluşturun.

df["total_order_number"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
df.groupby(["master_id"]).agg({"total_order_number": "sum"})
df["total_customer_value"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]
df.head()

# 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.

print(df.dtypes)

#1. yol

date = ["first_order_date", "last_order_date", "last_order_date_online", "last_order_date_offline"]
def objtodate():
    df[x] = pd.to_datetime(df[x], errors='coerce')

for x in date:
    objtodate()

print(df.dtypes)

#2. yol

for col in df.columns:
    if "date" in col:
        df[col] = pd.to_datetime(df[col])

# 5. Alışveriş kanallarındaki müşteri sayısının, ortalama alınan ürün sayısının ve ortalama harcamaların dağılımına bakınız.

df.groupby(["order_channel"]).agg({"master_id": "count", "total_order_number": "mean", "total_customer_value": "mean"})

# 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.

df.sort_values(by = "total_customer_value", ascending=False).head(10)

# 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.

df.sort_values(by = "total_order_number", ascending=False).head(10)

# 8. Veri ön hazırlık sürecini fonksiyonlaştırınız.

def veri_on_hazırlık(dataframe, csv = False):
    import pandas as pd
    import numpy as np
    import seaborn as sns

    pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_rows', None)
    pd.set_option("display.float_format", lambda x: '%.4f' % x)

    # 1. flo_data_20K.csv verisini okuyunuz.

    df_ = pd.read_csv("flo_data_20k.csv")
    df = df_.copy()
    df.head()

    # 2. Veri setinde

    # a. İlk 10 gözlem,
    df.head(10)
    # b. Değişken isimleri,
    df.columns
    # c. Betimsel istatistik,
    df.describe().T
    # d. Boş değer,
    df.isnull().sum()
    # e. Değişken tipleri, incelemesi yapınız.
    df.info()

    # 3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir. Herbir müşterinin toplam
    # alışveriş sayısı ve harcaması için yeni değişkenler oluşturun.

    df["total_order_number"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
    df.groupby(["master_id"]).agg({"total_order_number": "sum"})
    df["total_customer_value"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]
    df.head()

    # 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.

    #1.yol
    # df["last_order_date"] = df["last_order_date"].apply(pd.to_datetime)

    #2.yol
    print(df.dtypes)
    date = ["first_order_date", "last_order_date", "last_order_date_online", "last_order_date_offline"]

    def objtodate():
        df[x] = pd.to_datetime(df[x], errors='coerce')

    for x in date:
        objtodate()

    print(df.dtypes)

    # 5. Alışveriş kanallarındaki müşteri sayısının, ortalama alınan ürün sayısının ve ortalama harcamaların dağılımına bakınız.

    df.groupby(["order_channel"]).agg(
        {"order_channel": "count", "total_order_number": "mean", "total_customer_value": "mean"})

    # 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.

    df.sort_values(by="total_customer_value", ascending=False).head(10)

    # 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.

    df.sort_values(by="total_order_number", ascending=False).head(10)

    return df

###############################################################
# GÖREV 2: RFM Metriklerinin Hesaplanması
###############################################################

# Veri setindeki en son alışverişin yapıldığı tarihten 2 gün sonrasını analiz tarihi

import datetime as dt

df.sort_values(by = ["last_order_date"], ascending=False).head()
today_date = dt.datetime(2021, 6, 1 )
type(today_date)

# customer_id, recency, frequnecy ve monetary değerlerinin yer aldığı yeni bir rfm dataframe

rfm = df.groupby(["master_id"]).agg({"last_order_date": lambda last_order_date: (today_date - last_order_date.max()).days,
                                      "total_order_number": lambda total_order_number: total_order_number.sum(),
                                      "total_customer_value": lambda total_customer_value: total_customer_value.sum()
                                     })

rfm.columns = ["recency", "frequency", "monetary"]
rfm.head()
rfm.describe().T

###############################################################
# GÖREV 3: RF ve RFM Skorlarının Hesaplanması (Calculating RF and RFM Scores)
###############################################################

#  Recency, Frequency ve Monetary metriklerini qcut yardımı ile 1-5 arasında skorlara çevrilmesi ve
# Bu skorları recency_score, frequency_score ve monetary_score olarak kaydedilmesi

rfm["recency_score"] = pd.qcut(rfm["recency"], 5, labels = [5, 4, 3, 2, 1])
rfm["frequency_score"] = pd.qcut(rfm["frequency"].rank(method = "first"), 5, labels = [1, 2, 3, 4, 5])
rfm["monetary_score"] = pd.qcut(rfm["monetary"], 5, labels = [5, 4, 3, 2, 1])

# recency_score ve frequency_score’u tek bir değişken olarak ifade edilmesi ve RF_SCORE olarak kaydedilmesi

rfm["RFM_SCORE"] = (rfm["recency_score"].astype(str)) + (rfm["frequency_score"].astype(str)) + (rfm["monetary_score"].astype(str))
rfm["RF_SCORE"] = (rfm["recency_score"].astype(str)) + (rfm["frequency_score"].astype(str))
rfm.sort_values(by = "RF_SCORE", ascending = False).head(10)

###############################################################
# GÖREV 4: RF Skorlarının Segment Olarak Tanımlanması
###############################################################

# Oluşturulan RFM skorların daha açıklanabilir olması için segment tanımlama ve  tanımlanan seg_map yardımı ile RF_SCORE'u segmentlere çevirme

seg_map = {r"[1-2][1-2]": "hibernating",
           r"[1-2][3-4]": "at_risk",
           r"[1-2]5": "cant_loose",
           r"3[1-2]": "about_to_sleep",
           r"33": "need_attention",
           r"[3-4][4-5]": "loyal_customers",
           r"41": "promising",
           r"51": "new_customer",
           r"[4-5][2-3]": "potential_loyalist",
           r"5[4-5]": "champions"
           }

rfm["segment"] = rfm["RF_SCORE"].replace(seg_map, regex=True)
rfm.head()

###############################################################
# GÖREV 5: Aksiyon zamanı!
###############################################################

# 1. Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.

rfm[["segment", "recency", "frequency", "monetary"]].groupby("segment").agg(["mean", "count"])

# 2. RFM analizi yardımı ile 2 case için ilgili profildeki müşterileri bulunuz ve müşteri id'lerini csv ye kaydediniz.

# a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde. Bu nedenle markanın
# tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak iletişime geçeilmek isteniliyor. Bu müşterilerin sadık  ve
# kadın kategorisinden alışveriş yapan kişiler olması planlandı. Müşterilerin id numaralarını csv dosyasına yeni_marka_hedef_müşteri_id.cvs
# olarak kaydediniz.

target_segments_customer_ids = rfm[rfm["segment"].isin(["champions","loyal_customers"])]["customer_id"]
cust_ids = df[(df["master_id"].isin(target_segments_customer_ids)) &(df["interested_in_categories_12"].str.contains("KADIN"))]["master_id"]
cust_ids.to_csv("yeni_marka_hedef_müşteri_id.csv", index=False)

# b. Erkek ve Çoçuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte iyi müşterilerden olan ama uzun süredir
# alışveriş yapmayan ve yeni gelen müşteriler özel olarak hedef alınmak isteniliyor. Uygun profildeki müşterilerin id'lerini csv dosyasına indirim_hedef_müşteri_ids.csv
# olarak kaydediniz.

df2 = rfm.merge(df, how = "left", on = "master_id")
df2.head()

mask_segment = df2["segment"].isin(["cant_loose", "new_customers"])
mask_cats = df2["interested_in_categories_12"].str.contains(r"\b(?:ERKEK|COCUK)\b", na=False)
target_ids = (
    df2.loc[mask_segment & mask_cats, "master_id"]
       .dropna()
       .drop_duplicates()
)
#CSV’ye yaz
target_ids.to_frame(name="master_id").to_csv("indirim_hedef_müşteri_ids.csv", index=False)
