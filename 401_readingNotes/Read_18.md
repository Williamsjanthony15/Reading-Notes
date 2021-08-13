#Ciphering text and Deciphering text.

## Encrypting a message
The Caesar Cipher is a simple substitution cipher which replaces each original letter with a different letter in the alphabet by shifting the alphabet by a certain amount.
To make the encrypted message above, I shifted the alphabet by 6 and used this substitution table:
A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z
G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z	A	B	C	D	E	F
S shifts 6 letters over to Y, E shifts 6 letters over to K, etc. Here's the first word and its shifts:
S	E	C	R	E	T
Y	K	I	X	K	Z

## Decrypting a message
According to historical records, Caesar always used a shift of 3. As long as his message recipient knew the shift amount, it was trivial for them to decode the message.
Imagine Caesar sends this message to a comrade:
EHZDUH EUXWXV
The comrade uses this substitution table, where the alphabet is shifted by 3:
A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z
D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z	A	B	C
They can then decode the message with certainty. The first letter "E" was shifted by 3 from "B", the second letter "H" was shifted by 3 from "E", etc. The result is this ominous message:
BEWARE BRUTUS


## Cracking the cipher
Imagine that a very literate and savvy enemy intercepts one of Caesar's messages.
RZ VMZ WMDIBDIB VGG AJMXZN OJ EJDI RDOC XGZJKVOMV OJ YZAZVO OCZ ZIZHT LPZZI VO OCZ IDGZ YZGOV
That enemy does not know that Caesar always uses a shift of 3, so he must attempt to "crack" the cipher without knowing the shift.
There are three main techniques he could use: frequency analysis, known plaintext, and brute force.
## Frequency analysis
Human languages tend to use some letters more than others. For example, "E" is the most popular letter in the English language. We can analyze the frequency of the characters in the message and identify the most likely "E" and narrow down the possible shift amounts based on that.

## Brute force
There are only 25 possible shifts (not 26 — why not?). The enemy could take some time to try out each of them and find one that yielded a sensible message. They wouldn't even need to try the shifts on the entire message, just the first word or two.

## Encryption, decryption, and cracking
Thanks to this exploration of the Caesar Cipher, we now understand the three key aspects of data encryption:
Encryption: scrambling the data according to a secret key (in this case, the alphabet shift).
Decryption: recovering the original data from scrambled data by using the secret key.
Code cracking: uncovering the original data without knowing the secret, by using a variety of clever techniques.
Whenever we consider a possible encryption technique, we need to think about all those aspects: how easy is it to encrypt? how easy is it to decrypt? And most importantly, how easy is it for a nefarious individual to crack the code?





