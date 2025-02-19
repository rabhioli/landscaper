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

    # cutting grass with teeth
    if action == "cut grass":
        if "teeth" in tools:
            money += earnings["teeth"]
            print("You used your teeth to cut grass and earned $1!")
        else:
            print("You don't have any tools to cut grass with!")
    # buying scissors
    elif action == "buy tool":
        tool_to_buy = input("Which tool do you want to buy? ").lower()
        if tool_to_buy in tools_prices:
            if money >= tools_prices[tool_to_buy]:
                money -= tools_prices[tool_to_buy]
                tools.append(tool_to_buy)
                print(f"You bought {tool_to_buy} for ${tools_prices[tool_to_buy]}!")
            else:
                print("You don't have enough money to buy this tool.")
        else:
            print("Invalid tool.")
    # cutting grass with scissors
    elif action == "cut grass":
        if "teeth" in tools:
            money += earnings["teeth"]
            print("You used your teeth to cut grass and earned $1!")
        elif "scissors" in tools:
            money += earnings["scissors"]
            print("You used scissors to cut grass and earned $5!")
        else:
            print("You don't have any tools to cut grass with!")
    # buying lawnmower
    elif action == "buy tool":
        tool_to_buy = input("Which tool do you want to buy? ").lower()
        if tool_to_buy == "push lawnmower":
            if money >= tools_prices["push lawnmower"]:
                money -= tools_prices["push lawnmower"]
                tools.append("push lawnmower")
                print("You bought push lawnmower for $25!")
            else:
                print("You don't have enough money to buy push lawnmower.")
        else:
            print("Invalid tool.")
    # cutting grass with push lawnmower
    elif action == "cut grass":
        if "teeth" in tools:
            money += earnings["teeth"]
            print("You used your teeth to cut grass and earned $1!")
        elif "scissors" in tools:
            money += earnings["scissors"]
            print("You used scissors to cut grass and earned $5!")
        elif "push lawnmower" in tools:
            money += earnings["push lawnmower"]
            print("You used push lawnmower to cut grass and earned $50!")
        else:
            print("You don't have any tools to cut grass with!")
    # buying battery-powered lawnmower
    elif action == "buy tool":
        tool_to_buy = input("Which tool do you want to buy? ").lower()
        if tool_to_buy == "battery-powered lawnmower":
            if money >= tools_prices["battery-powered lawnmower"]:
                money -= tools_prices["battery-powered lawnmower"]
                tools.append("battery-powered lawnmower")
                print("You bought battery-powered lawnmower for $250!")
            else:
                print("You don't have enough money to buy battery-powered lawnmower.")
        else:
            print("Invalid tool.")
    # cutting grass with battery-powered lawnmower
    elif action == "cut grass":
        if "teeth" in tools:
            money += earnings["teeth"]
            print("You used your teeth to cut grass and earned $1!")
        elif "scissors" in tools:
            money += earnings["scissors"]
            print("You used scissors to cut grass and earned $5!")
        elif "push lawnmower" in tools:
            money += earnings["push lawnmower"]
            print("You used push lawnmower to cut grass and earned $50!")
        elif "battery-powered lawnmower" in tools:
            money += earnings["battery-powered lawnmower"]
            print("You used battery-powered lawnmower to cut grass and earned $100!")
        else:
            print("You don't have any tools to cut grass with!")
    # hiring team of starving students
    elif action == "buy tool":
        tool_to_buy = input("Which tool do you want to buy? ").lower()
        if tool_to_buy == "team of starving students":
            if money >= tools_prices["team of starving students"]:
                money -= tools_prices["team of starving students"]
                tools.append("team of starving students")
                print("You hired a team of starving students for $500!")
            else:
                print("You don't have enough money to hire a team.")
        else:
            print("Invalid tool.")
    # cutting grass with team of starving students and win scenario
    elif action == "cut grass":
        if "teeth" in tools:
            money += earnings["teeth"]
            print("You used your teeth to cut grass and earned $1!")
        elif "scissors" in tools:
            money += earnings["scissors"]
            print("You used scissors to cut grass and earned $5!")
        elif "push lawnmower" in tools:
            money += earnings["push lawnmower"]
            print("You used push lawnmower to cut grass and earned $50!")
        elif "battery-powered lawnmower" in tools:
            money += earnings["battery-powered lawnmower"]
            print("You used battery-powered lawnmower to cut grass and earned $100!")
        elif "team of starving students" in tools:
            money += earnings["team of starving students"]
            print("You hired a team of starving students to cut grass and earned $250!")
        else:
            print("You don't have any tools to cut grass with!")
    # the win scenario
    if money >= win_amount and "team of starving students" in tools:
        print("\nCongratulations! You've won the game!")
        break