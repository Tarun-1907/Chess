import streamlit as st
import chess
import chess.svg

# Initialize session state
if "puzzle_index" not in st.session_state:
    st.session_state.puzzle_index = 0
if "puzzle_board" not in st.session_state:
    st.session_state.puzzle_board = None

# Chess puzzles in FEN notation
puzzles = [
    {"fen": "6k1/5ppp/8/8/8/8/5PPP/6K1 w - - 0 1", "solution": "g2g4"},  # Puzzle 1
    {"fen": "6k1/5ppp/8/8/8/8/5PPP/5RK1 w - - 0 1", "solution": "f1f6"},  # Puzzle 2
    {"fen": "8/8/8/8/4k3/4P3/5PPP/4K3 w - - 0 1", "solution": "e3e4"},  # Puzzle 3
    {"fen": "8/8/8/3k4/8/8/4PP2/4K3 w - - 0 1", "solution": "e2e3"},  # Puzzle 4
    {"fen": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", "solution": "e2e4"},  # Puzzle 5
    {"fen": "8/8/8/3k4/3P4/8/8/4K3 w - - 0 1", "solution": "d4d5"},  # Puzzle 6
    {"fen": "8/8/8/8/8/5k2/5P2/5K2 w - - 0 1", "solution": "f2f3"},  # Puzzle 7
    {"fen": "4k3/8/8/4p3/8/8/4P3/4K3 w - - 0 1", "solution": "e2e3"},  # Puzzle 8
    {"fen": "8/8/8/5k2/8/8/6P1/5K2 w - - 0 1", "solution": "g2g4"},  # Puzzle 9
    {"fen": "6k1/6pp/8/8/8/8/5PPP/6K1 w - - 0 1", "solution": "g2g3"},  # Puzzle 10
    {"fen": "8/8/8/8/8/4k3/3P4/4K3 w - - 0 1", "solution": "d2d3"},  # Puzzle 11
    {"fen": "4k3/8/8/8/3P4/8/8/4K3 w - - 0 1", "solution": "d4d5"},  # Puzzle 12
    {"fen": "8/8/8/8/4k3/4P3/5P2/5K2 w - - 0 1", "solution": "f2f3"},  # Puzzle 13
    {"fen": "6k1/5ppp/8/8/8/8/4PPPP/5K2 w - - 0 1", "solution": "f2f3"},  # Puzzle 14
    {"fen": "8/8/8/8/5k2/4P3/5PP1/6K1 w - - 0 1", "solution": "g2g3"},  # Puzzle 15
    {"fen": "8/8/8/4k3/8/8/5PP1/6K1 w - - 0 1", "solution": "g2g4"},  # Puzzle 16
    {"fen": "8/8/8/8/4k3/4P3/8/4K3 w - - 0 1", "solution": "e3e4"},  # Puzzle 17
    {"fen": "8/8/8/8/4k3/4P3/4K3/8 w - - 0 1", "solution": "e3e4"},  # Puzzle 18
    {"fen": "8/8/8/8/5k2/4P3/5PP1/6K1 w - - 0 1", "solution": "g2g3"},  # Puzzle 19
    {"fen": "8/8/8/8/8/5k2/5PP1/6K1 w - - 0 1", "solution": "g2g4"},  # Puzzle 20
    {"fen": "8/8/8/8/4k3/4P3/5K2/8 w - - 0 1", "solution": "e3e4"},  # Puzzle 21
    {"fen": "8/8/8/8/5k2/4P3/5PP1/6K1 w - - 0 1", "solution": "g2g3"},  # Puzzle 22
    {"fen": "8/8/8/8/8/4k3/4P3/4K3 w - - 0 1", "solution": "e3e4"},  # Puzzle 23
    {"fen": "8/8/8/4k3/8/4P3/4K3/8 w - - 0 1", "solution": "e3e4"},  # Puzzle 24
    {"fen": "8/8/8/8/5k2/4P3/5PP1/6K1 w - - 0 1", "solution": "g2g3"},  # Puzzle 25
    {"fen": "8/8/8/8/8/4k3/4P3/4K3 w - - 0 1", "solution": "e3e4"},  # Puzzle 26
    {"fen": "8/8/8/8/5k2/4P3/5PP1/6K1 w - - 0 1", "solution": "g2g4"},  # Puzzle 27
    {"fen": "8/8/8/8/4k3/4P3/5PP1/6K1 w - - 0 1", "solution": "f2f3"},  # Puzzle 28
]

# Sidebar menu for toggling between modes
menu = st.sidebar.radio("Choose Mode:", ["Play Chess", "Tutorial", "Practice Puzzles"])

if menu == "Practice Puzzles":
    st.title("Practice Chess Puzzles")
    st.write("Sharpen your skills by solving these puzzles!")

    # Select the current puzzle
    puzzle = puzzles[st.session_state.puzzle_index]
    if "puzzle_board" not in st.session_state or st.session_state.puzzle_board is None:
        st.session_state.puzzle_board = chess.Board(puzzle["fen"])

    # Render the puzzle board
    st.subheader(f"Puzzle {st.session_state.puzzle_index + 1}: Find the Winning Move")
    st.write("**White to move. Solve the puzzle!**")
    puzzle_svg = chess.svg.board(st.session_state.puzzle_board, size=400)
    st.markdown(
        f'<div style="text-align: center;">{puzzle_svg}</div>',
        unsafe_allow_html=True,
    )

    # Input solution
    move_input = st.text_input("Your Move (e.g., g2g4):")

    if st.button("Submit Solution"):
        try:
            move = chess.Move.from_uci(move_input)
            if move_input == puzzle["solution"]:
                st.success("Correct! Well done.")
                st.session_state.puzzle_index = (st.session_state.puzzle_index + 1) % len(puzzles)
                st.session_state.puzzle_board = chess.Board(puzzles[st.session_state.puzzle_index]["fen"])
            else:
                st.error("Incorrect. Try again or analyze the position.")
        except Exception as e:
            st.error(f"Invalid move format: {e}. Use UCI format (e.g., g2g4).")

    # Navigation for puzzles
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Previous Puzzle"):
            st.session_state.puzzle_index = (st.session_state.puzzle_index - 1) % len(puzzles)
            st.session_state.puzzle_board = chess.Board(puzzles[st.session_state.puzzle_index]["fen"])
    with col2:
        if st.button("Next Puzzle"):
            st.session_state.puzzle_index = (st.session_state.puzzle_index + 1) % len(puzzles)
            st.session_state.puzzle_board = chess.Board(puzzles[st.session_state.puzzle_index]["fen"])

elif menu == "Tutorial":
    st.title("Chess Tutorial and Winning Strategies")
    st.write("Learn the basics of chess, strategies, and tricks to dominate your opponent!")

    st.subheader("Chess Basics")
    st.write("""
    - **Objective**: Checkmate your opponent's king.
    - **Setup**: The board is 8x8 with alternating light and dark squares.
    - **Pieces**: Pawn, Rook, Knight, Bishop, Queen, and King. Each has unique movement rules.
    """)
    
     # How Pieces Move
    st.subheader("2. How Pieces Move")
    st.markdown("""
    - **Pawn**: Moves forward one square but captures diagonally.
    - **Knight**: Moves in an L-shape (two squares in one direction and one square perpendicular).
    - **Bishop**: Moves diagonally any number of squares.
    - **Rook**: Moves horizontally or vertically any number of squares.
    - **Queen**: Combines the power of a rook and bishop.
    - **King**: Moves one square in any direction.
    """)

    # # Display chessboard setup image
    # st.image(
    #     "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/ChessBoardInitialSetup.svg/800px-ChessBoardInitialSetup.svg.png",
    #     caption="Chessboard Setup",
    #     use_container_width=True
    # )

    # Special Moves
    st.subheader("3. Special Moves")
    st.markdown("""
    - **Castling**: A move involving the king and a rook to improve safety.
    - **En passant**: A special pawn capture.
    - **Pawn Promotion**: A pawn reaching the opponent's end of the board can be promoted to a queen, rook, bishop, or knight.
    """)

    # Strategies
    st.subheader("4. Strategies to Improve Your Game")
    st.markdown("""
    - **Control the Center**: Place your pawns and pieces to control the center squares (e4, d4, e5, d5).
    - **Develop Your Pieces**: Move your knights and bishops early to active squares.
    - **King Safety**: Castle early to protect your king.
    - **Avoid Moving the Same Piece Twice**: Unless necessary, develop all your pieces first.
    - **Create Threats**: Attack your opponent’s weak pieces or pawns.
    - **Think Ahead**: Always plan your moves and anticipate your opponent’s replies.
    """)

    # Tricks to Win
    st.subheader("5. Tricks to Win the Game")
    st.markdown("""
    - **Scholar’s Mate**: A four-move checkmate targeting the f7 or f2 square.
    - **Forks**: Use knights or other pieces to attack two pieces at once.
    - **Pins**: Pin a piece so it cannot move without exposing a more valuable piece behind it.
    - **Skewers**: Force a valuable piece to move, exposing another piece to capture.
    - **Sacrifices**: Sacrifice a piece for a stronger attack or to gain a material advantage.
    """)

    # Interactive Quiz
    st.subheader("6. Test Your Knowledge!")
    question = st.radio("Which piece moves in an 'L' shape?", ["Pawn", "Bishop", "Knight", "Queen"])
    if st.button("Submit Answer"):
        if question == "Knight":
            st.success("Correct! Knights move in an 'L' shape.")
        else:
            st.error("Incorrect! The correct answer is Knight.")

    st.subheader("Watch Video Tutorials")
    st.video("https://www.youtube.com/watch?v=NAIQyoPcjNM")  # Example: Beginner chess tutorial
    st.video("https://www.youtube.com/watch?v=E4F77emUnqQ")  # Example: Chess strategy for beginners

    # Strategies
    st.subheader("Winning Strategies and Tricks")
    st.markdown("""
    - **Tactical Tricks**: 
      - **Forks**: Use knights or other pieces to attack two pieces at once.
      - **Pins**: Pin a piece so it cannot move without exposing a more valuable piece behind it.
      - **Sacrifices**: Give up material for a stronger position or a checkmate attack.
    """)

elif menu == "Play Chess":
    st.title("Play Chess")
    st.write("Enjoy a responsive and interactive chess game!")

    # Initialize the chessboard
    if "board" not in st.session_state:
        st.session_state.board = chess.Board()
    if "history" not in st.session_state:
        st.session_state.history = []

    # Render the chessboard
    board_svg = chess.svg.board(st.session_state.board, size=600)
    st.markdown(
        f'<div style="text-align: center;">{board_svg}</div>',
        unsafe_allow_html=True,
    )

    # Input moves
    col1, col2 = st.columns(2)
    with col1:
        start_square = st.text_input("From (e.g., e2):", key="start", max_chars=2)
    with col2:
        end_square = st.text_input("To (e.g., e4):", key="end", max_chars=2)

    if st.button("Make Move"):
        try:
            move = chess.Move.from_uci(start_square + end_square)
            if move in st.session_state.board.legal_moves:
                st.session_state.board.push(move)
                st.session_state.history.append(str(move))
                st.success(f"Move made: {move}")
            else:
                st.error("Invalid move! Please try again.")
        except Exception as e:
            st.error(f"Invalid input: {e}. Please enter valid squares (e.g., e2e4).")

    # Game status
    if st.session_state.board.is_checkmate():
        st.success("Checkmate! Game over.")
    elif st.session_state.board.is_stalemate():
        st.info("Stalemate! Game over.")
    elif st.session_state.board.is_insufficient_material():
        st.info("Draw due to insufficient material.")
    else:
        st.markdown(f"**Turn:** {'White' if st.session_state.board.turn else 'Black'}")

    # Move history
    if st.session_state.history:
        st.subheader("Move History")
        st.write(", ".join(st.session_state.history))

    # Reset game
    if st.button("Reset Game"):
        st.session_state.board.reset()
        st.session_state.history.clear()
        st.success("Game reset successfully!")