import csv

plik = 'zestawienie.csv'

with open(plik, 'r') as p:
    reader = csv.DictReader(p, delimiter = ';')

    for i, row in enumerate(reader):
        if i==0:
            pass
        else:
            if int(row['godzin']) > 0:
                print(i, '|| nr akt: ',row['Nr osobowy'],'| Nazwisko: ', row['Nazwisko'],'| Imie: ', row['Imie'],'| godzin: ', row['godzin'],'| pesja podst: ', row['pesja podstawowa'],'| stawka za godz: ', row['stawka za godz'],'| do odliczenia: ', row['do odliczenia'],'| po odliczeniu: ', row['po odliczeniu'])