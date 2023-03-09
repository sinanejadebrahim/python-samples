#!/usr/bin/python3
import requests
import hashlib
import sys


def req_api_data(char):
    url = 'https://api.pwnedpasswords.com/range/' + char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'error fetching: {res.status_code }')

    return res
    

def get_password_leak(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

    
def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1password[:5], sha1password[5:]
    
    response = req_api_data(first5)
    
    return get_password_leak(response, tail)
    
   
def hash_build(password):
    hash_methods = ['sha1', 'sha256', 'sha512', 'sha224', 'sha384', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'blake2b', 'blake2s', 'md5', 'blake2b', 'blake2s']
    hashes = {}
    
    for i in hash_methods:
    
        hash_obj = hashlib.new(i)
        hash_obj.update(password.encode('utf-8'))
        hash_value = hash_obj.hexdigest()
        
        hashes[i] = hash_value
        
    
    for key,value in hashes.items():
        print(key.upper(),value)
        


def main(password):
    count = pwned_api_check(password)
    if count:
        print(f'not a good password, {password} was found {count} times')
    else:
        print(f'good password, {password} was NOT found')




if __name__ == '__main__':
    main(sys.argv[1])
    print("###### generated hashes: ######")
    hash_build(sys.argv[1])
