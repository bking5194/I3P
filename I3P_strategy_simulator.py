import random

#
#   Infinite 3 Card Poker Strategy Simulator
#

#
#   Helper functions
#

def get_hand_data(cards):
    # Find high card
    highcard = -1
    r1 = cards[0] % 13
    r2 = cards[1] % 13
    r3 = cards[2] % 13
    arr = [r1, r2, r3]
    arr.sort()
    if arr[0] != arr[1]:
        highcard = arr[2]
    else: # Pair Protection
        highcard = arr[0]

    # Find Hand Type
    type = -1
    s1 = cards[0] % 4
    s2 = cards[1] % 4
    s3 = cards[2] % 4
    if is_highcard(r1, r2, r3, s1, s2, s3):
        type = 0
    if is_pair(r1, r2, r3, s1, s2, s3):
        type = 1
    if is_flush(r1, r2, r3, s1, s2, s3):
        type = 2
    if is_straight(r1, r2, r3, s1, s2, s3):
        type = 3
    if is_flush_pair(r1, r2, r3, s1, s2, s3):
        type = 4
    if is_trips(r1, r2, r3, s1, s2, s3):
        type = 5
    if is_straight_flush(r1, r2, r3, s1, s2, s3):
        type = 6
    if is_flush_trips(r1, r2, r3, s1, s2, s3):
        type = 7

    # Return data
    hand_data = [type, highcard]
    return hand_data

def parse_card(r, s):
    card = ""

    #Rank
    if r == 0:
        card = "2 of "
    elif r == 1:
        card = "3 of "
    elif r == 2:
        card = "4 of "
    elif r == 3:
        card = "5 of "
    elif r == 4:
        card = "6 of "
    elif r == 5:
        card = "7 of "
    elif r == 6:
        card = "8 of "
    elif r == 7:
        card = "9 of "
    elif r == 8:
        card = "10 of "
    elif r == 9:
        card = "Jack of "
    elif r == 10:
        card = "Queen of "
    elif r == 11:
        card = "King of "
    elif r == 12:
        card = "Ace of "

    #Suit
    if s == 0:
        card += "Spades"
    elif s == 1:
        card += "Hearts"
    elif s == 2:
        card += "Clubs"
    elif s == 3:
        card += "Diamonds"

    return card

def is_any_pair(r1, r2, r3):
    if r1==r2 and r2==r3:
        return False
    elif r1==r2 or r2==r3 or r3==r1:
        return True
    else:
        return False

def is_any_trips(r1, r2, r3):
    if r1==r2 and r2==r3:
        return True
    else:
        return False

def is_any_flush(s1, s2, s3):
    if s1==s2 and s2==s3:
        return True
    else:
        return False

def is_any_straight(r1, r2, r3):
    # Save compute
    if (r1==r2 or r2==r3 or r3==r1):
        return False

    # Sort
    arr = [r1, r2, r3]
    arr.sort()
    #Top straights
    if arr[0]-arr[1]==-1 and arr[1]-arr[2]==-1: # 2,3,4 -> Q,K,A
        return True
    #Bottom straight
    elif arr[0]-arr[1]==-1 and arr[1]-arr[2]==-11: # A,2,3
        return True
    else:
        return False

#
#   Hand Check Functions
#

def is_highcard(r1, r2, r3, s1, s2, s3):
    if (r1 != r2 and r2 != r3 and r3 != r1) and not is_any_flush(s1, s2, s3) and not is_any_straight(r1, r2, r3):
        return True
    else:
        return False

def is_pair(r1, r2, r3, s1, s2, s3):
    if is_any_pair(r1, r2, r3) and not is_any_flush(s1, s2, s3):
        return True
    else:
        return False

def is_trips(r1, r2, r3, s1, s2, s3):
    if is_any_trips(r1, r2, r3) and not is_any_flush(s1, s2, s3):
        return True
    else:
        return False

def is_straight(r1, r2, r3, s1, s2, s3):
    if is_any_straight(r1, r2, r3) and not is_any_flush(s1, s2, s3):
        return True
    else:
        return False

def is_flush(r1, r2, r3, s1, s2, s3):
    if is_any_flush(s1, s2, s3) and not is_any_pair(r1, r2, r3) and not is_any_trips(r1, r2, r3) and not is_any_straight(r1, r2, r3):
        return True
    else:
        return False

def is_flush_pair(r1, r2, r3, s1, s2, s3):
    if is_any_flush(s1, s2, s3) and is_any_pair(r1, r2, r3):
        return True
    else:
        return False

def is_flush_trips(r1, r2, r3, s1, s2, s3):
    if is_any_flush(s1, s2, s3) and is_any_trips(r1, r2, r3):
        return True
    else:
        return False

def is_straight_flush(r1, r2, r3, s1, s2, s3):
    if is_any_flush(s1, s2, s3) and is_any_straight(r1, r2, r3):
        return True
    else:
        return False


