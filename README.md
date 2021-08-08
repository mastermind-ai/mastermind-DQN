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

**Example**

Target: `['purple', 'red', 'blue', 'green']`

For feedback, the colors represent the following scenarios

- `default`: wrong color, wrong location
- `white`: correct color, wrong location
- `black`: correct color, correct location

| Iteration | Guess                                   | Feedback                                 |
| --------- | --------------------------------------- | ---------------------------------------- |
| 0         | ['red', 'blue', 'green', 'purple']      | ['white', 'white', 'white', 'white']     |
| 1         | ['blue', 'blue', 'green', 'purple']     | ['default', 'white', 'white', 'white']   |
| 2         | ['green', 'blue', 'green', 'purple']    | ['default', 'white', 'white', 'white']   |
| 3         | ['purple', 'blue', 'green', 'purple']   | ['default', 'white', 'white', 'black']   |
| 4         | ['purple', 'green', 'green', 'purple']  | ['default', 'default', 'white', 'black'] |
| 5         | ['purple', 'yellow', 'green', 'purple'] | ['default', 'default', 'white', 'black'] |
| 6         | ['purple', 'red', 'green', 'purple']    | ['default', 'white', 'black', 'black']   |
| 7         | ['purple', 'red', 'yellow', 'purple']   | ['default', 'default', 'black', 'black'] |
| 8         | ['purple', 'red', 'blue', 'purple']     | ['default', 'black', 'black', 'black']   |
| 9         | ['purple', 'red', 'blue', 'yellow']     | ['default', 'black', 'black', 'black']   |
| 10        | ['purple', 'red', 'blue', 'green']      | ['black', 'black', 'black', 'black']     |

**Solver performance**

Run the following to evaluate the algorithm's performance on 1000 solves

```bash
python Accuracy.py
```

Results

Model Successfully Loaded
Play:1000 Average Attempts:6.17 Stuck:96

