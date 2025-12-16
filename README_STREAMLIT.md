# ❌⭕ Tic-Tac-Toe vs AI - Streamlit Version

Play Tic-Tac-Toe against an unbeatable AI powered by the Minimax algorithm. Can you manage a tie?

## Features

- 🤖 **Unbeatable AI** using Minimax algorithm
- 🎮 **Interactive gameplay** - Click to make moves
- 📊 **Statistics tracking** - Wins, losses, and ties
- 🔄 **Flexible starting** - You or AI can go first
- 🎨 **Color-coded board** - Blue for X, Red for O
- 💡 **Strategy tips** included
- 🧠 **Algorithm explanation** built-in

## How to Run

### Prerequisites
```bash
pip install streamlit
```

### Run the App
```bash
streamlit run streamlit_tictactoe.py
```

## How to Play

1. **Start a game** - Click "New Game" in sidebar
2. **Make your move** - Click any empty cell
3. **Try to win** - Get 3 in a row (horizontal, vertical, or diagonal)
4. **Challenge yourself** - Can you at least tie with the AI?

## Game Rules

### Objective
Get three of your marks in a row before your opponent does.

### Valid Lines
- **Horizontal**: Any complete row (123, 456, 789)
- **Vertical**: Any complete column (147, 258, 369)
- **Diagonal**: Corner to corner (159, 357)

### Winning
- ✅ **You win**: Get 3 X's in a row
- ❌ **AI wins**: AI gets 3 O's in a row
- 🤝 **Tie**: Board is full with no winner

## The Minimax Algorithm

### How It Works
The AI uses Minimax, a decision-making algorithm that:

1. **Simulates all possibilities** - Looks at every possible game state
2. **Assumes perfect play** - Both players play optimally
3. **Maximizes AI score** - Chooses moves leading to wins
4. **Minimizes your score** - Blocks your winning moves

### Why It's Unbeatable
- Explores **entire game tree** (all possible futures)
- Assigns **scores** to outcomes (win=+1, lose=-1, tie=0)
- Always chooses the **optimal move**
- Accounts for **your best response**

### Algorithm Complexity
- **States explored**: Up to 255,168 game states
- **Max depth**: 9 moves (full board)
- **Time**: Milliseconds for Tic-Tac-Toe

## Strategy Tips

### Opening Moves
1. **Center** (position 5): Most strategic square
   - Controls 4 lines
   - Best opening move
   
2. **Corners** (1, 3, 7, 9): Second best
   - Control 3 lines each
   - Create fork opportunities
   
3. **Edges** (2, 4, 6, 8): Weakest
   - Only control 2 lines
   - Easier to defend against

### Advanced Tactics

#### The Fork
Create two winning threats at once
```
X | O | X
---------
  | X | 
---------
O |   | 
```
X can win at positions 7 or 3!

#### The Block
Always block opponent's winning move
```
O | O | 
---------
X |   | X
---------
  |   | 
```
Must play position 3 to block O!

### Best Strategy
Since the AI is perfect:
- ✅ **Possible**: Force a tie with perfect play
- ❌ **Impossible**: Beat the AI
- 🎯 **Goal**: Avoid losing and tie every game!

## Game Statistics

The app tracks:
- **Your Wins (X)**: Times you won
- **AI Wins (O)**: Times AI won
- **Ties**: Games ending in a draw
- **Moves Made**: Current game progress

## Files Included

- `streamlit_tictactoe.py` - Main Streamlit application
- `TicTacToe.py` - Original command-line version
- `README_STREAMLIT.md` - This file

## Original Version

Run the original command-line version:
```bash
python TicTacToe.py
```

This version requires typing move numbers (1-9).

## Mathematical Analysis

### Total Possible Games
- **First move**: 9 choices
- **Second move**: 8 choices
- **And so on...**
- **Total unique games**: 255,168
- **Unique board states**: 26,830

### Optimal Play Outcomes
With perfect play from both sides:
- **First player advantage**: Yes (goes to center)
- **Best outcome**: Tie (with perfect play)
- **Proven result**: Game is a draw

### Fun Facts
- 🎮 Tic-Tac-Toe is a **solved game**
- 🧮 First computer player built in 1952
- 🤖 Perfect AI has existed since the 1970s
- 🌍 Game is over 3,000 years old (Ancient Egypt)
- 📊 138 unique wins for X, 77 for O

## Learning from the AI

### Observe Patterns
Watch how the AI:
- Always blocks your winning moves
- Creates multiple threats (forks)
- Prefers center and corners
- Never makes mistakes

### Practice Perfect Play
Try to:
- Always go for center first
- Block AI's winning moves immediately
- Create forks when possible
- Recognize unwinnable positions

## Challenge Levels

### Level 1: Avoid Losing
Can you prevent the AI from winning?

### Level 2: Force Ties
Can you tie consistently?

### Level 3: Understand Why
Can you predict every AI move?

## Educational Value

This game teaches:
- **Algorithm thinking**: Understanding decision trees
- **Strategic planning**: Thinking ahead
- **Pattern recognition**: Spotting winning positions
- **Game theory**: Zero-sum games
- **Recursion**: How Minimax explores possibilities

Perfect for learning about AI and algorithms! 🧠

Enjoy playing! Can you beat the unbeatable? (Hint: You can't! But try for a tie!) ❌⭕
