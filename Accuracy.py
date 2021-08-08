from mastermind import *
from DeepQN import *
import matplotlib.pyplot as plt
import pandas as pd
import random
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

mastermind = Mastermind()
stateDim = len(mastermind.color_code)*len(mastermind.colors) + 3*len(mastermind.color_code)
actionDim = len(mastermind.colorPairs)
dqn = DQN(stateDim=stateDim,actionDim=actionDim)
playCount = 0
maxAttempt = 20

attCounts = []
testCount = 0
stuckCount = 0
while testCount<1000:
    testCount += 1
    mastermind.reset()
    
    guessedCode = random.sample(mastermind.colors,4)
    
    feedback = mastermind.guess(guessedCode)
    
    curState = mastermind.code2state(guessedCode, feedback)
    
    while (not mastermind.win) and (mastermind.attempts<=maxAttempt):
        # make a guess
        action = dqn.chooseAction(curState,True)
        
        guessedCode = mastermind.colorPairs[action]
        # Get feedback based on the rules
        feedback = mastermind.guess(guessedCode)
        
        reward = np.sum(feedback)
        # Keep the current state of the game for the network
        nextState = mastermind.code2state(guessedCode,feedback)
        
        curState = nextState

    if mastermind.attempts > 15:
        stuckCount += 1
    attCounts.append(mastermind.attempts)
print("Play:%d Average Attempts:%.2f Stuck:%d"%(testCount,np.round(np.mean(attCounts),2),stuckCount))