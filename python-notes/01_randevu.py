from dataclasses import dataclass
from datetime import datetime

@dataclass
class Randevu:
    hasta_ad: str
    doktor: str
    tarih: datetime
    durum: str = "Draft"

if __name__ == "__main__":
    r = Randevu(hasta_ad="Ayşe Yılmaz", doktor="Dr. Selim", tarih=datetime.now())
    print(r)
