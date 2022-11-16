import random

def password(pw_len=8):

    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ><-_'
    last_pos = len(all_chars) - 1
    pw = ''
    for _ in range(pw_len):
        index = random.randint(0, last_pos)
        pw += all_chars[index]
    return pw

if __name__ == '__main__':
    print(password())
    
