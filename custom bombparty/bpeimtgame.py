from time import sleep, strftime, gmtime
from datetime import datetime
import threading
import random
import sys
import os










# --------------------------- CUSTOM FUNCTIONS ---------------------------



def clear_screen():
    # Check if the operating system is Windows
    if os.name == 'nt':
        os.system('cls')

    # If it is not Windows (Mac/Linux), run this instead
    else:
        os.system('clear')



def check():
    global valid
    valid = None

    if mode == 'single':
        if len(ans) >= minimum:
            if morpheme.lower() in ans.lower():
                if ans.lower() in words:
                    if repetition_allowed:   
                        valid = True
                    else:
                        if ans.lower() not in used:
                            valid = True
                        else:
                            valid = False
                else:
                    valid = False 
            else:
                valid = False
        else:
            valid = False
    
    else:
        if len(ans) >= minimum:
            if morpheme.lower() in ans.lower():
                if ans.lower() in words:
                    if repetition_allowed:   
                        valid = True

                    else:
                        if gamemode == gamemodes[2]:
                            if ans.lower() not in used:
                                valid = True
                            else:
                                valid = False

                        else:
                            if ans.lower() not in players[i]['used']:
                                valid = True
                            else:
                                valid = False
                else:
                    valid = False 
            else:
                valid = False
        else:
            valid = False



def timecheck(player_specific=False):
    global timer
    global start

    if not player_specific:
        if (datetime.now() - start).total_seconds() <= timer:
            return False
        else:
            return True
    
    else:
        if (datetime.now() - start).total_seconds() <= players[current_player]['time']:
            return False
        else:
            return True










# ------------------------- WORDS AND MORPHEMES -------------------------



words = set()
with open('custom bombparty/dict.txt') as f:
    for line in f:
        for item in line.split(","):
            item = item.strip().strip('"')
            if item:
                words.add(item.lower())



morphemes = []
with open('custom bombparty/morphemes.txt') as f:
    for line in f:
        for item in line.split(","):
            item = item.strip().strip('"')
            if item:
                morphemes.append(item)










# ------------------------------- START SCREEN -------------------------------



