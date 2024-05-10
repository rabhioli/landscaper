# Initialize variables
money = 0
tools = []
tools_prices = {
    "teeth": 0,
    "scissors": 5,
    "push lawnmower": 25,
    "battery-powered lawnmower": 250,
    "team of starving students": 500
}
earnings = {
    "teeth": 1,
    "scissors": 5,
    "push lawnmower": 50,
    "battery-powered lawnmower": 100,
    "team of starving students": 250
}
win_amount = 1000

# status
def display_status():
    print(f"\nYou have ${money}. Your tools: {', '.join(tools)}")

# game loop
while True:
    display_status()
    action = input("\nWhat do you want to do? (cut grass/buy tool/quit): ").lower()
