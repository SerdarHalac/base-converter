import math
import sys

def convertNum(baseFrom, baseTo, number, alpha):
	total = 0
	power1 = (len(number) - 1)
	for i in number:
		if(i.isdigit()):
			total += int(int(i) * pow(baseFrom, power1))
			power1 -= 1
		else:
			total += int(alpha.index(i) * pow(baseFrom, power1))
			power1 -= 1

	numberList = []
	runningNum = total
	power = int(math.log(total, baseTo))

	while(power >= 0):
		digit = int(runningNum//(math.pow(baseTo,power)))
		numberList.append(digit)
		runningNum -= (digit * (math.pow(baseTo,power)))
		power -= 1

	return "".join([alpha[x] for x in numberList])

def main():
    alpha = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    redo = True
    while(redo):
        numToConv = sys.argv[1]
        bFrom = int(sys.argv[2])
        redo2 = False
        for i in numToConv:
            if alpha.index(i) >= bFrom:
                redo2 = True
        if (not redo2):
            redo = False
        else:
            print("The inputed number is not possible at this base.\nPlease either change the base or number.")

    bTo = int(sys.argv[3])
    stringer = convertNum(bFrom, bTo, numToConv, alpha)
    print(stringer)
    sys.stdout.flush()

if __name__ == "__main__":
	main()
