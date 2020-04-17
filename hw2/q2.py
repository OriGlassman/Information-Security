from q2_atm import ATM, ServerResponse
import itertools
from Crypto.PublicKey import RSA
import six
import math



def extract_PIN(encrypted_PIN):
	atm = ATM()
	all_pin_combinations = itertools.product([i for i in range(10)], repeat=4)
	for i in range(10**4):
		temp_combination_arr = all_pin_combinations.next()
		temp_combination_str = "".join(str(digit) for digit in temp_combination_arr)
		temp_combination_int = int(temp_combination_str)
		if atm.rsa_pin.encrypt(temp_combination_int,None)[0] == encrypted_PIN:
			return int(temp_combination_int)


def extract_credit_card(encrypted_credit_card):
	return int(round(int(encrypted_credit_card)**(1./3)))



def forge_signature():
    return ServerResponse(1,1)