# MapReduce Kelime Sayımı Projesi 📊

Bu proje, **MapReduce** paradigmasını kullanarak büyük metin verilerini işleyen bir Python uygulamasıdır. Uygulama, çeşitli metin dosyalarından kelimeleri okur, her kelimenin kaç kez geçtiğini sayar ve sonuçları dosyalar halinde kaydeder. Bu, büyük veri işleme ve paralel hesaplama gibi konularda temel bir örnek teşkil etmektedir. 🚀

## Proje Özeti 📜

MapReduce, dağıtık sistemlerde büyük veri kümeleri üzerinde işlem yapmak için yaygın olarak kullanılan bir yöntemdir. Bu proje, **Map** ve **Reduce** adımlarını simüle eder ve aşağıdaki işlemleri gerçekleştirir:

1. **Map** 🗺️: Her kelimeyi tespit eder ve her birinin geçişini bir `1` ile işaretler.
2. **Shuffle** 🔀: Aynı kelimeler gruplanarak, her kelime için biriktirilmiş değerler toplanır.
3. **Reduce** ➗: Aynı kelimenin tüm `1` değerlerinin toplamını hesaplayarak kelimenin sayısını belirler.

## Kullanılan Teknolojiler 🛠️

- **Python 3.13** 🐍: Python programlama dili kullanılarak geliştirilmiştir.
- **Faker** 🎲: Gerçekçi rastgele metin verisi oluşturmak için kullanılan bir Python kütüphanesidir.

## Gereksinimler 📋

Projenin düzgün çalışabilmesi için aşağıdaki Python kütüphanelerine ihtiyaç duyulmaktadır:

- `Faker`: Rastgele cümleler ve metinler üretmek için.
## MapReduce İşlemi
1. Map İşlemi:
MapReduce sürecinin ilk adımıdır. Bu aşamada, her kelime 1 ile eşleştirilir. Yani, her kelimenin her görünümü, bulunduğu dosyadaki her bir kez için bir 1 olarak sayılır.

2. Shuffle İşlemi:
Shuffle, aynı kelimeleri gruplar ve her kelime için 1 değerlerini toplar. Örneğin, "apple" kelimesi dosyalarda 3 kez geçiyorsa, Shuffle sonucunda şöyle bir yapı oluşur:



apple: 1
apple: 1
apple: 1

3. Reduce İşlemi:
Reduce adımında, her kelime için 1 değerleri toplanarak kelimenin toplam sayısı hesaplanır.

### Gereksinimlerin Yüklenmesi

Proje için gerekli olan tüm kütüphaneleri yüklemek için şu komutu kullanabilirsiniz:

```bash
pip3 install -r requirements.txt

