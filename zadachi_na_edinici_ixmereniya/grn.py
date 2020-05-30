class UAH:
    uah = None
    kop = None

    def __init__(self, uah, kop = 0):
        self.uah = uah
        self.kop = kop

    def __add__(self, other):
        kopTemp = self.uah * 100 + self.kop + other.uah * 100 + other.kop

        #self.uah = round(kopTemp / 100)
        self.uah = int(kopTemp / 100)
        self.kop = kopTemp % 100
        return self



def dodatyGrivny(grn1, kop1, grn2, kop2):
    kopVsogo1 = 100 * grn1 + kop1
    kopVsogo2 = 100 * grn2 + kop2
    vsogoKop = kopVsogo1 + kopVsogo2
    vsogoGrn = int(vsogoKop / 100)
    ostachaKop = vsogoKop % 100
    return str(vsogoGrn) + " грн. " + str(ostachaKop) + " коп."

print(dodatyGrivny(10,12,11,5))
















#sum = UAH(100, 10)

#sum = sum + UAH(10, 1)
#sum += UAH(10, 1)

#sum = self      + other
#sum = UAH(2, 50) + UAH(1)

#print(str(sum.uah) + " грн. " + str(sum.kop) + " коп")

