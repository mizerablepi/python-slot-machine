from curses.ascii import isdigit
import random

MIN_BET = 1
MAX_BET = 100
MAX_LINES = 3
ROWS = 3
COLS = 3

symbols = {
    'A':1,
    'B':2,
    'C':4,
    'D':8
}

symbol_value={
    'A':8,
    'B':4,
    'C':3,
    'D':2
}

def get_spin(rows,cols,symbols):
    all_symbols = []
    for item, item_count in symbols.items():
        for _ in range(item_count):
            all_symbols.append(item)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_spin(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i < COLS - 1:
                print(col[row], end =' | ')
            else:
                print(col[row])
        

def deposit():
    while True:
        amount = input("Enter amount to be deposited: $")
        if amount.isdigit():
            amount = int(amount)
            if amount <= 0:
                print("Enter a amount greter than zero")
            else:
                break
        else:
            print("Enter a valid number!")
    
    return amount

def get_lines():
    while True:
        lines = input(f"Enter Number of lines to bet on (1-{MAX_LINES})")
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES :
                break
            else: 
                print(f"Enter a number between 1 to {MAX_LINES}!")
        else:
            print("Enter a valid number!")

    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else: 
                print(f"Number must be between {MIN_BET} and {MAX_BET}!")
        else:
            print("Enter a valid number!")

    return bet

def get_winnings(columns, lines, bet, symbol_value):
    winnings = 0
    winning_lines = []
    for row in range(lines):
        symbol = columns[0][row]
        for column in columns:
            symbol_to_check = column[row]
            if symbol != symbol_to_check:
                break
        else:
            winnings += symbol_value[symbol] * bet
            winning_lines.append(row+1)
    return winnings, winning_lines

def spin(amount):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > amount:
            print(f"You don't have enough money to bet. Balance: {amount} Bet: {total_bet}")
        else:
            break


    print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}")

    slots = get_spin(ROWS, COLS, symbols)
    print_spin(slots)
    winnings, winning_line = get_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings} on lines: ",*winning_line)

    return winnings - total_bet



def main():
    amount = deposit()
    while True:
        print(f"Current balance is ${amount}")
        ans = input("Press enter to play(q to quit)")
        if ans == 'q':
            break
        amount += spin(amount)
    print(f"You left with ${amount}")
    

main()