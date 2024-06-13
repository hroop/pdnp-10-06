# stworzyc funkcje kantor
# ma posiadać dwie wewnętrzne funkcje usd, eur
# w zaleznosci od parametru funkcja ma zwracac funkcje usd lub eur
# mozliwosc wymiany dowolnej kwoty
def kantor(waluta):
    print("Otwieram kantor")

    def usd(kwota=0):
        print(f"Wymieniam usd {kwota} na {kwota * 4.0} pln")

    def eur(kwota=0):
        print(f"Wymieniam eur {kwota} na {kwota * 4.3} pln")

    if waluta == 'eur':
        return eur
    else:
        return usd


zenek_usd = kantor('usd')
zenek_usd()
zenek_usd(1000)

mirek_eur = kantor('eur')
mirek_eur()
mirek_eur(1000)
# Otwieram kantor
# Wymieniam usd 0 na 0.0 pln
# Wymieniam usd 1000 na 4000.0 pln
# Otwieram kantor
# Wymieniam eur 0 na 0.0 pln
# Wymieniam eur 1000 na 4300.0 pln