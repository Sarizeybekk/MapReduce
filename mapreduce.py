from faker import Faker
from functools import reduce
import random

fake = Faker()

# Dosya isimlerini belirle
file_names = [f"file_{i}.txt" for i in range(1, 6)]

# Dosyaları oluştur ve her birine rastgele metin yaz
for file_name in file_names:
    with open(file_name, "w") as file:
        for _ in range(10):  # Her dosyaya 10 rastgele cümle ekleyelim
            file.write(fake.sentence() + '\n')

# Tüm dosyaları birleştirip kelimeleri sayma işlemi
def map_reduce(files):
    words = []
    
    # Dosyaları oku ve kelimeleri listele
    for file_name in files:
        with open(file_name, 'r') as file:
            content = file.read()
            words.extend(content.split())
    
    # Map İşlemi (Her kelimeyi "1" ile eşleştir)
    mapped = list(map(lambda word: (word.lower().strip(".,!?"), 1), words))
    
    # Shuffle İşlemi (Kelime gruplama ve her 1 değerini ayrı yazma)
    word_groups = []
    for word, count in mapped:
        word_groups.append((word, 1))  # Burada her kelimeyi 1 ile ekliyoruz
    
    return word_groups

# Dosyalarla MapReduce işlemi yap
mapped_words = map_reduce(file_names)

# Shuffle işlemi: Aynı kelimeleri gruplayarak 1'lik değerlerini toplama
# Kelimeleri gruplayacağız, ama burada her 1'lik değeri ayrı tutacağız (yani apple: 1, apple: 1, apple: 1)
shuffled_word_count = {}

for word, count in mapped_words:
    if word not in shuffled_word_count:
        shuffled_word_count[word] = []
    shuffled_word_count[word].append(count)

# Reduce işlemi: Aynı kelimenin "1" değerlerini toplayacağız
def reduce_func(acc, word_data):
    word, counts = word_data
    acc[word] = sum(counts)  # Aynı kelimelerin "1" değerlerini topluyoruz
    return acc

# Reduce işleminden sonra toplam sayıları elde ediyoruz
final_word_count = reduce(reduce_func, shuffled_word_count.items(), {})

# Sonuçları 'sonuclar.txt' dosyasına yaz
with open("sonuclar.txt", "w") as result_file:
    result_file.write("Kelime Sayımları:\n")
    for word, count in final_word_count.items():
        result_file.write(f"{word}: {count}\n")

# Shuffle edilmiş sonuçları 'sonuclar_shuffled.txt' dosyasına yaz
with open("sonuclar_shuffled.txt", "w") as shuffled_file:
    shuffled_file.write("Shuffle Edilmiş Kelime Sayımları:\n")
    for word, counts in shuffled_word_count.items():
        for count in counts:
            shuffled_file.write(f"{word}: {count}\n")

print("Sonuçlar 'sonuclar.txt' ve 'sonuclar_shuffled.txt' dosyalarına yazıldı.")
