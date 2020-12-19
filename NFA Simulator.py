
def get_User_String():
    a = input("Please input a string of a's and b's: ")
    return a

def get_NFA():
    numOfStates = int(input("Please input the number of states you would like to have: "))
    print("You now have " + str(numOfStates) + " states you can use, each is numbered sequentially from 1.")
    startState = 'a'

    while startState == 'a':
        curr = int(input("Which state would you like to start at? "))
        if curr < 1 or curr > numOfStates:
            print("You inputed a number that is out of the bounds of the number of states you have... please input a starting state that you have: ")
        if 1 <= curr and curr < numOfStates:
            startState = curr
            print("Your starting state is now at state " + str(startState))
    print(" ")
    print("Now you need to connect your states... for inputs, please enter the number of the state you want to transfer two or a blank space ' ' if you want there to be no transition.")
    NFA_LIST = []

    for i in range(numOfStates):
        aList = []
        bList = []

        check1 = True
        while check1:
            a_output = input("Enter a transition state for 'a' at state " + str(i+1) + ": ")
            if a_output == ' ':
                check1 = False
            else:
                aList.append(int(a_output) - 1)
        check2 = True
        while check2:
            b_output = input("Enter a transition state for 'b' at state " + str(i+1) + ": ")
            if b_output == ' ':
                check2 = False
            else:
                bList.append(int(b_output) - 1)

        # These two if statements basically create a transition to a hypothetical dead-state if there is no transition for "a" or "b"
        if aList == []:
            aList.append(numOfStates)
        if bList == []:
            bList.append(numOfStates)

        NFA_LIST.append([aList, bList])

    finalState = numOfStates-1
    hypotheticalDeadState = numOfStates
    return NFA_LIST, startState, finalState, hypotheticalDeadState


def transitionFunction(transition, input, final, state, symbolCounter, hypotheticalDeadState):
    for j in range (len(input)): # j iterates through the length of the inputed string
        for each in transition[state][int(input[j])]:
            if each < hypotheticalDeadState:    # Just checks if there are more states to check
                state = each
                if j == len(input)-1 and (str(state) in final): # last symbol is read and current state lies in the set of final states
                    print("Accepted")
                    break
                transitionFunction(transition, input[symbolCounter+1:], final, state, symbolCounter, hypotheticalDeadState) #i nput string for next transition is input[i+1:]
        symbolCounter = symbolCounter + 1 # increment the counter


def RunNFASimulator():
    NFA = get_NFA()
    UserInput = get_User_String()

    UserInput = list(UserInput)
    for index in range(len(UserInput)):
        if UserInput[index] == 'a':
            UserInput[index] = '0'
        elif UserInput[index] == 'b':
            UserInput[index] = '1'

    StartState = NFA[1]
    FinalState = NFA[2]
    Symbol_Counter = 0  # This will be used to keep track of the symbols that have already been counted

    transitionFunction(NFA[0], UserInput, FinalState, StartState, Symbol_Counter, NFA[3])
    print("Rejected")   # This will execute if our transition function cannot find any transitions at any point for the inputed string... thus meaning it is not accepted!


### Runs the program:
RunNFASimulator()