from dosyalar import oku,yaz
from kurallar import varsayilan_log,varsayilan_cikti
from hatalar import parola_hatasi,dosya_hatasi
from parola_olcer import parola_olcer

import argparse
import logging
import sys

def analiz_et(parolalar):
    kayitlar=[]
    atlanan=0
    dagilim={
        "zayıf":0,
        "orta":0,
        "güçlü":0
    }

    for metin in parolalar:
        temiz_metin=metin.rstrip('\n')
        try:
            p=parola_olcer(temiz_metin)
            sev=p.seviye()

            if "zayıf" in sev:
                dagilim["zayıf"]+=1
            elif "orta" in sev:
                dagilim["orta"]+=1
            else:
                dagilim["güçlü"]+=1   

            kayitlar.append({
                "uzunluk":p.uzunluk,
                "puan":p.puan(),
                "seviye":sev
            })                     

        except parola_hatasi:
            atlanan+=1    

    ozet={
        "toplam":len(parolalar),
        "gecerli":len(kayitlar),
        "atlanan":atlanan,
        "dagilim":dagilim  
    }
    return kayitlar,ozet


def arguman_ayristir():
    """Komut satırı argümanlarını yapılandırır."""
    parse = argparse.ArgumentParser(description="Parolaları analiz eder ve raporlar.")
    parse.add_argument("girdi", help="Parola dosyası (.txt veya .csv)")
    parse.add_argument("--cikti", default=varsayilan_cikti, help="Rapor dosyası")
    parse.add_argument("--log", default=varsayilan_log, help="Log dosyası")
    return parse.parse_args()


def main():
    args = arguman_ayristir()
    
    logging.basicConfig(
        filename=args.log,
        encoding="utf-8",
        level=logging.DEBUG,
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        datefmt="%H:%M:%S"
    )
    
    try:
        logging.info(f"girdi okunuyor: {args.girdi}")

        parolalar=oku(args.girdi)
        logging.info(f"girdi okundu")
        
        kayitlar, ozet = analiz_et(parolalar)
        
        yaz(args.cikti, kayitlar, ozet)
        logging.info(f"rapor yazildi: {args.cikti}")
        
        print(f"{ozet['toplam']} satir okundu: {ozet['gecerli']} gecerli, {ozet['atlanan']} atlandi")
        print(f"Dagilim: {ozet['dagilim']}")
        print(f"Rapor yazildi: {args.cikti} | log: {args.log}")
        
        return 0
        
    except dosya_hatasi as hata:
        print(f"Hata: {hata}")
        logging.error(f"Dosya hatası: {hata}")
        return 1

if __name__ == "__main__":
  sys.exit(main())