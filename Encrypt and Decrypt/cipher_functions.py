ENCRYPT = 'e'
DECRYPT = 'd'

def clean_message (given_message):
    """(str) -> str
    
    When given_message is obtained modify it so that there are only 
    alphabetical characters in the message, and return that message with all
    letter capitalized
    
    >>> clean_message ("Hi, what is your name?")
    'HIWHATISYOURNAME'
    >>> clean_message ("198259852735")
    ''
    """
    
    modified_message = ""
    for char in given_message:
        if (char.isalpha()):
            modified_message = modified_message + char
    return (modified_message.upper())

def encrypt_letter (upper_letter, keystream_value):
    """(str, int) -> str
    
    Add the keystream_value to the "ord" value of the given upper_letter
    in order to obtain a return a second letter. If the "ord" value goes above 
    25, subtract the value by 26 and return the new letter
    
    >>> encrypt_letter ('A', 3)
    'D'
    >>> encrypt_letter ('X', 12)
    'J'
    """
    
    ord_diff = ord(upper_letter) - ord('A')
    new_char_ord = (ord_diff + keystream_value) % 26
    return chr(new_char_ord + ord('A'))

def decrypt_letter (upper_letter, keystream_value):
    """(str, int) -> str
    
    Subtract the keystream_value from the "ord" value of the given upper_letter
    in order to generate and return a second letter. If the "ord" value goes 
    below 0, add 26 to the value and return the new letter
    
    >>> decrypt_letter ('E', 15)
    'P'
    >>> decrypt_letter ('C', 1)
    'B'
    """
    
    ord_diff = ord(upper_letter) - ord('A')
    new_char_ord = (ord_diff - keystream_value) % 26
    return chr(new_char_ord + ord('A'))

def swap_cards (deck_of_cards, card_index):
    """(list of int, int) -> NoneType
    
    Precondition: The deck_of_cards are not empty (i.e. len(deck_of_cards) > 0)
                  and card_index >= 0 and card_index < len(deck_of_cards)
    
    When given a deck_of_cards and a particular card_index swap the value of
    the card at the given index with the value of the card at the
    next subsequent index. The deck is treated as circular, which means the 
    last card swaps with the first card
    
    >>> cards = [1,3,2,4]
    >>> swap_cards (cards, 1)
    >>> cards
    [1,2,3,4]
    >>> cards = [1,5,4,2,3]
    >>> swap_cards (cards, 4)
    >>> cards
    [3,5,4,2,1]
    """
    
    length = len(deck_of_cards)
    temp_value = 0
    if (card_index == length - 1):
        temp_value = deck_of_cards[0]
        deck_of_cards[0] = deck_of_cards[-1]
        deck_of_cards[-1] = temp_value
    else:
        temp_value = deck_of_cards[card_index]
        deck_of_cards[card_index] = deck_of_cards [(card_index) + 1]
        deck_of_cards[(card_index + 1)] = temp_value
    
def get_small_joker_value (deck_of_cards):
    """(list of int) -> int
    
    Precondition: len(deck_of_cards) > 2, and no two card values are 
    the same.
    
    When given a deck_of_cards determine and return the value of the second
    highest card
    
    >>>get_small_joker_value ([1,4,2,3,8,6,7])
    7
    >>>get_small_joker_value ([1,7,3,4,5,2,6])
    6
    """
    
    copy_of_deck = []
    for card in deck_of_cards:
        copy_of_deck.append (card)
    copy_of_deck.remove (max(copy_of_deck))
    return (max(copy_of_deck))

def get_big_joker_value (deck_of_cards):
    """(list of int) -> int
    
    Precondition: len(deck_of_cards) > 2, and no two card values are 
    the same.
    
    When given a deck_of_cards determine and return the value of the highest 
    card.
    
    >>>get_big_joker_value ([1,3,2,4,5])
    5
    >>>get_big_joker_value ([2,1])
    2
    """
    
    return (max(deck_of_cards))

def move_small_joker (deck_of_cards):
    """ (list of int) -> NoneType
    
    Precondition: len(deck_of_cards) > 2, and no two card values are 
    the same.
    
    Swap the card that is represented by the small joker with the sebsequent
    card to it.
    
    >>> deck = [6,3,4,5,1,2]
    >>> move_small_joker (deck)
    >>> deck
    [6,3,4,1,5,2]
    >>> deck = [1,3,2,4,7,6,5,10,8,9]
    >>> move_small_joker (deck)
    >>> deck
    [9,3,2,4,7,6,5,10,8,1]
    """
    
    joker_index = deck_of_cards.index (get_small_joker_value (deck_of_cards))
    swap_cards (deck_of_cards, joker_index)

