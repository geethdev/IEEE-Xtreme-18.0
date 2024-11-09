import sys
sys.set_int_max_str_digits(10**7 + 10)

def es_potencia_de_tres(N: str) -> int:

    if N[0] == '-' or N == '0':
        return -1
    if N == '1':
        return 0
        
    if N[-1] not in '1379':
        return -1
    
    if len(N) <= 100:  
        n = int(N)
        x = 0
        potencia = 1
        while potencia <= n:
            if potencia == n:
                return x
            if x > 100:  
                break
            x += 1
            potencia *= 3
        return -1
    

    from math import log
    
    d = len(N)

    
    exp_aproximada = (d - 1) / log(3, 10)  
    
    exponentes_potenciales = range(int(exp_aproximada - 2), int(exp_aproximada + 3))
    
    for x in exponentes_potenciales:
        if x < 0:
            continue
        try:

            potencia = pow(3, x)
            potencia_str = str(potencia)
            
            if potencia_str == N:
                return x
            if len(potencia_str) > len(N):
                break
        except OverflowError:
            continue
    
    return -1

def main():
    try:
        N = input().strip()
        resultado = es_potencia_de_tres(N)
        print(resultado)
        return 0
    except Exception as e:
        print(-1)
        return 1

if __name__ == "__main__":
    main()