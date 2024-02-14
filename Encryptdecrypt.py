alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position+shift_key)%26
            cipher_text+=alphabet[new_position]
        else:
            cipher_text+=char
    print(f"here's is the encryption {cipher_text}")   
def decryption(cipher_text,shift_key): 
    plain_text=""
    for char in cipher_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position+shift_key)%26
            plain_text+=alphabet[new_position]
        else:
            plain_text+=char
    print(f"here's is the decryption {plain_text}")  
        
wanna_end=False
while not wanna_end:
    what_to_do=input("type 'encrypt' for encryption and 'decrypt' for 'decryption':\n")
    text=input("enter the text you want to encrpt:\n")
    shift=int(input("enter the shift key:\n"))
    if what_to_do=="encrypt":
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do=="decrypt":
        decryption(cipher_text=text,shift_key=shift)

    play_again=input("type 'yes' to continue and 'no' to exit") 
    if play_again=="no":
        wanna_end=True
        print("have a good day ,bye!")
