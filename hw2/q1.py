from __future__ import division
import itertools
import random


class RepeatedKeyCipher(object):

    def __init__(self, key=[0, 0, 0, 0, 0]):
        """Initializes the object with a list of integers between 0 and 255."""
        assert all(0 <= k <= 255 and isinstance(k, (int, long)) for k in key)
        self.key = key

    def encrypt(self, plaintext):
        k=0
        encrypted_plaintext=""
        key_length = len(self.key)
        for c in plaintext:
        	encrypted_ascii = ord(c) ^ self.key[k]
        	encrypted_char = chr(encrypted_ascii)
        	encrypted_plaintext += encrypted_char
        	k = (k+1)%key_length
        return encrypted_plaintext



    def decrypt(self, ciphertext):
        return self.encrypt(ciphertext)


class BreakerAssistant(object):

	
    def plaintext_score(self, plaintext):
        histogram = {" ":17.00, "e": 12.02, "t": 9.10, "a": 8.12, "o": 7.68, "i": 7.31, "n": 6.95, "s": 6.28, "r": 6.02 , "h": 5.92, "d": 4.32, "l": 3.98, "u": 2.88,
        "c": 2.71, "m": 2.61, "f": 2.30, "y": 2.11 , "w": 2.09, "g": 2.03, "p": 1.82, "b": 1.49, "v": 1.11, "k": 0.69, "x": 0.17, "q": 0.11, "j": 0.10, "z": 0.07}
        words = ["the", "and","ing"]
        score = 0
        length = len(plaintext)
        for i in range(0, length, 1):
        	char = plaintext[i]
        	if char==' ' or char in histogram:
				score+=histogram.get(char)/length    
		for word in words:
			if word in plaintext:
				score+=17.00/length
       	return score

    def brute_force(self, cipher_text, key_length):
        max_plaintext=""
        max_score=0
        temp_key = itertools.product([i for i in range(256)], repeat=key_length)
        for i in range(2**(8*key_length)):
        	temp = RepeatedKeyCipher(temp_key.next())
        	temp_decryption = temp.decrypt(cipher_text)
        	temp_score = self.plaintext_score(temp_decryption)
        	if max_score < temp_score:
        		max_score = temp_score
        		max_plaintext = temp_decryption
        return max_plaintext

    def smarter_break(self, cipher_text, key_length):
    	possible_keys = []
    	length_cipher = len(cipher_text)
    	for key_position in range(key_length):     				
    		for possible_key in range(256):
    			count=0
    			for block_num in range(0, length_cipher-key_length, key_length):
    				temp_char = cipher_text[block_num + key_position]
    				possible = ord(temp_char) ^ possible_key
    				if chr(possible).isalpha() or chr(possible)==" " or chr(possible)=='\n':
    					count+=1
    			if count/(length_cipher//key_length) > 0.87:
    				possible_keys.append( (key_position, count/(length_cipher//key_length), possible_key) ) 

    	possible_keys.sort(key = lambda x: (x[0],-x[1])) # sort the list by (key_position, count/length)
    	key =[-1 for i in range(key_length)]
    	put_one_option_keys(key, possible_keys)
    	left_keys=left_possible_keys(key, possible_keys)
    	left_keys=insert_value_with_percent_100(key, left_keys)
    	new = []
    	for i in range(key_length):
    		temp=[]
    		for tup in left_keys:
    			if tup[0]==i:
    				temp.append(tup[2])
    		new.append(temp)
    	for i in range(key_length):
    		if len(new[i])==0:
    			new[i].append(key[i])
    	fill_value_when_found_no_candidate(new) # when no valid candidate found, puts a random key in that spot
    	max_plaintext=""
    	max_score=0
    	for option in list(itertools.product(*new)):
    		RKC=RepeatedKeyCipher(option)
    	 	temp = RKC.decrypt(cipher_text)
    	 	if self.plaintext_score(temp) > max_score:
    	 		max_plaintext = temp
    	 		max_score = self.plaintext_score(temp)
    	return max_plaintext

def fill_value_when_found_no_candidate(new):
	for i in range(len(new)):
		if -1 in new[i]:
			new[i][0] = random.choice([x for x in range(256)])

def insert_value_with_percent_100(key, left_keys):
	temp=[]
	for tup in left_keys:
		if tup[1]==1.0:
			key[tup[0]] = tup[2]
		elif key[tup[0]] == -1:
			temp.append(tup)
	return temp

def left_possible_keys(key, possible_keys):
	temp =[]
	for tup in possible_keys:
		if key[tup[0]]==-1:
			temp.append(tup)
	return temp

			


def put_one_option_keys(key, possible_keys):
	counter = [0 for i in range(len(key))]
	for tup in possible_keys:
		counter[tup[0]]+=1
	for i in range(len(counter)):
		if counter[i]==1:
			key[i] = find_key(i,possible_keys)[2]

def find_key(index, lst):
	for tup in lst:
		if tup[0]==index:
			return tup