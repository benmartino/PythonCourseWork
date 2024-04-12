#Project 4 - Ben Martino - 4/5/2024
import random
def get_word()->str:
    all_words = ['above','blame','corny','dress','email','flail','glass','horse','igloo','judge','kebab','lilac','moose','never','olive','prize','query','react','shrub','toxic','untie','vigor','wordl','yield','zesty']
    my_word = random.choice(all_words)
    return my_word

def get_guess()->str:
    user_input = input("Your Guess: ")
    guess = user_input.lower()
    return guess

def get_guess_extra()->str:
    user_input = input("Your Guess: ")
    while len(user_input) != 5 or user_input.isalpha() == False:
        print(f"{user_input} is an invalid guess")
        user_input = input("try again: ")
        continue
    else:
        guess = user_input.lower()
        return guess

def print_guess(guess:str)->None: #This is incomplete
    i = 0
    value = ''
    while i < len(guess):
        value = value + guess[i] + "  "
        i = i+1
    print(value)

def get_diff(ans:str, guess:str) ->list:
    i = 0
    diffs = []
    while i < len(ans):
        if ans[i] == guess[i]:
            diffs.append('g')
            i = i+1
        elif guess[i] in ans:
            diffs.append('y') 
            i = i+1
        else:
            diffs.append('r')
            i = i+1
    return diffs

def print_diff(list)->None:
    to_print = ''
    i = 0
    while i < len(list):
        if list[i] == 'g':
            to_print = to_print + "🟢 "
            i = i+1
        elif list[i] == 'y':
            to_print = to_print + "🟡 "
            i = i+1
        else:
            to_print = to_print + "🔴 "
            i = i+1
    print(to_print)

def play_turn(ans:str)->bool:
    guess = get_guess_extra()
    print_guess(guess)
    list = get_diff(ans,guess)
    print_diff(list)
    if ans == guess:
        return True
    else:
        return False

def play_game()->None:
    correct_word = get_word()
    has_won = False
    turn = 0
    while has_won == False:
        turn +=1
        if turn == 7:
            print(f"Out of turns, the word was: {correct_word}")
            break
        else:  
            print(f"\nTURN {turn}:")
            has_won = play_turn(correct_word)
            continue
    else:
        print(f"you've won! it took {turn} turns")
        return None


if __name__ == '__main__':
    play_game()
   
    
