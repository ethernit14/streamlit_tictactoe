import streamlit as st
import math

st.set_page_config(page_title="Tic-Tac-Toe vs AI", page_icon="❌⭕", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .big-font {
        font-size: 50px !important;
        font-weight: bold;
        text-align: center;
    }
    .cell-button {
        font-size: 60px !important;
        height: 100px;
        width: 100px;
    }
</style>
""", unsafe_allow_html=True)

# TicTacToe Class
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        
        return False

# Minimax Algorithm
def minimax(position, depth, is_maximizing, ai_player, human_player):
    if position.current_winner == ai_player:
        return {'position': None, 'score': 1 * (position.num_empty_squares() + 1)}
    elif position.current_winner == human_player:
        return {'position': None, 'score': -1 * (position.num_empty_squares() + 1)}
    elif not position.empty_squares():
        return {'position': None, 'score': 0}
    
    if is_maximizing:
        max_eval = {'position': None, 'score': -math.inf}
        for possible_move in position.available_moves():
            position.make_move(possible_move, ai_player)
            eval = minimax(position, depth + 1, False, ai_player, human_player)
            position.board[possible_move] = ' '
            position.current_winner = None
            eval['position'] = possible_move
            if eval['score'] > max_eval['score']:
                max_eval = eval
        return max_eval
    else:
        min_eval = {'position': None, 'score': math.inf}
        for possible_move in position.available_moves():
            position.make_move(possible_move, human_player)
            eval = minimax(position, depth + 1, True, ai_player, human_player)
            position.board[possible_move] = ' '
            position.current_winner = None
            eval['position'] = possible_move
            if eval['score'] < min_eval['score']:
                min_eval = eval
        return min_eval

# Initialize session state
if 'game' not in st.session_state:
    st.session_state.game = TicTacToe()
    st.session_state.human_letter = 'X'
    st.session_state.ai_letter = 'O'
    st.session_state.game_over = False
    st.session_state.message = "Your turn! You are X"
    st.session_state.human_starts = True
    st.session_state.wins = {'X': 0, 'O': 0, 'Tie': 0}

def reset_game(human_starts=True):
    """Reset the game"""
    st.session_state.game = TicTacToe()
    st.session_state.game_over = False
    st.session_state.human_starts = human_starts
    
    if not human_starts:
        # AI makes first move
        ai_move = minimax(st.session_state.game, 0, True, 
                         st.session_state.ai_letter, st.session_state.human_letter)['position']
        st.session_state.game.make_move(ai_move, st.session_state.ai_letter)
        st.session_state.message = "AI went first! Your turn (X)"
    else:
        st.session_state.message = "Your turn! You are X"

def make_human_move(square):
    """Handle human move"""
    if not st.session_state.game_over and st.session_state.game.board[square] == ' ':
        # Human move
        st.session_state.game.make_move(square, st.session_state.human_letter)
        
        # Check if human won
        if st.session_state.game.current_winner == st.session_state.human_letter:
            st.session_state.game_over = True
            st.session_state.message = "🎉 You win!"
            st.session_state.wins['X'] += 1
            return
        
        # Check for tie
        if not st.session_state.game.empty_squares():
            st.session_state.game_over = True
            st.session_state.message = "🤝 It's a tie!"
            st.session_state.wins['Tie'] += 1
            return
        
        # AI move
        ai_move = minimax(st.session_state.game, 0, True, 
                         st.session_state.ai_letter, st.session_state.human_letter)['position']
        st.session_state.game.make_move(ai_move, st.session_state.ai_letter)
        
        # Check if AI won
        if st.session_state.game.current_winner == st.session_state.ai_letter:
            st.session_state.game_over = True
            st.session_state.message = "🤖 AI wins!"
            st.session_state.wins['O'] += 1
            return
        
        # Check for tie after AI move
        if not st.session_state.game.empty_squares():
            st.session_state.game_over = True
            st.session_state.message = "🤝 It's a tie!"
            st.session_state.wins['Tie'] += 1
            return
        
        st.session_state.message = "Your turn! You are X"

# Title
st.markdown('<p class="big-font">❌⭕ Tic-Tac-Toe vs AI</p>', unsafe_allow_html=True)
st.markdown("### Play against an unbeatable AI using the Minimax algorithm!")

# Sidebar
st.sidebar.header("🎮 Game Settings")

if st.sidebar.button("🔄 New Game (You Start)", use_container_width=True):
    reset_game(human_starts=True)
    st.rerun()

if st.sidebar.button("🤖 New Game (AI Starts)", use_container_width=True):
    reset_game(human_starts=False)
    st.rerun()

st.sidebar.markdown("---")

# Statistics
st.sidebar.markdown("### 📊 Statistics")
st.sidebar.metric("Your Wins (X)", st.session_state.wins['X'])
st.sidebar.metric("AI Wins (O)", st.session_state.wins['O'])
st.sidebar.metric("Ties", st.session_state.wins['Tie'])

if st.sidebar.button("🗑️ Reset Statistics", use_container_width=True):
    st.session_state.wins = {'X': 0, 'O': 0, 'Tie': 0}
    st.rerun()

st.sidebar.markdown("---")

with st.sidebar.expander("ℹ️ About"):
    st.markdown("""
    ### How to Play
    - You are **X**, AI is **O**
    - Click on any empty cell to make your move
    - Try to get 3 in a row (horizontal, vertical, or diagonal)
    - The AI uses the **Minimax algorithm** and is unbeatable!
    
    ### Minimax Algorithm
    The AI evaluates all possible game states to choose the optimal move:
    - Maximizes its own score
    - Minimizes opponent's score
    - Looks ahead to the end of the game
    - Chooses moves that lead to wins or ties
    
    **Challenge:** Can you tie with the AI? 🤔
    """)

# Main game area
col1, col2 = st.columns([3, 1])

with col1:
    # Display current message
    if st.session_state.game_over:
        if "win" in st.session_state.message.lower():
            if "You" in st.session_state.message:
                st.success(st.session_state.message)
            else:
                st.error(st.session_state.message)
        else:
            st.info(st.session_state.message)
    else:
        st.info(st.session_state.message)
    
    # Create 3x3 grid
    board = st.session_state.game.board
    
    for row in range(3):
        cols = st.columns(3)
        for col in range(3):
            square = row * 3 + col
            with cols[col]:
                cell_value = board[square]
                display = cell_value if cell_value != ' ' else '　'
                
                # Color based on player
                if cell_value == 'X':
                    label = f"**:blue[{display}]**"
                elif cell_value == 'O':
                    label = f"**:red[{display}]**"
                else:
                    label = display
                
                # Create button
                if st.button(
                    label,
                    key=f"btn_{square}",
                    disabled=st.session_state.game_over or cell_value != ' ',
                    use_container_width=True
                ):
                    make_human_move(square)
                    st.rerun()
    
    # Game over options
    if st.session_state.game_over:
        st.markdown("---")
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("🔄 Play Again (You Start)", type="primary", use_container_width=True):
                reset_game(human_starts=True)
                st.rerun()
        with col_b:
            if st.button("🤖 Play Again (AI Starts)", use_container_width=True):
                reset_game(human_starts=False)
                st.rerun()

with col2:
    st.markdown("### 📋 Board Key")
    st.markdown("""
    ```
    1 | 2 | 3
    ---------
    4 | 5 | 6
    ---------
    7 | 8 | 9
    ```
    """)
    
    st.markdown("### 🎯 Game Status")
    moves_made = 9 - st.session_state.game.num_empty_squares()
    st.metric("Moves Made", f"{moves_made}/9")
    
    if not st.session_state.game_over:
        st.progress(moves_made / 9)
    
    st.markdown("---")
    
    # Display current board state
    with st.expander("🔍 Board State"):
        board_str = ""
        for i in range(3):
            row = st.session_state.game.board[i*3:(i+1)*3]
            board_str += "| " + " | ".join([cell if cell != ' ' else ' ' for cell in row]) + " |\n"
        st.code(board_str)
    
    # Tips
    with st.expander("💡 Tips"):
        st.markdown("""
        - **Center**: Taking the center early is often a good strategy
        - **Corners**: Corners are stronger than edges
        - **Block**: Always block the AI's winning moves
        - **Fork**: Try to create two winning opportunities at once
        - **Think Ahead**: Consider what moves the AI will make
        """)

# Footer
st.markdown("---")
st.markdown("### 🧠 About the AI")
st.markdown("""
The AI uses the **Minimax algorithm**, a recursive algorithm used in decision-making and game theory.
It explores all possible future game states to choose the optimal move. The AI assumes both players play perfectly,
making it impossible to beat - the best you can do is tie! 
""")
