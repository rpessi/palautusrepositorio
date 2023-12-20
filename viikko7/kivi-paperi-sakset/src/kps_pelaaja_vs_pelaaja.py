from kps_runko import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):

    def _toisen_siirto(self, ensimmaisen_siirto="k"):
        return input("Toisen pelaajan siirto: ")
