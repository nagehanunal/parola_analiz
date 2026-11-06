from hatalar import bos_parola_hatasi, cok_uzun_parola_hatasi
from kurallar import esik_uzunluk, max_uzunluk,puan_zayif,puan_orta,puan_iyi

class parola_olcer:
    def __init__(self,parola):
        self.parola=parola
        if not parola:
            raise bos_parola_hatasi("parola boş olamaz")
        if len(parola)>max_uzunluk:
            raise cok_uzun_parola_hatasi(f"parola uzunluğu max uzunluk sınırını ({max_uzunluk}) geçemez")

    def istatistik(self):
        """parolanın temel istatistiklerini hesaplar."""
        return{
            "uzunluk":len(self.parola),
            "buyuk_harf":any(i.isupper() for i in self.parola ),
            "kucuk_harf":any(i.islower() for i in self.parola),
            "rakam":any(i.isdigit() for i in self.parola),
            "ozel_karakter":any(not i.isalnum() for i in self.parola)
        }

    @property
    def uzunluk(self):
        return len(self.parola)
    
    def puan(self):
        puan=0
        ist=self.istatistik()
        if ist["uzunluk"]>= esik_uzunluk:
            puan+=1
        if ist["buyuk_harf"]:
            puan+=1    
        if ist["kucuk_harf"]:
            puan+=1
        if ist["rakam"] or ist["ozel_karakter"]:
            puan+=1

        return puan        


    def seviye(self):
        p=self.puan()

        if p<=puan_zayif:
            return "zayıf şifre seviyesi"
        elif p<=puan_orta:
            return "orta şifre seviyesi"
        else:
            return "güçlü şifre seviyesi"


    def rapor(self):
        return {
            "parola":self.parola,
            "uzunluk":self.uzunluk,
            "puan":self.puan(),
            "seviye":self.seviye(),
            "detaylar":self.istatistik()
        }

    def __str__(self):
        return f"Parola(uzunluk={self.uzunluk}, puan={self.puan()}, seviye={self.seviye()})"



