import random
special_chars = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+",";",":","<",",",".",">"]
normal_chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
normal_chars_upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
nums = ["1","2","3","4","5","6","7","8","9","0"]
possible_chars = [normal_chars, normal_chars_upper, nums, special_chars]
password = ""

def randomize():
   pass_length = 16
   while pass_length > 0:
       char_type = random.randint(0,len(possible_chars))
       char = possible_chars[char_type - 1][random.randint(0,len(possible_chars[char_type - 1]) - 1)]
       global password
       password = password + char
       pass_length-=1
   else:
       return password

def main():
    print(f"Your randomly generated password is: {randomize()}")

if __name__ == "__main__":
    main()
