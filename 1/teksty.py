tekst = "Witaj świecie"
print(tekst)
print(type(tekst))  # <class 'str'>

# teskty sa niemutowalne
tekst.upper()
""" Return a copy of the string converted to uppercase. """
print(tekst)  # Witaj świecie
print(tekst.upper())  # WITAJ ŚWIECIE
print(tekst)
tekst2 = tekst.upper()
print(tekst2)  # WITAJ ŚWIECIE

print(tekst.lower())  # witaj świecie
tekst_lower = tekst.lower()
print(tekst.lower())

print(tekst.removesuffix('świecie'))  # "Witaj "
print(tekst.removeprefix("Witaj"))  # " świecie"
print(" świecie".strip())  # "świecie"

print(tekst)  # Witaj świecie

print(tekst.count("i"))  # 3
print(tekst.count("i", 0, 4))
# Witaj świecie
# numerujemy od zera
# 0123456789
# 0, 4
# Wita 0123 - z prawej strony zbiór otwarty
print(tekst.count("i", 5, 9))  # " świ", 1
print(tekst.count("j", 0, 4))  # "Wita" -> 0123
print(tekst[3])  # indeks 3 czyli "a"

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie'
print(type(encoded_s))  # <class 'bytes'>
print(encoded_s.decode('utf-8'))  # Witaj świecie

imie = 'Radek'
tekst_format = f"Mam na imię {imie} i lubię Pythona"
# f - f string - tekst sformatowany
# w {} wpisujemy zawartość zmiennej
print(tekst_format)  # Mam na imię Radek i lubię Pythona
tekst_format_2 = f"\tMam na imię {imie}\n i lubię Pythona.\b"
print(tekst_format_2)
# "	  Mam na imię Radek
#  i lubię Pythona"
# \t - tabulator
# \n - nowa linia
# \b - backspace

starszy = "witaj %s!"  # %s - oczekuje stringa
print(starszy % imie)  # witaj Radek!

print('Witaj {}!'.format(imie))  # Witaj Radek!

# tekst wielolinijkowy
print("""Tekst
wielolinijkowy
    sformatowany""")
# "Tekst
# wielolinijkowy
#     sformatowany"
