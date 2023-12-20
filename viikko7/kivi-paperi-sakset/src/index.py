from olio import aloita_peli

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        valinnat = ["a", "b", "c"]
        if vastaus in valinnat:
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            pelityyppi = valinnat.index(vastaus)
            aloita_peli(pelityyppi)
        else:
            break

if __name__ == "__main__":
    main()
