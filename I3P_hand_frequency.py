import random

#
#   Infinite 3 Card Poker Hand Frequency Checker
#

#
#   Helper functions
#

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

#WIP: Add ability to change number of ranks, rather than default 13
# global variable for max rank?
def is_any_straight(r1, r2, r3):
    if (r1==r2 or r2==r3 or r3==r1):
        return False

    arr = [r1, r2, r3]
    arr.sort()
    #Top straights
    if arr[0]-arr[1]==-1 and arr[1]-arr[2]==-1:
        return True
    #Bottom straight
    elif arr[0]-arr[1]==-1 and arr[1]-arr[2]==-11:
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
    #Error checking
    check_counter = 0;

    #Count set up
    hand_counter = 0
    output = ""

    highcard_counter = 0
    pair_counter = 0
    trips_counter = 0
    straight_counter = 0
    flush_counter = 0
    flush_pair_counter = 0
    flush_trips_counter = 0
    straight_flush_counter = 0

    #Calculation (to be looped)

    #Number of suits (default 4) and ranks (default 13)
    num_suits = 4
    num_ranks = 13
    last_card_index = (num_ranks * num_suits) - 1

    loops = 1000000
    for i in range(loops):
        # Generate Cards
        c1 = random.randint(0, last_card_index)
        c2 = random.randint(0, last_card_index)
        c3 = random.randint(0, last_card_index)
        # Rank
        r1 = c1 % num_ranks
        r2 = c2 % num_ranks
        r3 = c3 % num_ranks
        # Suit
        s1 = c1 % num_suits
        s2 = c2 % num_suits
        s3 = c3 % num_suits
        # output = parse_card(r1, s1) + ", " + parse_card(r2, s2) + ", " + parse_card(r3, s3)

        hand_counter += 1

        if is_highcard(r1, r2, r3, s1, s2, s3):
            check_counter += 1
            highcard_counter += 1
            # print("High Card")
        if is_pair(r1, r2, r3, s1, s2, s3):
            check_counter += 1
            pair_counter += 1
            # print("Pair")
        if is_flush(r1, r2, r3, s1, s2, s3):
            check_counter += 1
            flush_counter += 1
            # print("Flush")
        if is_straight(r1, r2, r3, s1, s2, s3):
            check_counter += 1
            straight_counter += 1
            # print("Straight")
        if is_flush_pair(r1, r2, r3, s1, s2, s3):
            check_counter += 1
            flush_pair_counter += 1
            # print("Flush Pair")
        if is_trips(r1, r2, r3, s1, s2, s3):
            check_counter += 1
            trips_counter += 1
            # print("Trips")
        if is_straight_flush(r1, r2, r3, s1, s2, s3):
            check_counter += 1
            straight_flush_counter += 1
            # print("Straight Flush")
        if is_flush_trips(r1, r2, r3, s1, s2, s3):
            check_counter += 1
            flush_trips_counter += 1
            # print("Flush Trips")
        # print(output)

        progress = i % (loops / 100)
        percent = 0;
        if progress == ((loops / 100) - 1):
            percent = 100 * ((i + 1) / loops)
            print(percent, "%")
    # End of loop

    # Print Results

    print()
    print("High card % =")
    highcard_percent = highcard_counter/hand_counter
    print(100 * highcard_percent)
    print()

    print("Pair % =")
    pair_percent = pair_counter/hand_counter
    print(100 * pair_percent)
    print()

    print("Flush % =")
    flush_percent = flush_counter / hand_counter
    print(100 * flush_percent)
    print()

    print("Straight % =")
    straight_percent = straight_counter/hand_counter
    print(100 * straight_percent)
    print()

    print("Flush Pair % =")
    flush_pair_percent = flush_pair_counter/hand_counter
    print(100 * flush_pair_percent)
    print()

    print("Trips % =")
    trips_percent = trips_counter/hand_counter
    print(100 * trips_percent)
    print()

    print("Straight Flush % =")
    straight_flush_percent = straight_flush_counter / hand_counter
    print(100 * straight_flush_percent)
    print()

    print("Flush Trips % =")
    flush_trips_percent = flush_trips_counter/hand_counter
    print(100* flush_trips_percent)
    print()

    print("Odds Testing:")
    stack = 100
    pair_pay = 2
    flush_pay = 4
    straight_pay = 5
    flush_pair_pay = 7
    trips_pay = 13
    straight_flush_pay = 17
    flush_trips_pay = 37
    ev = stack * ((pair_pay * pair_percent) + (flush_pay * flush_percent) + (straight_pay * straight_percent) + (flush_pair_pay * flush_pair_percent) + (trips_pay * trips_percent) + (straight_flush_pay * straight_flush_percent) + (flush_trips_pay * flush_trips_percent))
    print('EV(100):', ev)

    print("V1 Odds:")
    stack = 100
    pair_pay = 2
    flush_pay = 4
    straight_pay = 5
    flush_pair_pay = 7
    trips_pay = 10
    straight_flush_pay = 19
    flush_trips_pay = 49
    ev = stack * ((pair_pay * pair_percent) + (flush_pay * flush_percent) + (straight_pay * straight_percent) + (
                flush_pair_pay * flush_pair_percent) + (trips_pay * trips_percent) + (
                              straight_flush_pay * straight_flush_percent) + (flush_trips_pay * flush_trips_percent))
    print('EV(100):', ev)

    #print("Error check:")
    #check = hand_counter - check_counter
    #print(check)

