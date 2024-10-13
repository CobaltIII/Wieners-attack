import random
import math

def check(d, e, N): #to check if the guessed private exponent is indeed a correct one with 10 random guessed numbers.
    ans = True
    for i in range(10):
        x = random.randint(1 , N - 1)
        if pow(pow(x, e, N), d, N) != pow(x, 1, N):
            ans = False
            break
    return ans


def Wiener_Attack(e, N): #(public exponent, modulo) #works when assumed that private_exponent < 1/3 * sqrt(sqrt(N))
    value = e / N
    c_values = {0:math.floor(value)}
    epsilon_values = {0:value - c_values[0]}
    
    for j in range(1, 50):
        c_values[j] = math.floor(1 / epsilon_values[j-1])
        epsilon_values[j] = (1 / epsilon_values[j-1]) - c_values[j]
        if epsilon_values[j] == 0:
            break        
    
    ab_values = {0:[math.floor(value) , 1], 1: [c_values[0]*c_values[1] + 1, c_values[1]]}
    for j in range(2, 30):
        ab_values[j] = [(c_values[j] * ab_values[j-1][0]) + ab_values[j-2][0] , (c_values[j] * ab_values[j-1][1]) + ab_values[j-2][1]]

    for j in range(1, 30):
        if check(ab_values[j][1], e, N):
            print("Broken. d = " , ab_values[j][1])
            return
    
    print("Not breakable by Weiner.")

print("""
Choose 1 for a pre-given input
Choose 2 for your own input
Anything else to exit
""")

n = input("Enter input: ")

if n in ["1" , "2"]:
    if n == "1":
        print("""
        Using pre-given Input : 
        Public exponent = 6792605526025
        Public mod = 9449868410449
        """)
        Wiener_Attack(6792605526025, 9449868410449)
    else:
        e = input("Enter your public exponent : ")
        N = input("Enter your public mod : ")
        
        try : 
            e = int(e)
            N = int(N)
            Wiener_Attack(e , N)  
        except:
            print("Invalid input, please try again")

print("\n\n--------------A project by Dhruv Jaiswal-----------")
#
#
#                            ╱|、
#                           (˚ˎ。7  
#                           |、˜ 〵          
#                           じしˍ,)ノ
#
