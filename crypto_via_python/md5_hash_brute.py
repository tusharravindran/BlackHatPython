#crypto
import hashlib

print("\033[94m]**************PASSWORD CRACKER ******************")

# To check if the password
# found or not.
pass_found = 0

input_hash = input("\033[92m{+} Enter the hashed password:")
#061a01a98f80f415b1431236b62bb10b
# for example:vivek

pass_doc = input("\033[92m{+} \nEnter passwords filename including path(root / home/):")

try:
    # trying to open the password file
    pass_file = open(pass_doc, 'r')
except:
    print("Error:")
    print(pass_doc, "is not found.\nPlease give the path of file correctly.")
    quit()

# comparing the input_hash with the hashes
# of the words in password file,
# and finding password.

for word in pass_file:
    # encoding the word into utf-8 format
    enc_word = word.encode('utf-8')

    # Hasing a word into md5 hash
    hash_word = hashlib.md5(enc_word.strip())

    # digesting that hash into a hexa decimal value
    digest = hash_word.hexdigest()

    if digest == input_hash:
        # comparing hashes
        print("\033[94mPassword found.\nThe password is:", word)
        pass_found = 1
        break

# if password is not found.
if not pass_found:
    print("Password is not found in the", pass_doc, "file")
    print('\n')
print("\033[93m***************** Thank you ! **********************")
print("\033[94m{+} **********Featured by tushar***********************")

#/root/Desktop/python_programs/crypto/pass.txt pass in txt