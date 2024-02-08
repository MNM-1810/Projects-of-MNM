import random
try:
    
    saltings = ["!","@","#","$","%","^","&","*","(",")","_","-","=","+","[","]","{","}",";",":","'","<",">",",",".","?","/","|","\\","`","~","1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    def encrypt(ini):
        leng = len(ini)
        if leng<3 and leng>1:
            rev = ini[::-1]
            print(f"The encrypted message is: {rev}")
        else:
            fir = ini[0]
            repl = ini.replace(fir,"")
            repl = repl[::-1]
            fin = enc + repl + enc + fir
            print(f"Your encrypted message is: {fin}")
    def decrypt(dec_str):
        dec_len = len(dec_str)
        if dec_len<3 and dec_len>1:
            rever = dec_str[::-1]
            finn = rever.capitalize()
            print(f"The decrypted message is: {finn}")
        else:
                dec_fir = dec_str[-1]
                dec_str = dec_str.replace(dec_fir,"")
                dec_str = dec_str.replace(dec_str[-1],"")
                dec_str = dec_str.replace(dec_str[-1],"")
                dec_str = dec_str.replace(dec_str[-1],"")
                dec_str = dec_str[::-1]
                dec_fin = dec_fir + dec_str
                dec_fin = dec_fin.capitalize()
                print(f"The decrypted message is: {dec_fin}")
    print("\n\n")
    print('*' * 10, "Welcome to Manav's Secret Coder", '*' * 10)
    print("-" * 50)
    ans = input("Do you want to encrypt or decrypt a message? (y/n): ").lower()
    print(f"You have chosen {ans}")
    if ans=="y": 
        while True:      
            ans1 = input("Press 1 for encryption and 2 for decryption or press q to quit: ")
            if ans1 == "1":
                    sal = saltings[random.randint(0, 93)]
                    sal1 = saltings[random.randint(0, 93)]
                    sal2 = saltings[random.randint(0, 93)]
                    enc = sal + sal1 + sal2
                    ini = input("Enter a message you want to encrypt: ").lower()
                    ini = ini.replace(" ","")
                    encrypt(ini)
            elif ans1 == "2":
                    saltinga=saltings[random.randint(33, 93)]
                    salting=saltings[random.randint(33, 93)]
                    saltingb=saltings[random.randint(33, 93)]
                    dec_key = salting + saltinga + saltingb
                    print(f"Your decryption key is {dec_key} please use it at the start and at the end of the message for decryption!")
                    dec_str = input("Enter the message you want to decrypt: ").lower()
                    dec_str = dec_str.replace(" ","")
                    decrypt(dec_str)
            elif ans1 == "q":
                    break
            else:
                    raise  ValueError("Invalid input entered!")
    elif ans=="n":
        pass
    else:
        raise ValueError("Invalid input entered!")

        

finally:
    print("Thanks for using my secret code program!")
