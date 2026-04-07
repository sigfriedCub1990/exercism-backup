"""Validate a credit card number using Luhn's algorithm"""


def is_valid_sequence(nums_seq) -> bool:
    """Determine if input is a sequence of number

    :param nums_seq: string - given sequence.
    :return: boolean - whether sequence is valid or not.
    """
    for digit in nums_seq:
        if not digit.isdigit():
            return False
    return True


class Luhn:
    """Validate a credit card number using Luhn's algorithm"""

    def __init__(self, card_num):
        self._card_num = card_num

    def valid(self):
        """Determine if card_num is valid according to Luhn's formula

        :return: boolean - whether credit card is valid or not
        """
        if len(self._card_num.strip()) <= 1:
            return False

        numbers_seq = list("".join(self._card_num.split()))
        if not is_valid_sequence(numbers_seq):
            return False

        # starts from right to left
        numbers_seq.reverse()

        even_digits = [
            int(digit) for (idx, digit) in enumerate(numbers_seq) if idx % 2 == 0
        ]
        odd_digits = [
            int(digit) for (idx, digit) in enumerate(numbers_seq) if idx % 2 != 0
        ]

        doubled_digits = [
            digit * 2 if digit * 2 <= 9 else digit * 2 - 9 for digit in odd_digits
        ]

        doubled_digits.extend(even_digits)

        return sum(doubled_digits) % 10 == 0
