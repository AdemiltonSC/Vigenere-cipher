# vigenere  cipher

def main():
    alpha_map = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z'
        ]
            
    msg = input("Digite a cifra ou a mensagem a ser cifrada:").lower()
    key = input("Digite a Chave de Encriptação: ").lower()    
    resp = int(input("encriptar(1) ou desencriptar(0): "))
        
    msg2 = ''
    key_aux = 0
    for char in msg:
        # espaços cuidamos bem cedo
        if char == ' ':
            msg2 += ' '
            continue
        
        # pegamos os indices deles no alphabeto.
        msg_i = alpha_map.index(char)
        key_i = alpha_map.index(key[key_aux])
        
        # encripta ou decripta o char
        if resp:
            soma = msg_i + key_i
        else:
            soma = msg_i - key_i
        if soma> 26:
            soma -= 26
        msg2 += alpha_map[soma]

        # incremento do indice da chave
        if key_aux+1 == len(key):
            key_aux = 0
        else:
            key_aux += 1
    print(msg2)


if __name__ == "__main__":
    main()
