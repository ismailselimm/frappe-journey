from dataclasses import dataclass
from datetime import datetime

def valid_tc(tc: str) -> bool:
    if not (tc and tc.isdigit() and len(tc) == 11 and tc[0] != "0"):
        return False
    d = list(map(int, tc))
    d10 = ((d[0] + d[2] + d[4] + d[6] + d[8]) * 7 - (d[1] + d[3] + d[5] + d[7])) % 10
    d11 = sum(d[:10]) % 10
    return d[9] == d10 and d[10] == d11

@dataclass
class Randevu:
    hasta_ad: str
    tc_kimlik: str
    doktor: str
    tarih: datetime
    durum: str = "Draft"

    def __post_init__(self):
        if not valid_tc(self.tc_kimlik):
            raise ValueError("TC Kimlik geçersiz")

if __name__ == "__main__":
    # Bilinen geçerli örnek: 10000000146
    r = Randevu(
        hasta_ad="Ayşe Yılmaz",
        tc_kimlik="10000000146",
        doktor="Dr. Selim",
        tarih=datetime.now(),
    )
    print("OK:", r)
