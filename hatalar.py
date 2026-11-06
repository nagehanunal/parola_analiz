class parola_hatasi(Exception):
    """Parola ile ilgili hatalarin ortak tabani."""
class bos_parola_hatasi(parola_hatasi):
    pass

class cok_uzun_parola_hatasi(parola_hatasi):
    pass

class dosya_hatasi(Exception):
    """Girdi/cikti hatalari."""