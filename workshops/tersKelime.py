def tersine_cevir(kelime):
    return kelime[::-1]

def kullanici_girdisi_al():
    kelime = input("Bir kelime girin: ")
    return kelime

def ana_program():
    kelime = kullanici_girdisi_al()
    ters_kelime = tersine_cevir(kelime)
    print("Kelimenin tersi: ", ters_kelime)

ana_program()