def move_big_joker (deck_of_cards):
    """ (list of int) -> NoneType
    
    Precondition: len(deck_of_cards) > 2, and no two card values are 
    the same.
    
    Move the card that is represented by the big joker down two places in the
    deck.
    
    >>> deck = [1,3,2]
    >>> move_big_joker (deck)
    >>> deck
    [3,2,1]
    >>> deck = [4,1,3,2]
    >>> move_big_joker (deck)
    >>> deck
    [1,3,4,2]
    """
    
    joker_index = deck_of_cards.index (get_big_joker_value (deck_of_cards))
    swap_cards (deck_of_cards, joker_index)
    if (joker_index + 1 == len(deck_of_cards)):
        swap_cards (deck_of_cards, 0)
    else:
        swap_cards (deck_of_cards, (joker_index + 1))


def triple_cut (deck_of_cards): 
    """ (list of int) -> NoneType
    
    Precondition: len(deck_of_cards) > 2, and no two card values are 
    the same.
    
    Find the index of the two jokers in the deck_of_cards, and move the cards
    infront of the joker closest to the top of the deck bedhind the joker 
    furthest away from the top of the deck. Additionally move the cards behind
    the joker furthest away from the top of the deck infront of the joker
    closest to the top of the deck.
    
    >>> deck = [1,4,5,2,10,7,6,9,8,3]
    >>> triple_cut (deck)
    >>> deck
    [8,3,10,7,6,9,1,4,5,2]
    >>> deck = [2,1,3]
    >>> triple_cut (deck)
    >>> deck
    [2,1,3]
    """
    
    # Determining the joker that is closest and furthest away from the 
    # beginning of the list.
    joker_1 = deck_of_cards.index (get_big_joker_value (deck_of_cards))
    joker_2 = deck_of_cards.index (get_small_joker_value (deck_of_cards))
    if (joker_1 > joker_2):
        joker_1, joker_2 = joker_2, joker_1
    joker_1_values = []
    joker_2_values = []
    length = len (deck_of_cards)
    index_counter = 0
    for index in range (joker_1):
        joker_1_values.append (deck_of_cards.pop(0))
    length = length - (joker_2 + 1)
    # Changing the index where the second joker is located becuase the list was
    # modified above.
    joker_2 = joker_2 - len (joker_1_values)
    start_index = joker_2 + 1
    for index in range (start_index, start_index + length):
        joker_2_values.append (deck_of_cards.pop(start_index))
    deck_of_cards.extend (joker_1_values)
    for card in joker_2_values:
        deck_of_cards.insert (index_counter, card)
        index_counter = index_counter + 1

def insert_top_to_bottom (deck_of_cards):
    """ (list of in) -> NoneType
    
    Precondition: len(deck_of_cards) > 2, and no two card values are 
    the same.
    
    Take the value of the bottom card in the deck_of_cards (if that card is the
    big joker, use the value of the small joker) and move that many cards from
    the top of the deck to bottom. Just infront of the bottom card.
    
    >>> deck = [1,3,2,8,4,6,7,5]
    >>> insert_top_to_bottom (deck)
    >>> deck
    [6,7,1,3,2,8,4,5]
    >>> deck = [1,2,3]
    >>> insert_top_to_bottom (deck)
    >>> deck
    [1,2,3]
    """
    
    num_of_cards = deck_of_cards[-1]
    if (num_of_cards == get_big_joker_value (deck_of_cards)):
        num_of_cards = get_small_joker_value (deck_of_cards)
    cards_to_move = []
    for index in range (num_of_cards):
        cards_to_move.append (deck_of_cards.pop(0))
    for card in cards_to_move:
        deck_of_cards.insert (-1, card)

def get_card_at_top_index (deck_of_cards):
    """ (list of int) -> int
    
    Precondition: len(deck_of_cards) > 2, and no two card values are 
    the same.
    
    Use the top card in the deck_of_cards as an index to find and return the 
    card at that specific index. If the top card is the big joker, use the 
    small joker as the index.
    
    >>> get_card_at_top_index ([1,2,3,5,4,])
    1
    >>> get_card_at_top_index ([5,2,3,1,4,])
    4
    """
    
    top_card_value = deck_of_cards[0]
    if (top_card_value == get_big_joker_value (deck_of_cards)):
        top_card_value = get_small_joker_value (deck_of_cards)
    return (deck_of_cards[top_card_value])

