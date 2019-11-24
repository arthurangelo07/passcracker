# passcracker
Hash tool and cracker
This tool has for goal to crack password as well as generate MD5 hash passwords from a text input. 

The MD5 algorithm is an extension of the MD4, it is more conservative and slower than MD4 and provides a bit more security in exchange of speed. 

In cryptography, a hash function is an algorithm that maps data of any size to a bit string of fixed size, the output is known as the hash or message-digest. Hashing then in this case can be a more secure way to store passwords.

PassCracker is written in Python and provides a mean to decode and encode common passwords if they are listed in the local list of common passwords hosted in the same folder as the script.  

It uses the hash and compare it to the local dictionary keys (passwords). PassCracker can be used when passwords are lost but their hash could be retrieved in the password file on Linux system for example. 

PassCracker also provides an approach to securing passwords on other systems by hashing the cleartext password. Storing cleartext password is a security malpractice that can lead to unfortunate incidents

Usage:

Start the script to view the different options
- Enter 1 for encoding a hash: Prompt the user to enter a password to convert in hash
- Enter 2 for decoding a hash: You will be prompted to the hash of a password to recover, PassCracker will decode the hash and reveal the password in clear text



Arthur
