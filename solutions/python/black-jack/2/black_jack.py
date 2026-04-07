"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    face_cards = 'JQK'
    number_cards = [f'{number}' for number in range(2, 11)]


    if card in face_cards:
        return 10
    if card in number_cards:
        return int(card)
    return 1


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    score_a = value_of_card(card_one)
    score_b = value_of_card(card_two)

    if score_a > score_b:
        return card_one
    if score_b > score_a:
        return card_two
    return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    score_a = 0
    if card_one == 'A':
        score_a = 11
    else:
        score_a = value_of_card(card_one)

    score_b = 0
    if card_two == 'A':
        score_b = 11
    else:
        score_b = value_of_card(card_two)

    score_hand = score_a + score_b

    if score_hand <= 10:
        return 11
    return 1

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    ten_cards = ['10', 'J', 'Q', 'K']

    if card_one == 'A' and card_two in ten_cards:
        return True

    if card_two == 'A' and card_one in ten_cards:
        return True

    return False



def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    score_a = value_of_card(card_one)
    score_b = value_of_card(card_two)

    if score_a == score_b:
        return True
    return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    score_a = value_of_card(card_one)
    score_b = value_of_card(card_two)

    total_score = score_a + score_b

    if total_score in [9, 10, 11]:
        return True
    return False