def get_next_keystream_value (deck_of_cards):
    """ (list of int) -> int
    
    Precondition: len(deck_of_cards) > 2, and no two card values are 
    the same.
    
    Call of the steps in the encryption/decryption (move_small_joker,
    move_big_joker, triple_cut, insert_top_to_bottom, get_next_keystream_value)
    to determine a specific keystream value given a deck_of_cards. Keep 
    repeating the algorithm until the value to return is not between 1 and 
    the big joker value - 2)
    
    >>> get_next_keystream_value ([1,5,4,2,3])
    2
    >>> get_next_keystream_value ([1,7,3,6,5,4,2])
    1
    """
    
    move_small_joker (deck_of_cards)
    move_big_joker (deck_of_cards)
    triple_cut (deck_of_cards)
    insert_top_to_bottom (deck_of_cards)
    keystream_value = get_card_at_top_index (deck_of_cards)
    big_joker = get_big_joker_value (deck_of_cards)
    small_joker = get_small_joker_value (deck_of_cards)
    while ((keystream_value == big_joker) or (keystream_value == small_joker)):
        move_small_joker (deck_of_cards)
        move_big_joker (deck_of_cards)
        triple_cut (deck_of_cards)
        insert_top_to_bottom (deck_of_cards)
        keystream_value = get_card_at_top_index (deck_of_cards)        
    return (keystream_value)

def process_messages (deck_of_cards, messages, task):
    """ (list of int, list of str, str) -> list of str
    
    Precondition: len(deck_of_cards) > 2, and no two card values are 
    the same.
    
    Return the messages the were given but altered based on the given 
    deck_of_cards and what the task of the user is (encrypt or decrypt).
    
    >>> process_messages ([1,4,5,2,3], ["Hi", "What  your name"], "e")
    ['IK', 'YJDWAPXUQBPH']
    >>> process_messages ([1,4,5,2,3], ['IK', 'YJDWAPXUQBPH'], "d")
    ["Hi", "What  your name"]
    """
    
    transformed_messages = []
    keystream_value = 0
    new_message = ""
    new_character = ""
    for message in messages:
        if (task == ENCRYPT):
            message = clean_message (message)
        new_message = ""
        for char in message:
            keystream_value = get_next_keystream_value (deck_of_cards)
            if (task == ENCRYPT):
                new_character = encrypt_letter (char, keystream_value)
            else:
                new_character = decrypt_letter (char, keystream_value)
            new_message = new_message + new_character
        transformed_messages.append (new_message)
    return (transformed_messages)

def read_messages (file_of_messages):
    """ (file open for reading) -> list of str
    
    Read the contents of the file_of_messages and separate them line by line, 
    while removing the newline character ('\n') whenever it occurs.
    """
    line = file_of_messages.readline()
    collection_of_messages = []
    while (line != ""):
        collection_of_messages.append(line.strip())
        line = file_of_messages.readline()
    return (collection_of_messages)

def is_valid_deck (deck_of_cards):
    """ (list of int) -> bool
    
    Precondition: len(deck_of_cards) > 2, and no two card values are 
    the same.
    
    Return whether or not the given deck_of_cards is valid or not. Validity is 
    determined by the cards in the deck having the value  between 1 and the 
    length of the deck. The value of two cards cannot by the same, and they can
    be in any particular order.
    
    >>> is_valid_deck ([1,3,22,6])
    False
    >>> is_valid_deck ([1,5,4,2,3])
    True
    """
    
    num_of_cards = len (deck_of_cards)
    required_cards = []
    copy_of_deck = []
    for i in range (num_of_cards):
        required_cards.append (i + 1)
    for card in deck_of_cards:
        copy_of_deck.append(card)
    copy_of_deck.sort()
    if (len (copy_of_deck) != len (required_cards)):
        return (False)
    else:
        for i in range (len(copy_of_deck)):
            if (copy_of_deck[i] != required_cards[i]):
                return (False)
        return (True)

def read_deck (deck_file):
    """ (file open for reading) -> list of int
    
    Read the contents of the deck_file and store the values of the cards that 
    are desired
    """
    
    cards = deck_file.read()
    deck_of_cards = []
    cards = cards.strip()
    card_value = ""
    newline_index = cards.find('\n')
    while (newline_index != -1):
        cards = cards.replace('\n', " ")
        newline_index = cards.find('\n')
    for i in range (len(cards)):
        if (cards[i] != ' '):
            card_value = card_value + cards[i]
        else:
            if (card_value.isnumeric()):
                deck_of_cards.append (int(card_value))
            card_value = ""
    if ((card_value != "") and (card_value.isnumeric())):
        deck_of_cards.append (int(card_value))    
    return (deck_of_cards)
