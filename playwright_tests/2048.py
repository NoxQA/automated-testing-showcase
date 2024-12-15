from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context()
    page = browser.new_page()

    page.goto("https://www.2048.org")

    MOVES = ["ArrowUp", "ArrowRight", "ArrowDown", "ArrowLeft"]

    game_board = page.locator('.game-container')

    end_time = time.time() + 240  # Run for 240 seconds?

    try:
        while time.time() < end_time:
            for move in MOVES:
                game_board.press(move)
                time.sleep(0.1)

                if "game-over" in page.inner_html('.game-container'):
                    print("Game Over!")
                    break

            score = page.locator('.score-container').inner_text()
            print(f"Current Score: {score}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        browser.close()
