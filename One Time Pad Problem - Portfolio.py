# This function accepts a list of keys encrypted using a repeated one-time-pad and decrypts them using brute force.
# A one-time-pad is a method of encryption in which a random string of bits is added to a plaintext to encrypt it.
# A well-implemented one-time-pad is unbreakable, however the method used here repeats the bits for all 11 letters, making it crackable.

bins=[0,1]
keys=[[X,Y,Z,U,E] for X in bins for Y in bins for Z in bins for U in bins for E in bins]

# Contract possiblePlaintexts : list -> list
# Purpose to take a list of keys and decyphers the given cyphertext using the keys provided
# Example possiblePlaintexts([[0,1,0,1,0],[0,0,0,0,0]]) should produce [['Error!', 'O', 'Error!', 'B', 'T', 'J', 'B', 'Error!', 'O', 'T', 'Q'], ['V', 'E', 'V', 'L', 'Z', 'D', 'L', 'V', 'E', 'Z', ' ']]
def possiblePlaintexts(keys):
    return([cypherTextCombiner(key) for key in keys])

# Contract cypherTextCombiner : list -> list
# Purpose to take in a key and output a list of characters decrypted using that key
# Example c
def cypherTextCombiner(key):
    possibleCyphers=[[1,0,1,0,1], [0,0,1,0,0], [1,0,1,0,1], [0,1,0,1,1], [1,1,0,0,1], [0,0,0,1,1], [0,1,0,1,1], [1,0,1,0,1], [0,0,1,0,0], [1,1,0,0,1], [1,1,0,1,0]]
    return([decrypter(cypher,key) for cypher in possibleCyphers])

# Contract decrypter : list, list -> char
# Purpose to decrypt cypher using key to gain a single character
# Example decrypter([0,1,0,1,0], [0,0,1,0,1]) should produce 'P'
def decrypter(cypher,key):
    numberToCharacter={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z',26:' '}
    cypherKeyCombined=[cypher[0]+key[0],cypher[1]+key[1],cypher[2]+key[2],cypher[3]+key[3],cypher[4]+key[4]]
    GF2dict={2:0,1:1,0:0}
    GF2=[GF2dict[X] for X in cypherKeyCombined]
    integer=(GF2[0]*16+GF2[1]*8+GF2[2]*4+GF2[3]*2+GF2[4])
    if integer>26:
        return("Error!")
    else:
        return(numberToCharacter[integer])
