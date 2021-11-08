from itertools import *
import random

'''
s = [1, 2, 3, 4]
c = 0
for i in product('1234', repeat=3):
    print(i, end=' ')
    c += 1

print("\n", c)
'''


def start_slot():
    print("Welcome to the Slot Machine!")
    print("    Match 3 of cherry = 10 cr")
    print("    Match 3 of plum = 20 cr")
    print("    Match 3 of lemon = 30 cr")
    print("    Match 3 of grapes = 40 cr")


class SlotMachine:
    def __init__(self):
        self.words = ["Cherry", "Plum", "Lemon", "Grapes"]

    def spin(self):
        line1 = []
        line2 = []
        line3 = []
        for j in range(3):
            rand = random.randint(0, 3)
            line1.append(rand)
            rand = random.randint(0, 3)
            line2.append(rand)
            rand = random.randint(0, 3)
            line3.append(rand)

        words1 = []
        words2 = []
        words3 = []
        for j in range(3):
            words1.append(self.words[line1[j]])
            words2.append(self.words[line2[j]])
            words3.append(self.words[line3[j]])

        # print(word1, " ", word2, " ", word3)
        print(words1[0], " ", words1[1], " ", words1[2])
        print(words2[0], " ", words2[1], " ", words2[2])
        print(words3[0], " ", words3[1], " ", words3[2])

        win1 = 0
        win2 = 0
        win3 = 0

        if line1[0] == line1[1] == line1[2]:
            if line1[0] == 0:
                win1 = 10
            elif line1[0] == 1:
                win1 = 20
            elif line1[0] == 2:
                win1 = 30
            else:
                win1 = 40

        if line2[0] == line2[1] == line2[2]:
            if line2[0] == 0:
                win2 = 10
            elif line2[0] == 1:
                win2 = 20
            elif line2[0] == 2:
                win2 = 30
            else:
                win2 = 40

        if line3[0] == line3[1] == line3[2]:
            if line3[0] == 0:
                win3 = 10
            elif line3[0] == 1:
                win3 = 20
            elif line3[0] == 2:
                win3 = 30
            else:
                win3 = 40

        return win1 + win2 + win3


def band_rtp(band):
    return band.get('earn') / band.get('totalBet')


class Weights:
    band1 = {'earn': 9435887360, 'totalBet': 9905819520, 'weight': 130000}
    band2 = {'earn': 4885756080, 'totalBet': 6184163520, 'weight': 160000}
    band3 = {'earn': 227520000, 'totalBet': 150720, 'weight': 3}
    band4 = {'earn': 5814797280, 'totalBet': 1352401920, 'weight': 35000}
    band5 = {'earn': 5965686960, 'totalBet': 926880000, 'weight': 24000}
    band6 = {'earn': 12119692200, 'totalBet': 6567131520, 'weight': 170000}
    band7 = {'earn': 2424346560, 'totalBet': 640183680, 'weight': 16570}
    band8 = {'earn': 170067120, 'totalBet': 16192180320, 'weight': 440000}
    band9 = {'earn': 72124920, 'totalBet': 2316424320, 'weight': 58500}
    band10 = {'earn': 3120, 'totalBet': 382080, 'weight': 1500}
    band = [band1, band2, band3, band4, band5, band6, band7, band8, band9, band10]

    def weights_sum(self):
        s = 0
        for i in self.band:
            s += i.get('weight')
        return s

    def weighted_sum(self):
        s = 0
        for i in self.band:
            s += band_rtp(i) * i.get('weight')
        return s

    def weighted_average(self):
        return self.weighted_sum() / self.weights_sum()

    def change_weights(self):
        for i in self.band:
            if abs(i.get('earn') / i.get('totalBet') - 0.95) >= 0.01:
                i.update(weight=0)
                # c += 1
            else:
                i.update(weight=1)


def first_task():
    start_slot()
    slot = SlotMachine()

    replay = 'y'
    while replay.lower() == 'y':
        input("Press Enter to spin:  ")
        print()
        calculate = slot.spin()
        print("You have won $" + str(calculate))
        replay = input("Play again?(Y/N)  ")


def second_task():
    weights = Weights()
    print('default RTP: ')
    print(round(weights.weighted_average(), 2))
    weights.change_weights()
    print('new RTP: ')
    print(round(weights.weighted_average(), 2))


def main():
    first_task()
    # second_task()


if __name__ == "__main__":
    main()
