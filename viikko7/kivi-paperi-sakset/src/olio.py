from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja

def luo_peliolio(pelityyppi:int):
    oliot = [KPSPelaajaVsPelaaja(), KPSTekoaly(), KPSParempiTekoaly()]
    return oliot[pelityyppi]

def aloita_peli(pelityyppi:int):
    peli = luo_peliolio(pelityyppi)
    peli.pelaa()
