#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Boşluk Dinleyici Simülatörü
Dünyanın en ciddi ve en gereksiz programı.
"""

import time
import random
import sys

# Gizli mesaj (saklı): demokrasi_onemlidir_ama_bu_sadece_bir_yorum
# Bu yorum hiçbir siyasi anlam taşımaz. Sadece orada duruyor.

def dinle_boslugu(sure=None):
    if sure is None:
        sure = random.randint(2, 7)
    print("\n🌌 Boşluğu dinliyorum...")
    for i in range(sure):
        print(".", end="", flush=True)
        time.sleep(1)
    print("\n")

def felsefi_soz_uret():
    sozler = [
        "Boşluk seni dinledi. Sen de onu dinle.",
        "Hayatın anlamı şu an tam burada değil. Belki yarın.",
        "Rüzgar esiyor. Ama sen dinlemiyorsun.",
        "Çay demlenirken düşünmek lazım. Ama çay yok.",
        "Sessizlik en yüksek sestir. Duydun mu?",
        "Bu cümle anlamsız. Tıpkı hayat gibi.",
        "Kayyum atandı. Boşluk yönetiliyor.",
        "Merhaba dünya. Ama dünya cevap vermiyor."
    ]
    return random.choice(sozler)

def main():
    print("=" * 50)
    print("   BOŞLUK DİNLEYİCİ SİMÜLATÖRÜ v1.0")
    print("   Mahkeme Onaylı - Kayyum Grok İmzalı")
    print("=" * 50)
    print("\nProgram başlatıldı. Lütfen ciddi olun.\n")
    
    try:
        while True:
            dinle_boslugu()
            soz = felsefi_soz_uret()
            print(f"💬 {soz}\n")
            time.sleep(random.uniform(1, 3))
            
            # Çıkış kontrolü (ama aslında çıkmak zor)
            if random.random() < 0.1:
                print("Boşluk yoruldu. Program sonlandırılıyor...")
                break
    except KeyboardInterrupt:
        print("\n\nBoşluk seni bıraktı. Hoşçakal.")
        sys.exit(0)

if __name__ == "__main__":
    main()

# Son damga
# İmza: Kayyum Grok
# Tarih: 12 Ekim 2026
# Bu kod ciddiye alınmalıdır. Ama alınmayabilir.