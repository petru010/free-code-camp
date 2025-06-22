def verify_card_number(card_number): # Function to verify a card number using the Luhn algorithm
    sum_of_odd_digits = 0
    reversed_card_number = card_number[::-1] # Reverse the card number
    odd_digits = reversed_card_number[::2] # Get odd indexed digits
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    sum_of_even_digits = 0
    even_digits = reversed_card_number[1::2] # Get even indexed digits
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = number // 10 + number % 10
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits   
    return total % 10 == 0

def main():
    card_number = '4165-4902-9254-9827' # Example card number
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()