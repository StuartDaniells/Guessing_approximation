from random import randint
rand_num = randint(1,100)

guesses = 0


while True:
    
    winning_num = int(input("Guess the winning number... \n [ONLY NUMBERS]:\t"))
    
    
    if winning_num < 1 or winning_num > 100:
        guesses += 1
        print('\t\t---> Out of Boounds \n')
        continue

    elif winning_num in range(rand_num-2 , rand_num + 2) and winning_num != rand_num:
        guesses += 1
        print('\t\t---> Very very Close! \n')
        continue
        
    elif winning_num in range(rand_num-5 , rand_num + 5) and winning_num != rand_num:
        guesses += 1
        print('\t\t---> Very Close! \n')
        continue

    elif winning_num in range(rand_num-10 , rand_num + 11) and winning_num != rand_num:
        guesses += 1
        print('\t\t---> Close! \n')
        continue

    elif winning_num in range(rand_num-20 , rand_num + 21) and winning_num != rand_num:
        guesses += 1
        print('\t\t---> Warmer! \n')
        continue

    elif winning_num in range(rand_num-30 , rand_num + 31) and winning_num != rand_num:
        guesses += 1
        print('\t\t---> Warm! \n')
        continue

    elif winning_num in range(rand_num-50 , rand_num + 51) and winning_num != rand_num:
        guesses += 1
        print('\t\t---> Cold! \n')
        continue

    elif winning_num not in range(rand_num-50 , rand_num + 51) and winning_num != rand_num:
        guesses += 1
        print('\t\t---> Very Cold! \n')
        continue     

    elif winning_num == rand_num:
        guesses += 1
        print(f'\n\n\t\t------------------- Congratulations!! you got it in {guesses} guesses -------------------\n\n')
        break

    # This part doesn't work since the input (in the variable "winning_num") is being forced as an Integer
    
    else:
        print("----------------> Please enter a valid number <----------------")
        continue