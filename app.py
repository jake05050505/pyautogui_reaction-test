import pyautogui as pag

def main():
    print("Running! Click the reaction test to start.")

    for _ in range(5):
        try:
            while True:
                if pag.pixel(*pag.position()) == (75, 219, 106):
                    pag.doubleClick()
                    break
        except KeyboardInterrupt:
            print("Cancelled")
            break

    return 0

if __name__ == "__main__":
    main()