# Caesar Cipher

The Caesar Cipher is a cryptographic function that encodes a message by shifting the letters in a phrase by n number of steps up the alphabet. 

For example the phrase "the quick brown fox jumps over the lazy dog" 

Encoded with the Caeser Cipher in which the number of steps = 10 returns: "dro aesmu lbygx pyh tewzc yfob dro vkji nyq"

To encode this I first converted each character within the string to an ascii value. For more on ascii values check here: https://www.asciitable.com/

With a numerical value, we can now add the number of steps to shift up by. For example, if the key is 10 then "a" ---> "k", "b" ---> "l" and so on. However we run into a problem when we want to shift "q" up by 10 steps. We need to cycle around to the top of the alphabet back to "a" and continue the count from there. Also what if we want to choose a higher number of steps, say 100, 1000 etc.

As you can see the primary problem with encoding this cipher in this fashion is the situation in which we have to loop around to the top of the alphabet. The solution to this problem is displayed in detail within the caesar.py file of this project.