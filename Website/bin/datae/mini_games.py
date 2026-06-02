import random

def tic_tac_toe():
    board = [" "] * 9
    def show():
        for i in range(0, 9, 3):
            print(" {} | {} | {} ".format(board[i], board[i+1], board[i+2]))
            if i < 6: print("---+---+---")
    def winner():
        wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for a, b, c in wins:
            if board[a] != " " and board[a] == board[b] == board[c]:
                return board[a]
        if " " not in board: return "Tie"
        return None
    print("Tic Tac Toe! You are X, computer is O. Enter 1-9.")
    show()
    while True:
        try:
            move = int(input("Your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid."); continue
        except: print("Invalid."); continue
        board[move] = "X"
        w = winner()
        if w: show(); print("Result: {}".format("You win!" if w == "X" else "Tie!" if w == "Tie" else "")); return
        empty = [i for i in range(9) if board[i] == " "]
        if not empty: show(); print("Tie!"); return
        board[random.choice(empty)] = "O"
        w = winner()
        if w: show(); print("Result: {}".format("Computer wins!" if w == "O" else "Tie!")); return
        show()

def connect_four():
    rows, cols = 6, 7
    grid = [[" "] * cols for _ in range(rows)]
    def show():
        print("\n".join("|" + "|".join(row) + "|" for row in grid))
        print(" " + " ".join(str(i+1) for i in range(cols)))
    def drop(col, piece):
        for r in range(rows-1, -1, -1):
            if grid[r][col] == " ":
                grid[r][col] = piece; return r
        return -1
    def check(r, c, piece):
        for dr, dc in [(0,1),(1,0),(1,1),(1,-1)]:
            count = 0
            for i in range(-3, 4):
                nr, nc = r + dr*i, c + dc*i
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == piece:
                    count += 1
                    if count == 4: return True
                else: count = 0
        return False
    print("Connect Four! You are X, computer is O. Enter column 1-7.")
    show()
    for turn in range(rows * cols):
        if turn % 2 == 0:
            try:
                col = int(input("Column (1-7): ")) - 1
                if col < 0 or col >= cols or grid[0][col] != " ": print("Invalid."); continue
            except: print("Invalid."); continue
            r = drop(col, "X")
            if check(r, col, "X"): show(); print("You win!"); return
        else:
            empty = [c for c in range(cols) if grid[0][c] == " "]
            col = random.choice(empty)
            r = drop(col, "O")
            if check(r, col, "O"): show(); print("Computer wins!"); return
        show()
    print("Tie!")

def word_search_puzzle():
    words = ["python", "java", "ruby", "swift", "kotlin", "rust", "go", "php", "perl", "dart"]
    target = random.choice(words)
    scrambled = list(target)
    random.shuffle(scrambled)
    print("Find the programming language: " + "".join(scrambled))
    for _ in range(3):
        g = input("Guess: ").lower()
        if g == target: print("Correct!"); return
        print("Wrong.")
    print("Answer: {}".format(target))

def number_puzzle():
    target = random.randint(100, 999)
    digits = [int(d) for d in str(target)]
    print("I'm thinking of a 3-digit number. The digits are: {} {} {}".format(digits[0], digits[1], digits[2]))
    print("Can you guess the order?")
    for _ in range(5):
        try:
            g = int(input("Guess (3-digit number): "))
            if g == target: print("Correct!"); return
            gd = [int(d) for d in str(g).zfill(3)]
            correct_pos = sum(1 for a,b in zip(gd, digits) if a == b)
            print("{} digits in correct position.".format(correct_pos))
        except: print("Invalid.")
    print("Answer: {}".format(target))

def memory_challenge():
    seq = []
    print("Memory challenge! Remember the sequence of numbers.")
    while True:
        seq.append(random.randint(0, 9))
        print("Sequence: " + " ".join(str(x) for x in seq))
        try:
            g = input("Enter the sequence (space separated): ").strip()
            if not g: break
            gs = [int(x) for x in g.split()]
            if gs == seq: print("Correct! Next round...")
            else: print("Wrong! Game over. Length: {}".format(len(seq)-1)); return
        except: print("Invalid.")

def reaction_game():
    import time
    print("Reaction game! Press Enter when you see GO...")
    input("Press Enter when ready...")
    delay = random.uniform(1, 5)
    time.sleep(delay)
    start = time.time()
    input("GO! Press Enter NOW! ")
    reaction = time.time() - start
    print("Your reaction time: {:.3f} seconds".format(reaction))
    if reaction < 0.2: print("Amazing reflexes!")
    elif reaction < 0.3: print("Great!")
    elif reaction < 0.5: print("Good.")
    else: print("You can do better!")

def guess_the_number_advanced():
    import math
    low, high = 1, 1000
    print("Think of a number between {} and {}.".format(low, high))
    input("Press Enter when ready...")
    attempts = 0
    while low <= high:
        mid = (low + high) // 2
        attempts += 1
        print("Is it {}?".format(mid))
        resp = input("(h)igher, (l)ower, (c)orrect: ").lower()
        if resp == "c": print("Got it in {} tries!".format(attempts)); return
        if resp == "h": low = mid + 1
        elif resp == "l": high = mid - 1
    print("You cheated!")

def word_association():
    chains = [
        "cat", "dog", "bone", "tree", "leaf", "wind", "storm", "rain", "water",
        "sky", "blue", "ocean", "wave", "sand", "beach", "sun", "hot", "fire",
    ]
    current = random.choice(chains)
    used = []
    print("Word Association. Say a word related to '{}'.".format(current))
    for _ in range(20):
        w = input("Your word: ").strip().lower()
        if w in used: print("Already used."); continue
        used.append(w)
        if w in chains or w[-2:] in ["er","ly","ed","ing"]:
            print("Good! Next: {}".format(w))
        else:
            print("Not a good association. Score: {}".format(len(used)-1)); return
    print("Great! Perfect score!")

def rapid_math():
    print("Rapid Math! Solve as fast as you can.")
    import time
    score = 0
    start = time.time()
    for _ in range(10):
        a = random.randint(10, 99)
        b = random.randint(10, 99)
        op = random.choice(["+", "-"])
        ans = a + b if op == "+" else a - b
        try:
            g = int(input("{} {} {} = ".format(a, op, b)))
            if g == ans: score += 1
        except: pass
    elapsed = time.time() - start
    print("Score: {}/10 in {:.1f}s".format(score, elapsed))
