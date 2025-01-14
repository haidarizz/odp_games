def a():
    """
    Buatlah fungsi Python yang mengonversi angka menjadi format teks
    bahasa Indonesia untuk angka 1 hingga 1.000

    MASUKAN
    n = 345

    KELUARAN
    Tiga ratus empat puluh lima
    """

    # write the code solution here
    n = int(input("Masukkan angka: "))

    if not (1 <= n <= 999_999_999):
        return "Angka di luar jangkauan (1-999999999)."

    angka = ["", "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan"]
    satuan = ["", "puluh", "ratus"]

    def terbilang_3digit(num):
        """Mengonversi angka tiga digit menjadi teks."""
        hasil = ""
        ratusan = num // 100
        puluhan_satuan = num % 100

        # Ratusan
        if ratusan > 0:
            if ratusan == 1:
                hasil += "seratus "
            else:
                hasil += angka[ratusan] + " ratus "

        # Puluhan dan satuan
        if 10 <= puluhan_satuan <= 19:
            hasil += ["sepuluh", "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas", "enam belas", "tujuh belas", "delapan belas", "sembilan belas"][puluhan_satuan - 10]
        else:
            puluhan = puluhan_satuan // 10
            satuan_angka = puluhan_satuan % 10

            if puluhan > 0:
                if puluhan == 1:
                    hasil += "sepuluh "
                else:
                    hasil += angka[puluhan] + " puluh "

            if satuan_angka > 0:
                hasil += angka[satuan_angka]

        return hasil.strip()

    hasil = ""

    # Bagian juta
    juta = n // 1_000_000
    if juta > 0:
        hasil += terbilang_3digit(juta) + " juta "

    # Bagian ribu
    ribu = (n % 1_000_000) // 1_000
    if ribu > 0:
        if ribu == 1:
            hasil += "seribu "
        else:
            hasil += terbilang_3digit(ribu) + " ribu "

    # Bagian satuan
    satuan = n % 1_000
    if satuan > 0:
        hasil += terbilang_3digit(satuan)
    
    hasil = hasil.capitalize()
    print(hasil.strip())
    return hasil.strip()
    #print("Mohon maaf, permainan A belum tersedia!")
