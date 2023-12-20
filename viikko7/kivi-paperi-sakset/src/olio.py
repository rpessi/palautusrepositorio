#from kps_runko import KiviPaperiSakset
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

def luo_peliolio(pelityyppi):
    oliot = [KPSPelaajaVsPelaaja(), KPSTekoaly(), KPSParempiTekoaly()]
    return oliot[pelityyppi]

def aloita_peli(pelityyppi):
    peli = luo_peliolio(pelityyppi)
    peli.pelaa()
