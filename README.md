# Deep Q Network (DQN) for Mastermind

**Run the solver for one case:**

```bash
python Test.py
```

- This runs with 5 colors and no replacement in the answer

**Steps:**

1. Start with a random guess
3. Pass the current guess and the feedback to the model, outputs the next action to be taken
4. Stop the iteration when all the slots are the correct color

**Solver performance**

Run the following to evaluate the algorithm's performance on 1000 solves

```bash
python Accuracy.py
```
Model Successfully Loaded

Play:1000 Average Attempts:6.17 Stuck:96

Results


| Color configuration | Allow Duplicates? | Average guesses (out of 1000) |
| ------------------- | ----------------- | ----------------------------- |
| 5 choose 4          | No                | 6.17                         |

