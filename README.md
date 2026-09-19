# U.S. States Guessing Game

An educational Python game where you try to guess all 50 U.S. states.

A blank map of the United States is displayed, and whenever a correct state name is entered, the program places that state's name at its corresponding location on the map.

This project was built as part of my Python learning journey to strengthen my understanding of **Pandas, CSV files, Turtle graphics, coordinate positioning, conditional logic, lists, and program flow.**

---

## 🗺️ What the Game Does

The game starts with a blank map of the United States.

The player enters the name of a state through the Turtle screen.

- If the state is correct, its name is displayed on the map.
- If the state has already been guessed, it is not added again.
- The game continues asking for states until all 50 states have been guessed.
- The number of correctly guessed states is displayed while playing.

The goal is to identify all **50 U.S. states**.

---

## 🛠️ Technologies & Concepts Used

### Python
- Variables
- Lists
- `while` loops
- `if` conditions
- Membership checking using `in`
- String methods
- Functions
- Program execution flow

### Pandas
- Reading CSV files using `read_csv()`
- Working with DataFrames
- Filtering rows
- Extracting values from specific rows and columns

### Turtle Graphics
- Creating a Turtle screen
- Loading a map image as a Turtle shape
- Creating Turtle objects
- Positioning text using X/Y coordinates
- Writing text onto the screen

### Data Handling
- CSV-based state database
- State names paired with their corresponding X/Y coordinates
- Extracting the correct coordinates based on the user's answer

---

## 📂 Project Structure

```text
US_State_Guess_Game/
│
├── main.py
├── 50_states.csv
├── blank_states_img.gif
└── README.md

### `main.py`
Contains the main game logic, including user input, state validation, coordinate extraction, and displaying guessed states.

### `50_states.csv`
Contains the 50 U.S. state names along with their corresponding X and Y coordinates on the map.

### `blank_states_img.gif`
The blank U.S. map used as the background of the game.

---

## 🔄 How the Program Works

The basic program flow is:

1. Create the Turtle screen.
2. Load the blank U.S. map.
3. Read the state data from the CSV file using Pandas.
4. Create a list containing all state names.
5. Create an empty list for correctly guessed states.
6. Ask the player to enter a state name.
7. Check whether the answer:
   - exists in the list of states, and
   - has not already been guessed.
8. Find the corresponding row in the Pandas DataFrame.
9. Extract that state's X and Y coordinates.
10. Create a Turtle object and write the state name at those coordinates.
11. Repeat until all 50 states have been guessed.

---

## 🧩 Key Problem-Solving Challenges

### 1. Connecting a State Name to Its Position

One of the main challenges was figuring out how to take a user's answer and determine **where that state should appear on the map**.

I solved this by storing each state's name together with its X and Y coordinates in a CSV file.

After checking that the answer was valid, I filtered the DataFrame to find the row corresponding to that state and extracted its coordinates.

The coordinates were then passed to Turtle to display the state name at the correct location.

---

### 2. Keeping Track of Correct Guesses

I needed a way to prevent a correctly guessed state from being displayed multiple times.

I created a `guessed_states` list and checked whether the entered state was already present before processing it.

This helped me understand how lists can be used as part of a program's state and logic.

---

### 3. Deciding When the Game Should Continue

Another challenge was determining how the program should continuously ask for guesses and when it should stop.

I used a `while` loop:

```python
while len(guessed_states) < len(all_states):
```

This means the game continues as long as the number of correctly guessed states is smaller than the total number of states.

Once all 50 states have been guessed, the condition becomes false and the loop ends.

---

## 📍 Creating the Coordinate Data

The state coordinates were not simply available as part of the original program.

I created a separate coordinate-extraction program using Turtle's mouse-click functionality.

By clicking on the approximate location of each state on the map, I could obtain its **X and Y coordinates**.

I then organized the state names and coordinates into the CSV file used by the main program.

This gave me practical experience in connecting **manually collected data with a Python program**.

---

## 🧠 What I Learned

This project helped me strengthen several technical concepts, but the biggest learning was developing a more structured **programming mindset**.

I practiced thinking in terms of:

**Input → Condition → Data → Action → Output → Repeat**

Instead of only thinking about individual lines of code, I had to think about:

- What should happen?
- When should it happen?
- What condition should trigger it?
- What data is required?
- Where should the result be displayed?
- When should the program stop?

This helped me understand how individual Python concepts combine to create a complete program.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-link>
```

### 2. Install Pandas

```bash
pip install pandas
```

### 3. Make sure these files are in the same folder

```text
main.py
50_states.csv
blank_states_img.gif
```

### 4. Run the program

```bash
python main.py
```

---

## 🎮 How to Play

1. Run the program.
2. Enter the name of a U.S. state when prompted.
3. If the answer is correct, the state name will appear on the map.
4. Continue guessing until you identify all 50 states.

If you cannot identify all of them, the program can also be extended to generate a list of the states that were not guessed.

---

## 🚀 Future Improvements

Possible improvements I could add in the future:

- Display the final score.
- Show the states that were missed.
- Add a timer.
- Add a restart option.
- Improve the user interface.
- Add different difficulty levels.
- Add more geographical quiz modes.

