try:
    
    def encrypt(ini):
        ini = ini[::-1]
        leng = len(ini)
        if leng<3 and leng>1:
            rev = ini[::-1]
            print(f"The encrypted message is: {rev}")
        else:
            fir = ini[0]
            repl = ini.replace(fir,"")
            a = repl + fir
            fin = random + a + random
            print(f"Your encrypted message is: {fin}")
    def decrypt(dec_str):
        dec_len = len(dec_str)
        if dec_len<3 and dec_len>1:
            rever = dec_str[::-1]
            finn = rever.capitalize()
            print(f"The decrypted message is: {finn}")
        else:
            if random not in dec_str:
                print("Invalid message entered!")
            else:
                dec_fir = dec_str[-4]
                dec_str=dec_str.replace(random,"")
                dec_str=dec_str.replace(dec_str[-1],"")
                dec_str = dec_str[::-1]
                dec_fin = dec_fir + dec_str
                dec_fin = dec_fin.capitalize()
                print(f"The decrypted message is: {dec_fin}")
    print("\n\n")
    print('*' * 10, "Welcome to Manav's Encrypter", '*' * 10)
    print("-" * 50)
    ans = input("Do you want to encrypt or decrypt a message? (y/n): ").lower()
    random = input("Enter three random characters to be present as salting: ")
    while ans=="y":
        ans1 = input("Press 1 for encryption and 2 for decryption or press q to quit: ")
        if ans1 == "1":
            ini = input("Enter a message you want to encrypt: ").lower()
            ini = ini.replace(" ","")
            encrypt(ini)
        elif ans1 == "2":
            dec_str = input("Enter the message you want to decrypt: ").lower()
            dec_str = dec_str.replace(" ","")
            decrypt(dec_str)
        elif ans1 == "q":
            break
        else:
            print("Invalid input!")
            break

finally:
    print("Thanks for using my encrypter!")
