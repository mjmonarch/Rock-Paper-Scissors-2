# ------------------------------STAGE 1-----------------------------------------
VALID_CHOiCES = ['rock', 'paper', 'scissors']
UNFAIR_COMPUTER_TURN = {'paper': 'scissors', 'rock': 'paper', 'scissors': 'rock'}

while True:
    choice = input()
    if choice not in VALID_CHOiCES:
        continue
    print(f"Sorry, but the computer chose {UNFAIR_COMPUTER_TURN[choice]}")
    break
