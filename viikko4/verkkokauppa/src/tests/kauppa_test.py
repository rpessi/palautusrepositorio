import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())
        self.varasto_mock = Mock()

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42
        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")
        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_toinen_testi(self):
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", self.viitegeneraattori_mock.uusi()-1, "12345", 
            kauppa._kaupan_tili, kauppa._ostoskori.hinta())

    def test_kolmas_testi(self):
        def varasto_saldo(tuote_id):
            if tuote_id == 1 or tuote_id ==2:
                return 10
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 4)
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", self.viitegeneraattori_mock.uusi()-1, "12345", 
            kauppa._kaupan_tili, kauppa._ostoskori.hinta())

    def test_neljas_testi(self):
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 0
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 4)
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("kalle", "54321")
        self.pankki_mock.tilisiirto.assert_called_with("kalle", self.viitegeneraattori_mock.uusi()-1, "54321", 
            kauppa._kaupan_tili, kauppa._ostoskori.hinta())
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("maija", "111")
        self.pankki_mock.tilisiirto.assert_called_with("maija", self.viitegeneraattori_mock.uusi()-1, "111", 
            kauppa._kaupan_tili, kauppa._ostoskori.hinta())
        
    def test_viides_testi(self):
        self.varasto_mock = Mock(wraps=Varasto())
        self.kauppa_mock = Mock(wraps=Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock))
        self.kauppa_mock.aloita_asiointi()
        self.kauppa_mock.lisaa_koriin(1)
        self.kauppa_mock.poista_korista(1)
        self.kauppa_mock.poista_korista.assert_called_with(1)