if __name__ == '__main__':

    #
    # Variables for testing here
    #

    games = 10000 # total games to simulate
    loops = 250 # total loops per game. 2-250
    token_size = 4

    # User betting conditions
    ante = 1 * token_size # limit = 16, min = 1
    pair_plus = 3 * token_size # limit = 16, min = 0
    starting_stack = 640 # Max ~2300 (64 stack * 36 slots of __________) ?????
    play_pair_plus = pair_plus > 0 # Play Pair Plus?
    # [0, 0] - [0, 2] play every hand? THEN WHY DO THE ODDS CHANGE?????
    user_to_qualify = [0, 11] # Hand type (0-7) & Highest active card (0-12)
    dynamic_quit_conditions = True # still problems here

    # Success conditions
    quit_success = 2 * starting_stack  # 864  Max score before quitting
    success_threshold = 1.65 * starting_stack
    success_top = 2 * starting_stack
    success_bottom = starting_stack + 32

    # Failure Conditions
    quit_failure = starting_stack / 2 # Min score before quitting
    failure_threshold =  (starting_stack / 2) + 128
    failure_top = starting_stack
    failure_bottom = quit_failure

    house_starting_stack = 5100 # House bankroll? min 5100, ideal 13284
    house_stack = house_starting_stack
    house_to_qualify = 11 # Default 11 = King, update to array like user_to_qualify
    pair_reward = 2 # final ratio 1:1
    flush_reward = 4 # final ratio 1:3
    straight_reward = 5 # v1 ratio 1:4
    flush_pair_reward = 7 # v1 ratio 1:6
    trips_reward = 13 # v1 ratio 1:9
    straight_flush_reward = 17 # v1 ratio 1:18
    flush_trips_reward = 37 # v1 ratio 1:48

    #
    # End of testing variables
    #

    # Counter Variables
    user_win_count = 0 #
    session_win_count = 0 #
    session_busted_count = 0 #
    total_hand_count = 0 #
    total_stack_max = 0 #
    total_stack_min = 0 #
    total_stack_final = 0 #
    total_hands_qualified = 0 #
    total_positive_sessions = 0 #

    # Results Variables
    avg_stack_max = 0
    avg_stack_min = 0
    avg_stack_final = 0
    avg_hands_until_quitting = 0
    hand_win_percent = 0
    busted_percent = 0

    # Set up
    user_cards = []
    house_cards = []
    max_winnings = 0

    #
    # Main Loop
    #

    game_counter = 0
    while game_counter < games: # Play Games
        game_counter += 1
        quit_success = 2 * starting_stack
        quit_failure = starting_stack / 2
        # Session Variables
        session_win = False
        session_busted = False
        hand_counter = 0
        stack = starting_stack
        stack_max = starting_stack
        stack_min = starting_stack
        # Start Inner Loop (Play Hands)
        while hand_counter < loops:
            # Deal & Ante
            user_cards = [random.randint(0, 51), random.randint(0, 51), random.randint(0, 51)]
            house_cards = [random.randint(0, 51), random.randint(0, 51), random.randint(0, 51)]
            stack += -(ante) # Play Ante
            house_stack += ante
            if (play_pair_plus):
                stack += -(pair_plus) # Play Pair Plus
                house_stack += pair_plus
            hand_counter += 1 # Increment Hand count

            # Qualification
            user_hand = get_hand_data(user_cards)
            house_hand = []
            if (user_hand[0] > user_to_qualify[0]) or (user_hand[0] == user_to_qualify[0] and user_hand[1] >= user_to_qualify[1]):
                # User Qualified Pay Play
                total_hands_qualified += 1
                stack += -(ante)
                house_stack += ante

                # House Hand Qualification
                house_qualifies = True
                house_hand = get_hand_data(house_cards)
                if house_hand[0] == 0 and house_hand[1] < house_to_qualify:
                    # House does not qualify
                    house_qualifies = False

                # Hand Comparison
                # Bottom Straight??????????????????? A23 = AKQ & A23 > KQJ
                user_wins = True
                if (house_hand[0] > user_hand[0]) or (house_hand[0] == user_hand[0] and house_hand[1] > user_hand[1]):
                    user_wins = False

                # Ante and Play payout
                # WHAT ARE WE DOING HERE?????? FIRST TWO CONDITIONS ARE STUPID
                if not house_qualifies and not play_pair_plus:
                    #stack += (2 * ante) v1 payout
                    #house_stack += -(2 * ante) v1 payout
                    stack += (3 * ante - (ante / 4))  # Pay Ante 1:1 and return Play 4:3 (ante - 1)
                    house_stack += -(3 * ante - (ante / 4))
                elif not house_qualifies and play_pair_plus:
                    #stack += (3 * ante) v1 payout
                    #house_stack += -(3 * ante) v1 payout
                    stack += (3 * ante)  # Pay Ante 1:1 and return Play
                    house_stack += -(3 * ante)
                elif house_qualifies and user_wins:
                    stack += (4 * ante + (ante / 4))  # Pay Ante 1:1 and Play 4:5 (ante + 1)
                    house_stack += -(4 * ante + (ante / 4))
                    user_win_count += 1

                # Pair Plus payout
                user_hand_rank = user_hand[0]
                if user_hand_rank == 1 and play_pair_plus:  # Pair
                    stack += (pair_reward * pair_plus)
                    house_stack += -(pair_reward * pair_plus)
                elif user_hand_rank == 2 and play_pair_plus:  # Flush
                    stack += (flush_reward * pair_plus)
                    house_stack += -(flush_reward * pair_plus)
                elif user_hand_rank == 3 and play_pair_plus:  # Straight
                    stack += (straight_reward * pair_plus)
                    house_stack += -(straight_reward * pair_plus)
                elif user_hand_rank == 4 and play_pair_plus:  # Flush Pair
                    stack += (flush_pair_reward * pair_plus)
                    house_stack += -(flush_pair_reward * pair_plus)
                elif user_hand_rank == 5 and play_pair_plus:  # Trips
                    stack += (trips_reward * pair_plus)
                    house_stack += -(trips_reward * pair_plus)
                elif user_hand_rank == 6 and play_pair_plus:  # Straight FLush
                    stack += (straight_flush_reward * pair_plus)
                    house_stack += -(straight_flush_reward * pair_plus)
                elif user_hand_rank == 7 and play_pair_plus:  # Flush Trips
                    stack += (flush_trips_reward * pair_plus)
                    house_stack += -(flush_trips_reward * pair_plus)
            #
            # Record Hand Data
            #

            #print(stack)
            if (stack > stack_max): stack_max = stack
            if (stack < stack_min): stack_min = stack

            #
            # End Record Hand Data
            #

            # Break loop conditions (we can add more?)
            if stack >= quit_success:  # Success
                session_win = True
                break
            elif stack <= quit_failure:  # Failure
                session_busted = True
                break
            elif dynamic_quit_conditions and stack >= success_threshold: # change conditions based on performace
                quit_success = success_top
                quit_failure = success_bottom
            elif dynamic_quit_conditions and stack <= failure_threshold:
                quit_success = failure_top
                quit_failure = failure_bottom
        # End Inner Loop

        #
        # Record Session Data
        #

        total_stack_max += stack_max # Stack records
        total_stack_min += stack_min
        total_stack_final += stack
        if stack >= stack_max:
            total_positive_sessions += 1;
        if session_win: # Increment for a won game
            session_win_count += 1
        elif session_busted:
            session_busted_count += 1
        total_hand_count += hand_counter # Add number of played hands to total
        if max_winnings < stack:
            max_winnings = stack
        # hand win counter directly incremented in loop

        #
        # End Session Game Data
        #

        # Loading indicator
        progress = game_counter % (games / 100)
        percent = 0
        if progress == ((games / 100) - 1):
            percent = 100 * ((game_counter + 1) / games)
            print(percent, "%")


    #
    # End Main Loop
    #

    # Results:
    avg_stack_max = total_stack_max / games
    avg_stack_min = total_stack_min / games
    avg_stack_final = total_stack_final / games
    avg_hands_until_quitting = total_hand_count / games # probably a mean is better than an avg
    hand_win_percent = 100 * user_win_count / total_hand_count
    success_percent = 100 * session_win_count / games
    busted_percent = 100 * session_busted_count / games
    positive_session_percent = 100 * total_positive_sessions / games
    house_profits = house_stack - house_starting_stack
    house_bankrupt = house_stack <= 0

    # Print Results
    print()
    print("I3P Simulation")
    print("-----------------------------------------------")
    print("Total Hands Simulated:", total_hand_count)
    print("Total Hands Won:", user_win_count)
    print("Total Hands Qualified:", total_hands_qualified)
    print("Total Pair Plus Won:")
    print("Game Length:", loops)
    print("Average Hands Until Quitting:", avg_hands_until_quitting)
    print("-----------------------------------------------")
    print("Total Sessions Simulated:", games)
    print("Total Successful Sessions:", session_win_count)
    print("Total Neutral Sessions:")
    print("Total Times Busted:", session_busted_count)
    print("-----------------------------------------------")
    print("Average Stack Max:", avg_stack_max)
    print("Average Stack Min:", avg_stack_min)
    print("Average Stack Final:", avg_stack_final)
    print("Starting Stack:", starting_stack)
    print("-----------------------------------------------")
    print("Qualified Hands Won Percent:")
    print("Hand Wins Percent:", hand_win_percent, "%")
    print("Pair Plus Wins Percent:")
    print("-----------------------------------------------")
    print("Session Success Condition Met:", success_percent, "%")
    print("Session Busted Condition Met:", busted_percent, "%")
    print("Session Positive Percent:", positive_session_percent, "%")
    print("-----------------------------------------------")
    print("House Profits:", house_profits)
    print("House Gains per Game:", (house_profits / games))
    print("House Gains per Hand:", (house_profits / total_hand_count))
    print("House Bankrupt:", house_bankrupt)
    print("Biggest Winner:", max_winnings)
