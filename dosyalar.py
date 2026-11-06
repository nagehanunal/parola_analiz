from hatalar import dosya_hatasi
from pathlib import Path
import csv
import json

def oku(yol):
    path=Path(yol)
    try:
        with open(path,"r",encoding="utf-8") as f:
            return f.readlines()

    except FileNotFoundError:
        raise dosya_hatasi(f"Girdi dosyası bulunamadı: {yol}")
    except PermissionError:
        raise dosya_hatasi(f"Girdi dosyası okunamadı: {yol}")
    except IsADirectoryError:
        raise dosya_hatasi(f"Girdi dosyası bir dizin: {yol}")
    except UnicodeDecodeError:
        raise dosya_hatasi(f"Girdi dosyası okunamadı (UnicodeDecodeError): {yol}")    

def yaz(yol, kayitlar,ozet):
    path=Path(yol)
    try:
        veriler={ 
                "toplam":ozet["toplam"],
                "gecerli":ozet["gecerli"],
                "atlanan":ozet["atlanan"],
                "dagilim":ozet["dagilim"]  
            }

        if path.suffix.lower()==".csv":
            with open(path,"w",newline="",encoding="utf-8") as f:
                yazici=csv.DictWriter(f,fieldnames=["uzunluk","puan","seviye"])
                yazici.writeheader()
                yazici.writerows(kayitlar)
        elif path.suffix.lower()==".json":
            with open(path,"w",encoding="utf-8") as f:
                json.dump(veriler,f,ensure_ascii=False,indent=2)        
    except PermissionError:
        raise dosya_hatasi(f"Rapor dosyası yazılamadı: {yol}")

  