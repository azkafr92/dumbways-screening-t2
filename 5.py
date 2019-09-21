def isPrime(tanggal):
    if (tanggal == 1):
        return False
    else:
        if (tanggal <= 31):
            for i in range(2, tanggal):
                if tanggal % i == 0:
                    return False
            return True
        else:
            return False


def isOdd(tanggal):
    if tanggal % 2 != 0:
        return True
    else:
        return False


def isMultipleOfFive(tanggal):
    if tanggal % 5 == 0:
        return True
    else:
        return False


def buyEgg(tanggal, uang):
    hargaTelur = 2500
    baseTotalEgg = uang/hargaTelur
    bonusTotalEgg = 0
    lusinTelur = int(baseTotalEgg/12)

    if (isOdd(tanggal)) | (tanggal == 2):
        if isPrime(tanggal):
            bonusTotalEgg += lusinTelur*2
        else:
            bonusTotalEgg += lusinTelur*3

    if isMultipleOfFive(tanggal):
        if isOdd(bonusTotalEgg):
            bonusTotalEgg *= 5
        else:
            bonusTotalEgg *= 10

    return int(baseTotalEgg+bonusTotalEgg)


if __name__ == "__main__":
    print(buyEgg(13, 60000))
