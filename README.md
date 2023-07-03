

Merhaba,
Projenin amacı model eğitimiyle görüntü işlemeli ve nesne algılamalı bir otomasyon uygulaması oluşturup kolaylık sağlamasıdır.
Proje tamamen bir oyuna yönelik yapılmıştır ama bu tarz oyunların hepsinde yapılabilir.
Bir cascade classifier olarak objemizi tanıtıyoruz ve uygulamamız tanıttığımız objeyi otomatik algılıyor ve bizim yapmamız gerekeni kendisi yapıyor

Kodlar github hesabımda herkese açık olarak yayındadır.


Nasıl Çalıştırırım
main.py dosyası eski, onu kullanmanıza gerek yoktur. gui.py üzerinden anlatacağım.

* gui.py dosyasını açıp 110. satırdaki cascade değişkenine cascade.xml dosya yolunu yazın.
* Python yüklü ise CMD ekranını yönetici olarak çalıştırın.
* Dosyaların bulunduğu dizine cd komutu ile gidin
* Ekrana **python gui.py** yazarak enter yapın.
* Araya basıp oyun ekranını seçin.
* Metin kesme sürenizi yazın ve başlata basın.

# SSS
* **No module named ...** := Adı geçen modül yüklü değil demektir.
* **NameError: name 'wincap' is not defined** := Adı geçen ekran bulunamadı demektir.
* **win32ui.error: BitBlt failed** := Oyunda ekran yakalama engelli demektir.



Kaynak:

https://www.youtube.com/watch?v=KecMlLUuiE4&list=PL1m2M8LQlzfKtkKq2lK5xko4X-8EZzFPI
https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html
