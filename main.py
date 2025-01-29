from faker import Faker
import os

fake = Faker()

# Dosya isimlerini belirle
file_names = [f"file_{i}.txt" for i in range(1, 6)]

# Dosyaları oluştur ve her birine rastgele metin yaz
for file_name in file_names:
    with open(file_name, "w") as file:
        for _ in range(10):  # Her dosyaya 10 rastgele cümle ekleyelim
            file.write(fake.sentence() + '\n')
