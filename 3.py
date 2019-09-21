from collections import Counter
stokUangKembalian = [50000, 20000, 10000, 5000, 2000, 1000, 500]


def hitungKembalian(totalBelanja, totalUang):

    daftarUangKembalian = []
    uangKembalian = totalUang-totalBelanja
    while uangKembalian >= 0:
        UangKembalianMax = max(
            list(filter(lambda x: x <= uangKembalian, stokUangKembalian)), default=0)

        if UangKembalianMax == 0:
            return (Counter(daftarUangKembalian))

        uangKembalian -= UangKembalianMax
        daftarUangKembalian.append(UangKembalianMax)


if __name__ == "__main__":
    try:
        kembalian = hitungKembalian(31000, 35000)
        for k in stokUangKembalian:
            print('{}x {}'.format(kembalian[k], k))
    except:
        print('Tolong cek kembali uang anda')