clear_screen()
modes = ['single', 'multi']
print('                           ___________________')
print('==========================| CUSTOM BOMB PARTY |==========================')
print('                           ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print('Welcome! Choose a mode:')
print('    - Single')
print('    - Multi')
print()
mode = input('> ').lower()



while mode not in modes:
    print('That\'s not a mode! Please pick one of the modes above!')
    mode = input('> ').lower()



clear_screen()










# ---------------------------- SETTINGS (SINGLEPLAYER) ----------------------------



if mode == 'single':
    lives = 2
    timer = 10
    minimum = 0
    repetition_allowed = False
    decay = True



    while True:
        print('                              ______________')
        print('=============================| SINGLEPLAYER |=============================')
        print('                              ‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
        print('Here you can change your settings!')
        print(f'    1 - Lives: {lives}')
        print(f'    2 - Starting Time: {timer} seconds')
        print(f'    3 - Minimum Word Length: {minimum} letters')
        print(f'    4 - Allow Word Repetition? {repetition_allowed}')
        print(f'    5 - Time Decay? {decay}')
        print()
        print('You may alter any settings by typing their respective number. For example, if you want to change how many lives you get, type "1".')
        print('If you want to start with these settings, type "start".')
        query = input('> ').lower()



        options = ['1', '2', '3', '4', '5', 'start']



        while query not in options:
            print('That\'s not an option! Try again.')
            query = input('> ').lower()
        


        print()
        if query == '1':
            print('How many lives would you like?')
            query = input('> ')



            while True:
                try:
                    if int(query) < 1:
                        print('You must have atleast 1 life. Try again.')
                        query = input('> ')
                        continue

                    lives = int(query)
                    break

                except:
                    print('That\'s not a number! Please type a number.')
                    query = input('> ')
        


        elif query == '2':
            print('How much time would you like to start with, in seconds?')
            query = input('> ')



            while True:
                try:
                    if int(query) < 1:
                        print('Time cannot be less than 1. Type a higher number.')
                        query = input('> ')
                        continue

                    timer = int(query)
                    break

                except:
                    print('That\'s not a number! Please type a number.')
                    query = input('> ')  



        elif query == '3':
            print('What would you like the minimum length of your answers to be? Maximum of 8.')
            query = input('> ')



            while True:
                try:
                    if int(query) > 8:
                        print('Minimum word length cannot exceed 8. Type a lower number.')
                        query = input('> ')
                        continue
                    
                    elif int(query) < 0:
                        print('Minimum word length cannot be less than 0. Type a higher number.')
                        query = input('> ')
                        continue

                    minimum = int(query)
                    break

                except:
                    print('That\'s not a number! Please type a number.')
                    query = input('> ')



        elif query == '4':
            if repetition_allowed:
                repetition_allowed = False
                print('Word repetition has been disabled.')

            elif not repetition_allowed:
                repetition_allowed = True
                print('Word repetition has been enabled.')
            


            sleep(1)
        


        elif query == '5':
            if decay:
                decay = False
                print('Time decay has been disabled.')

            elif not decay:
                decay = True
                print('Time decay has been enabled.')
            


            sleep(1)
        


        elif query == 'start':
            break
        


        print()
        print('Your settings have been updated!')
        sleep(2)
        clear_screen()










# ---------------------------- SETTINGS (MULTIPLAYER) ----------------------------



elif mode == 'multi':
    gamemodes = ['Hot Potato', 'Time Attack', 'Co-op']
    gamemode = gamemodes[0]
    player_count = 2
    lives = 2
    timer = 30
    minimum = 0
    repetition_allowed = False



    players = {
        1: {},
        2: {}
    }



    while True:
        if gamemode == gamemodes[1]:
            lives = 1



        print('                              _____________')
        print('=============================| MULTIPLAYER |=============================')
        print('                              ‾‾‾‾‾‾‾‾‾‾‾‾‾')
        print('Here you can change your settings!')
        print(f'    1 - Gamemode: {gamemode}')
        print(f'    2 - # of Players: {player_count}')
        print(f'    3 - Lives: {lives}')
        print(f'    4 - Starting Time: {timer} seconds')
        print(f'    5 - Minimum Word Length: {minimum} letters')
        print(f'    6 - Allow Word Repetition? {repetition_allowed}')
        print()
        print('You may alter any settings by typing their respective number. For example, if you want to change how many lives you get, type "3".')
        print('If you want to start with these settings, type "start".')
        query = input('> ').lower()



        options = [1, 2, 3, 4, 5, 6, 7, 'start']



        try:
            query = int(query)

        except:
            pass



        while query not in options:
            print('That\'s not an option! Try again.')
            query = input('> ').lower()
        


        print()
        if query == 1:
            print('Choose one of the following gamemodes by typing their respective number.')
            print('    1 - Hot Potato - Classic BombParty. One timer for all players, and whoever the timer runs out on loses a life. This mode has buffer time (5s).')
            print('    2 - Time Attack - Each player has one timer each, whoever runs out of time first loses (One life per player). This mode does not have buffer time.')
            print('    3 - Co-op - Players share lives and timer, answer as many words as possible. This mode has buffer time (5s).')
            query = input('> ').lower()



            while True:
                try:
                    if (int(query) < 1) or (int(query) > len(gamemodes)):
                        print('There are no choices with that number. Try again.')
                        query = input('> ').lower()
                        continue
                    
                    gamemode = gamemodes[int(query) - 1]
                    break

                except:
                    print('That\'s not an option! Try again.')
                    query = input('> ').lower()
        


        elif query == 2:
            print('How many players will be playing?')
            query = input('> ').lower()

            while True:
                try:
                    if int(query) < 2:
                        print('You cannot have less than 2 players. Try again.')
                        query = input('> ').lower()
                        continue
                    
                    player_count = int(query)
                    break

                except:
                    print('That\'s not a number! Please type a number.')
                    query = input('> ')
        


        if query == 3:
            if gamemode == gamemodes[1]:
                print('In the Time Attack gamemode, all players only have 1 life. If you want to change this, set a different gamemode.')
                sleep(5)
                clear_screen()
                continue



            print('How many lives would you like?')
            query = input('> ')



            while True:
                try:
                    if int(query) < 1:
                        print('You must have atleast 1 life. Try again.')
                        query = input('> ')
                        continue

                    lives = int(query)
                    break

                except:
                    print('That\'s not a number! Please type a number.')
                    query = input('> ')
        


        elif query == 4:
            print('How much time would you like to start with, in seconds?')
            query = input('> ')

            while True:
                try:
                    if int(query) < 1:
                        print('Time cannot be less than 1. Type a higher number.')
                        query = input('> ')
                        continue

                    timer = int(query)
                    break

                except:
                    print('That\'s not a number! Please type a number.')
                    query = input('> ')  



        elif query == 5:
            print('What would you like the minimum length of your answers to be? Maximum of 8.')
            query = input('> ')

            while True:
                try:
                    if int(query) > 8:
                        print('Minimum word length cannot exceed 8. Type a lower number.')
                        query = input('> ')
                        continue
                    
                    elif int(query) < 0:
                        print('Minimum word length cannot be less than 0. Type a higher number.')
                        query = input('> ')
                        continue

                    minimum = int(query)
                    break

                except:
                    print('That\'s not a number! Please type a number.')
                    query = input('> ')



        elif query == 6:
            if repetition_allowed:
                repetition_allowed = False
                print('Word repetition has been disabled.')
                
            elif not repetition_allowed:
                repetition_allowed = True
                print('Word repetition has been enabled.')
            


            sleep(1)
        


        elif query == 'start':
            break       
        


        print()
        print('Your settings have been updated!')
        sleep(2)
        clear_screen()
    


    if player_count > 2:
        for i in range(3, player_count + 1):
            players[i] = {}



    if gamemode == gamemodes[2] and not repetition_allowed:
        used = set()



    for i in players:
        if gamemode == gamemodes[1]:
            players[i]['time'] = timer
        
        if gamemode != gamemodes[2]:
            players[i]['lives'] = lives

        if not repetition_allowed:
            if gamemode != gamemodes[2]:
                players[i]['used'] = set()



    print()










# --------------------------------- GAME (SINGLEPLAYER) ---------------------------------



if mode == 'single':
    clear_screen()



    ans = None
    answers = 0



    if not repetition_allowed:
        used = []



    print('Type "/quit" at anytime to exit. You may also type "/skip" to skip a word, with a penalty of losing half a second.')
    print('Press enter to start.')
    input('> ')



    while lives > 0:
        clear_screen()



        start = datetime.now()
        morpheme = random.choice(morphemes)
        print(f'Within {timer} seconds, type a word containing {morpheme.upper()}.')
        ans = input('> ')



        check()



        while not valid:
            if timecheck():
                break

            if not repetition_allowed:
                if ans.lower() in used:
                    time_left = round(timer - ((datetime.now() - start).total_seconds()), 1)
                    print(f'You\'ve already used this word. You have {time_left} seconds left.')
                    print(f'Type another word containing {morpheme.upper()}')
                    ans = input('> ')

                    check()
            


            clear_screen()
            if ans == '/quit':
                sys.exit()

            elif ans == '/skip':
                timer -= 0.4
                break

            else:
                time_left = round(timer - ((datetime.now() - start).total_seconds()), 1)

                if time_left <= 0:
                    break

                print(f'Invalid word. You have {time_left} seconds left.')
                print(f'Type a word containing {morpheme.upper()}')
                ans = input('> ')

                check()



        if timecheck():
            lives -= 1

            if lives > 0:
                clear_screen()

                print('Too late. You\'ve lost a life.')
                print(f'You now have {lives} lives remaining.')
                print(f'Press enter to resume. You will have {timer} seconds left.')
                input('> ')
                continue

            else:
                break
        


        if not repetition_allowed:
            if ans != '/skip':
                used.append(ans)



        answers += 1



        if decay:
            timer -= 0.1
            
            timer = round(timer, 1)










# ------------------------------------ GAME OVER (SINGLEPLAYER) ------------------------------------



    clear_screen()



    print(f'Too late. You have run out of lives and lost! You gave {answers} valid words. Nice try!')
    sys.exit()










# ----------------------------------- GAME (MULTIPLAYER -- HOT POTATO) -------------------------------------



elif mode == 'multi':
    while True:
        clear_screen()



        ans = None
        answers = 0
        timer_start = timer



        print('Type "/quit" at anytime to exit. You may also type "/skip" to skip a word, with a penalty of losing half a second.')
        print('Press enter to start.')
        input('> ')



        if gamemode == gamemodes[0]:
            game_start = datetime.now()
            turn_order = list(players.keys())



            while True:
                current_player = turn_order[0]
                next_player = turn_order[1]
                clear_screen()

                start = datetime.now()
                morpheme = random.choice(morphemes)
                print(f'Player {current_player}, within {timer} seconds, type a word containing {morpheme.upper()}.')
                ans = input('> ')



                check()



                while not valid:
                    if timecheck():
                        break
                    


                    if not repetition_allowed:
                        if ans.lower() in players[current_player]['used']:
                            time_left = round(timer - ((datetime.now() - start).total_seconds()), 1)
                            print(f'You\'ve already used this word. You have {time_left} seconds left.')
                            print(f'Type another word containing {morpheme.upper()}')
                            ans = input('> ')

                            check()



                    clear_screen()
                    if ans == '/quit':
                        sys.exit()

                    elif ans == '/skip':
                        timer -= 0.4
                        break

                    else:
                        time_left = round(timer - ((datetime.now() - start).total_seconds()), 1)

                        if time_left <= 0:
                            break
                        
                        print(f'Invalid word. You have {time_left} seconds left.')
                        print(f'Type a word containing {morpheme.upper()}')
                        ans = input('> ')

                        check()



                if timecheck():
                    clear_screen()
                    players[current_player]['lives'] -= 1



                    if players[current_player]['lives'] > 0:
                        turn_order.append(turn_order.pop(0))

                        print(f'Too late. Player {current_player}, you\'ve lost a life.')
                        print(f'You now have {players[current_player]['lives']} lives remaining.')
                        print(f'Press enter to resume. It will be Player {next_player}\'s turn, starting with {timer_start} seconds.')
                        input('> ')

                        timer = timer_start
                        continue



                    else:
                        print(f'Too late. Player {current_player}, you\'ve run out of lives!')

                        turn_order.pop(0)

                        sleep(1)

                        if len(turn_order) == 1:
                            break

                        else:
                            print(f'Press enter to resume. It will be Player {next_player}\'s turn, starting with {timer_start} seconds.')
                            input('> ')

                            timer = timer_start
                            continue
                    


                if not repetition_allowed:
                    if ans != '/skip':
                        players[current_player]['used'].add(ans)



                turn_order.append(turn_order.pop(0))
                answers += 1



                clear_screen()
                print(f'''PLAYER {next_player}\'S TURN IS NEXT! GET READY!''')
                


                sleep(2)



                timer = round((timer - ((datetime.now() - start).total_seconds())) + 7, 1)










# --------------------------------- GAME (MULTIPLAYER -- TIME ATTACK) ---------------------------------



        elif gamemode == gamemodes[1]:
            game_start = datetime.now()
            turn_order = list(players.keys())



            while True:
                current_player = turn_order[0]
                next_player = turn_order[1]
                timer_start = players[current_player]['time']
                clear_screen()

                start = datetime.now()
                morpheme = random.choice(morphemes)
                print(f'Player {current_player}, within {players[current_player]['time']} seconds, type a word containing {morpheme.upper()}.')
                ans = input('> ')



                check()



                while not valid:
                    if timecheck(True):
                        break
                    


                    if not repetition_allowed:
                        if ans.lower() in players[current_player]['used']:
                            time_left = round(players[current_player]['time'] - ((datetime.now() - start).total_seconds()), 1)
                            print(f'You\'ve already used this word. You have {time_left} seconds left.')
                            print(f'Type another word containing {morpheme.upper()}')
                            ans = input('> ')

                            check()



                    clear_screen()
                    if ans == '/quit':
                        sys.exit()

                    elif ans == '/skip':
                        players[current_player]['time'] -= 0.4
                        break

                    else:
                        time_left = round(players[current_player]['time'] - ((datetime.now() - start).total_seconds()), 1)

                        if time_left <= 0:
                            break
                        
                        print(f'Invalid word. You have {time_left} seconds left.')
                        print(f'Type a word containing {morpheme.upper()}')
                        ans = input('> ')

                        check()



                if timecheck(True):
                    clear_screen()
                    players[current_player]['lives'] -= 1


                
                    print(f'Too late. Player {current_player}, you\'ve run out of lives!')

                    turn_order.pop(0)

                    sleep(1)

                    if len(turn_order) == 1:
                        break

                    else:
                        print(f'Press enter to resume. It will be Player {next_player}\'s turn, starting with {timer_start} seconds.')
                        input('> ')

                        players[current_player]['time'] = timer_start
                        continue
                    


                if not repetition_allowed:
                    if ans != '/skip':
                        players[current_player]['used'].add(ans)



                turn_order.append(turn_order.pop(0))
                answers += 1



                clear_screen()
                print(f'''PLAYER {next_player}\'S TURN IS NEXT! GET READY!''')
                


                sleep(2)



                players[current_player]['time'] = round((players[current_player]['time'] - ((datetime.now() - start).total_seconds())) + 2, 1)










# --------------------------------- GAME (MULTIPLAYER -- CO-OP) ---------------------------------



        elif gamemode == gamemodes[2]:
            game_start = datetime.now()
            turn_order = list(players.keys())



            while True:
                current_player = turn_order[0]
                next_player = turn_order[1]
                clear_screen()

                start = datetime.now()
                morpheme = random.choice(morphemes)
                print(f'Player {current_player}, within {timer} seconds, type a word containing {morpheme.upper()}.')
                ans = input('> ')



                check()



                while not valid:
                    if timecheck():
                        break
                    


                    if not repetition_allowed:
                        if ans.lower() in used:
                            time_left = round(timer - ((datetime.now() - start).total_seconds()), 1)
                            print(f'You\'ve already used this word. You have {time_left} seconds left.')
                            print(f'Type another word containing {morpheme.upper()}')
                            ans = input('> ')

                            check()



                    clear_screen()
                    if ans == '/quit':
                        sys.exit()

                    elif ans == '/skip':
                        timer -= 0.4
                        break

                    else:
                        time_left = round(timer - ((datetime.now() - start).total_seconds()), 1)

                        if time_left <= 0:
                            break
                        
                        print(f'Invalid word. You have {time_left} seconds left.')
                        print(f'Type a word containing {morpheme.upper()}')
                        ans = input('> ')

                        check()



                if timecheck():
                    clear_screen()
                    lives -= 1



                    if lives > 0:
                        turn_order.append(turn_order.pop(0))

                        print(f'Too late. You\'ve lost a life.')
                        print(f'You now have {lives} lives remaining.')
                        print(f'Press enter to resume. It will be Player {next_player}\'s turn, starting with {timer_start} seconds.')
                        input('> ')

                        timer = timer_start
                        continue



                    else:
                        print(f'Too late. You\'ve run out of lives!')

                        turn_order.pop(0)

                        sleep(1)

                        break
                    


                if not repetition_allowed:
                    if ans != '/skip':
                        used.add(ans)



                turn_order.append(turn_order.pop(0))
                answers += 1



                clear_screen()
                print(f'''PLAYER {next_player}\'S TURN IS NEXT! GET READY!''')
                


                sleep(2)



                timer = round((timer - ((datetime.now() - start).total_seconds())) + 7, 1)










# --------------------------------- GAME OVER (MULTIPLAYER) ---------------------------------



            clear_screen()



            if gamemode != gamemodes[2]:
                print(f'================== CONGRATULATIONS, PLAYER {next_player}! ==================')
                print(f'Winner: Player {next_player}!')

                print()
                print('Nice try, everyone else!')
            
            else:
                print(f'================== NICE TRY, PLAYERS! ==================')
                print(f'Player {current_player} lost the last life!')

                print()
                print('Nice try, everyone!')

            sleep(3)

            print()
            print('Click enter to see the game stats.')
            input('> ')
            


            clear_screen()
            print('================================= GAME STATS =================================')
            print(f'# of Words Used (All Players): {answers}')
            print(f'Game Length (Minutes:Seconds): {strftime('%M:%S', gmtime((datetime.now() - game_start).total_seconds()))}')
            


            break