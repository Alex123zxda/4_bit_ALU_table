#import time

INPUTS = [0] * 9
OUTPUTS = [0] * 9
CHECK, x, VALUE = 2 ** (len(INPUTS) - 1) - 1, 0, 0

def FULL_ADDER(A, B, C):
    if A == B == C == 1: return "11"
    elif A == B == 1: return "01"
    elif B == C == 1: return "01"
    elif A == C == 1: return "01"
    elif A == 1: return "10"
    elif B == 1: return "10"
    elif C == 1: return "10"
    else: return "00"

def ALU(A0, B0, A1, B1, A2, B2, A3, B3):
    OUTPUTS = [0] * 9
    CO0 = FULL_ADDER(A0, B0, INPUTS[0])
    CO1 = FULL_ADDER(A1, B1, int(CO0[1]))
    CO2 = FULL_ADDER(A2, B2, int(CO1[1]))
    CO3 = FULL_ADDER(A3, B3, int(CO2[1]))
    O4 = 0
    if CO3[0] == CO3[1] == "1":
        O4 = "1"
    return CO0 + CO1 + CO2 + CO3 + str(O4)

print("-" * 55 + "\n" + "+1|A0|B0|A1|B1|A2|B2|A3|B3| O0|C0|O1|C1|O2|C2|O3|C3|O4|")
try:
    while True:
        for i in range(1, 9):
            if INPUTS[i] == 2:
                INPUTS[i + 1] += 1
                INPUTS[i] = 0
        ALU_VAL = ALU(INPUTS[1], INPUTS[2], INPUTS[3], INPUTS[4], INPUTS[5], INPUTS[6], INPUTS[7], INPUTS[8])

        OUTPUTS[0], OUTPUTS[1], OUTPUTS[2], OUTPUTS[3], OUTPUTS[4], OUTPUTS[5], OUTPUTS[6], OUTPUTS[7], OUTPUTS[8] = \
        int(ALU_VAL[0]), int(ALU_VAL[1]), int(ALU_VAL[2]), int(ALU_VAL[3]), int(ALU_VAL[4]), \
        int(ALU_VAL[5]), int(ALU_VAL[6]), int(ALU_VAL[7]), int(ALU_VAL[8])

        print(INPUTS, OUTPUTS, "\t", x)
        INPUTS[1] += 1
        x += 1
        if x > CHECK:
            if VALUE == 0:
                INPUTS = [0] * 9
                INPUTS[0] = 1
                VALUE = 1
                CHECK = 2 ** len(INPUTS) - 1
            elif VALUE == 1:
                break
#    time.sleep(0.05)
except KeyboardInterrupt:
    print("\nStopped")
