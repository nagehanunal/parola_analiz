# parola_analiz

Bu proje, metin dosyasından okuduğu parolaları kurallara göre analiz edip puanlayan ve sonuçları istenilen formatta raporlayan bir komut satırı uygulamasıdır.

Proje Dosyaları:

- main.py: Programın başlatıldığı ve akışın yönetildiği ana dosya.
- dosyalar.py: Girdi dosyasını okuyan ve çıktıyı yazan fonksiyonlar.
- parola_olcer.py: Parolanın uzunluğunu ve karakterlerini inceleyip puan veren sınıf.
- hatalar.py: Özel hata sınıfları (dosya ve parola hataları).
- kurallar.py: Sabit değerler ve kurallar.
- parolalar.txt: Test etmek için örnek parola listesi.

Çalıştırma:
python main.py parolalar.txt

Raporun csv olarak çıkması için:
python main.py parolalar.txt --cikti rapor.csv
