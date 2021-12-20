import pyautogui as auto, time

#plik_graficzny_link = 'C:/Users/plmko/PycharmProjects/automat/test.png'
plik_img_brutto = 'img/img_brutto.png'
plik_img_fundusze = 'img/img_fundusze.png'
plik_img_potracenia = 'img/img_potracenia.png'
plik_img_kol_nr_akt = 'img/img_kolumna_numer_akt.png'
plik_img_kolumna_nazwisko = 'img/img_kolumna_nazwisko.png'
plik_img_przycisk_edytuj = 'img/img_przycisk_edytuj.png'

#test1 = plik_graficzny_link+'test.png'
przycisk_img_potracenia = auto.locateOnScreen(plik_img_potracenia)
print(przycisk_img_potracenia)

print('plik_img_kolumna_nazwisko')
auto.click(plik_img_kolumna_nazwisko)
time.sleep(1)

print('rutkowska')
auto.typewrite('rutkowska')
time.sleep(1)

print('plik_img_kol_nr_akt')
auto.click(plik_img_kol_nr_akt)
time.sleep(1)

print('27')
auto.typewrite('27')
time.sleep(1)

print('plik_img_przycisk_edytuj')
auto.click(plik_img_przycisk_edytuj)
time.sleep(2)

print('plik_img_brutto')
auto.click(plik_img_brutto)
time.sleep(2)

print('plik_img_potracenia')
auto.click(plik_img_potracenia)
time.sleep(2)

print('plik_img_fundusze')
auto.click(plik_img_fundusze)
time.sleep(2)

print('plik_img_brutto')
auto.click(plik_img_brutto)
time.sleep(2)


