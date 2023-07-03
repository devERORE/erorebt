from cv2 import cv2
import os
from time import time, sleep
import pydirectinput, pyautogui, threading
from ekranyakala import ekranYakala
from vision import Vision
# from detection import Detection

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Pencere ismi aşağıdaki başlık kısmına yazılmalı.
baslik = ("UYGULAMA ADI")

# Pencerenin başlığı eşleşene kadar dönüyor.
for i in baslik:
    try:
        wincap = ekranYakala(i)
    except:
        continue

# Model dosyası
cascade = cv2.CascadeClassifier("/cascade/cascade.xml")

vision = Vision(None)
loop_time = time()

metine_vur = False
s = 1
s1 = 0
kontrol = 0
def metinevur(rectangles):
    global metine_vur
    global kontrol
    global s, s1

    if len(rectangles) > 0:
        targets = vision.get_click_points(rectangles)
        target = wincap.get_screen_position(targets[0])
        pyautogui.moveTo(x=target[0], y=target[1])
        sleep(0.4)
        pyautogui.click(x=target[0], y=target[1])
        print(s,"Metin Bulundu")
        s += 1
        # Metin taşını kesme hızınıza(saniye) göre bekletin
        sleep(17)
    else:
        s1 += 1
        print(s1, "Bulunamadı")
        """
        - Oyunda objeyi bulamazsa 6 defa 'e' tuşuna basar. yani ekranı döndürür.
        'f' ile kamerayı genişletir.
        - 3 defa bulamazsa 3 kez 'w'e basar ve ileri gider.
        Bu işlem sadece Metin2 için geçerlidir. Kendi oyununuzda butonlara göre değişim yapabilirsiniz.

        Yani kısacası burada yaptığımız işlem konum değiştirmek.
        

        Eğer oyun içinde tuş basmıyorsa programı yönetici olarak çalıştırıp deneyin.
        
        """
        pydirectinput.press("e", presses=6)
        pydirectinput.press("f", presses=10)
        kontrol += 1
        if kontrol >= 3:
            print("Kontrol", kontrol)
            pydirectinput.press("w", presses=3)
            kontrol = 0

    metine_vur = False

while True:
    ss = wincap.get_screenshot()

    rectangles = cascade.detectMultiScale(ss)
    
    detection_image = vision.draw_rectangles(ss, rectangles)
    cv2.imshow('Goruntu', detection_image)

    if not metine_vur:
        """
        True, False kullanmamızın sebebi,
        Program sürekli döngüde kalacağı için,
        sadece 'false' durumlarda bu koşula girmesini istiyoruz.
        """
        metine_vur = True
        thrd = threading.Thread(target=metinevur, args=(rectangles,))
        thrd.start()

    # FPS göster
    # print("FPS {}".format(1 / (time() - loop_time)))
    # loop_time = time()
    
    # Döngüden çık
    key = cv2.waitKey(1)
    if key == ord("q"):
        cv2.destroyAllWindows()
        print("Döngüden Çıkıldı")
        break