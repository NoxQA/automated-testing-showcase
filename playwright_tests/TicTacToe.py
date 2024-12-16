from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context()
    page = browser.new_page()
    page.goto("https://playtictactoe.org/")

    table = page.locator('.board')
    squares = table.locator('.square')

    board_state = ["", "", "", "", "", "", "", "", ""]

    def update_board_state():
        global board_state
        for i in range(squares.count()):
            square = squares.nth(i)
            if square.locator('.x').count() > 0:
                board_state[i] = "X"
            elif square.locator('.o').count() > 0:
                board_state[i] = "0"
            else:
                board_state[i] = ""
        print("Updated Board State:", board_state)

    winning_patterns = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    def find_best_move(board_state, player_symbol, opponent_symbol):
        for pattern in winning_patterns:
            if (
                board_state[pattern[0]] == player_symbol and
                board_state[pattern[1]] == player_symbol and
                board_state[pattern[2]] == ""
            ):
                return pattern[2]
            if (
                board_state[pattern[0]] == player_symbol and
                board_state[pattern[2]] == player_symbol and
                board_state[pattern[1]] == ""
            ):
                return pattern[1]
            if (
                board_state[pattern[1]] == player_symbol and
                board_state[pattern[2]] == player_symbol and
                board_state[pattern[0]] == ""
            ):
                return pattern[0]

        for pattern in winning_patterns:
            if (
                board_state[pattern[0]] == opponent_symbol and
                board_state[pattern[1]] == opponent_symbol and
                board_state[pattern[2]] == ""
            ):
                return pattern[2]
            if (
                board_state[pattern[0]] == opponent_symbol and
                board_state[pattern[2]] == opponent_symbol and
                board_state[pattern[1]] == ""
            ):
                return pattern[1]
            if (
                board_state[pattern[1]] == opponent_symbol and
                board_state[pattern[2]] == opponent_symbol and
                board_state[pattern[0]] == ""
            ):
                return pattern[0]

        if board_state[4] == "":
            return 4

        for corner in [0, 2, 6, 8]:
            if board_state[corner] == "":
                return corner

        for side in [1, 3, 5, 7]:
            if board_state[side] == "":
                return side

        return None

    def make_move(move):
        if move is not None:
            squares.nth(move).click()
            print(f"Making move at position {move}")

    def restart_game():
        restart_button = page.locator('.restart')
        if restart_button.is_visible():
            restart_button.click()
            print("Game restarted.")

    def get_current_scores():
        player1_score = int(page.locator('.player1 .score').inner_text())
        ties_score = int(page.locator('.ties .score').inner_text())
        player2_score = int(page.locator('.player2 .score').inner_text())
        return player1_score, ties_score, player2_score

    def update_scores(player1_score, ties_score, player2_score):
        print(f"Player 1 Score: {player1_score}")
        print(f"Ties Score: {ties_score}")
        print(f"Player 2 Score: {player2_score}")

    def check_game_over():
        for pattern in winning_patterns:
            if board_state[pattern[0]] == board_state[pattern[1]] == board_state[pattern[2]] and board_state[pattern[0]] != "":
                return True

        if all(cell != "" for cell in board_state):
            return True

        return False

    player_symbol = "X"
    opponent_symbol = "0"

    player1_score = 0
    player2_score = 0
    ties_score = 0

    for game in range(5):
        print(f"Starting Game {game + 1}")
        board_state = ["", "", "", "", "", "", "", "", ""]

        while not check_game_over():
            best_move = find_best_move(board_state, player_symbol, opponent_symbol)
            make_move(best_move)

            time.sleep(2)

            update_board_state()

            player_symbol, opponent_symbol = opponent_symbol, player_symbol

            time.sleep(1)

        if check_game_over():
            if board_state == ["X", "X", "X", "", "", "", "", "", ""]:
                player1_score += 1
            elif board_state == ["", "", "", "X", "X", "X", "", "", ""]:
                player1_score += 1
            elif board_state == ["", "", "", "", "", "", "X", "X", "X"]:
                player1_score += 1
            elif board_state == ["", "X", "", "X", "", "X", "", "", ""]:
                player1_score += 1
            elif board_state == ["", "", "", "0", "0", "0", "", "", ""]:
                player2_score += 1
            elif board_state == ["X", "", "", "", "X", "", "", "", "X"]:
                player2_score += 1
            else:
                ties_score += 1

        restart_game()

        update_scores(player1_score, ties_score, player2_score)

        time.sleep(2)

    browser.close()
