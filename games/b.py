def b():
    """
    Diberikan sebuah list angka, cari pasangan angka dengan selisih terkecil.

    MASUKAN
    data = [4, 8, 15, 16, 23, 42] 

    KELUARAN
    15 16
    """

    data = input('Masukkan angka yang diinginkan (pisahkan dengan koma, contoh: 1, 2, 3): ')
    data = [int(x) for x in data.split(",")]

    data.sort()

    def bb(data):
        selisih = []
        for i in range(len(data)-1):
            selisih.append(abs(data[i] - data[i+1]))
        return selisih

    hasil = bb(data)
    hasill = hasil.index(min(hasil))
    hasill

    u1 = data[hasill]
    u2 = data[hasill+1]
    print('Pasangan angka dengan selisih terkecil adalah', u1, 'dan',u2 )
    # write the code solution here
    # print("Mohon maaf, permainan B belum tersedia!")