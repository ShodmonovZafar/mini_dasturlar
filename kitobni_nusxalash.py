def f(toq_son, juft_son):
    n = (juft_son - (toq_son - 1)) // 4 
    l = []
    for i in range(n):
        l.append(toq_son)
        l.append(juft_son)
        toq_son += 2
        juft_son -= 2
    return l



def f1(toq_son, juft_son):
    n = (juft_son - (toq_son - 1)) // 4
    l = []
    toq_son = toq_son + 2*n
    juft_son = toq_son - 1
    for i in range(n):
        l.append(toq_son)
        l.append(juft_son)
        toq_son += 2
        juft_son -= 2
    return l

def main():
    while True:
        toq_son = int(input("Toq sonni kiriting: "))
        if toq_son == 0:
            break
        juft_son = int(input("Juft sonni kiriting: "))
        print(f(toq_son, juft_son))
        print(f1(toq_son, juft_son))
        print()

    
main()
        
