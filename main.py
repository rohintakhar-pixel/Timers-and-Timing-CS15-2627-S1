import time
import random

def reaction_game(attempts=5):
    print("Reaction Time Game")
    print("You will have", attempts, "attempts.")
    print("When you see GO! press Enter as fast as you can.\n")

    times = []
    for i in range(1, attempts + 1):
        input(f"Attempt {i}: Press Enter when you're ready to start...")
        wait = random.uniform(2, 5)
        time.sleep(wait)
        print("GO!")
        start = time.monotonic()
        input()
        end = time.monotonic()
        rt = end - start
        times.append(rt)
        print(f"Your reaction time: {rt:.3f} seconds\n")

    fastest = min(times)
    print("All attempts complete!")
    for idx, t in enumerate(times, 1):
        print(f"Attempt {idx}: {t:.3f} seconds")
    print(f"\nYour fastest reaction time: {fastest:.3f} seconds")

if __name__ == "__main__":
    reaction_game()



