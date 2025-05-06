import turtle

# === Step 1: User input ===
try:
    GRID_SIZE = int(input("Enter grid size (e.g., 5 for 5x5): "))
    CELL_SIZE = int(input("Enter cell size in pixels (e.g., 40): "))
except ValueError:
    print("Invalid input. Using default grid size 5 and cell size 40.")
    GRID_SIZE = 5
    CELL_SIZE = 40

# === Step 2: Input solution matrix ===
print("Enter your Nonogram solution row by row (0s and 1s separated by spaces):")
solution = []
for i in range(GRID_SIZE):
    while True:
        try:
            row = list(map(int, input(f"Row {i + 1}: ").strip().split()))
            if len(row) == GRID_SIZE and all(val in (0, 1) for val in row):
                solution.append(row)
                break
            else:
                print(f"Please enter exactly {GRID_SIZE} numbers (0 or 1).")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

# === Step 3: Setup ===
board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
puzzle_solved = False

screen = turtle.Screen()
screen.title("Nonogram Game")
screen.bgcolor("white")
screen.setup(width=GRID_SIZE * CELL_SIZE + 100, height=GRID_SIZE * CELL_SIZE + 100)

drawer = turtle.Turtle()
drawer.penup()
drawer.hideturtle()
drawer.speed(0)

# === Step 4: Drawing functions ===
def draw_grid():
    drawer.clear()
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = col * CELL_SIZE - GRID_SIZE * CELL_SIZE / 2
            y = GRID_SIZE * CELL_SIZE / 2 - row * CELL_SIZE
            draw_cell(x, y, board[row][col])

    global puzzle_solved
    if board == solution and not puzzle_solved:
        puzzle_solved = True
        drawer.goto(0, -GRID_SIZE * CELL_SIZE / 2 - 30)
        drawer.write("🎉 Puzzle Solved!", align="center", font=("Arial", 16, "bold"))

def draw_cell(x, y, filled):
    drawer.goto(x, y)
    drawer.setheading(0)
    drawer.pendown()
    for _ in range(4):
        drawer.forward(CELL_SIZE)
        drawer.right(90)
    drawer.penup()
    if filled:
        drawer.goto(x + CELL_SIZE / 2, y - CELL_SIZE)
        drawer.dot(CELL_SIZE - 5, "black")

# === Step 5: Click event ===
def click_handler(x, y):
    left = -GRID_SIZE * CELL_SIZE / 2
    right = GRID_SIZE * CELL_SIZE / 2
    top = GRID_SIZE * CELL_SIZE / 2
    bottom = -GRID_SIZE * CELL_SIZE / 2

    if left <= x <= right and bottom <= y <= top:
        col = int((x + GRID_SIZE * CELL_SIZE / 2) // CELL_SIZE)
        row = int((GRID_SIZE * CELL_SIZE / 2 - y) // CELL_SIZE)
        if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
            board[row][col] = 1 - board[row][col]
            draw_grid()

# === Step 6: Launch game ===
draw_grid()
screen.onclick(click_handler)
screen.mainloop()

