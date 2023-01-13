from tkinter import *
# vigenere  cipher

def cli():
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



class app:
    def __init__(self, master=None):
        self.root = Tk()
        self.root.title("Vigenere Cipher")
        self.root.geometry("500x450+30+30")
        self.root.maxsize(500, 450)
        self.root.resizable(0, 0)
        self.root.config(bg="black")

        self.row1 = Frame(self.root, height=100)
        self.row1.pack_propagate(0)
        self.row2 = Frame(self.root, height=100)
        self.row2.pack_propagate(0)
        self.row3 = Frame(self.root, height=100)
        self.row3.pack_propagate(0)
        self.row3.columnconfigure(0, weight=1)
        self.row3.columnconfigure(1, weight=1)
        self.row4 = Frame(self.root, height=100)
        self.row4.pack_propagate(0)

        self.row1.pack(pady=(50,0), fill="both")
        self.row2.pack(fill="both")
        self.row3.pack(fill="both")
        self.row4.pack(fill="both")

        # Mensagem
        self.msgV = StringVar(self.root, value="Sua mensagem")
        self.msg = Entry(self.row1, font=("verdana", 20))
        self.msg.pack()

        # Key
        self.keyV = StringVar(self.root, value="key")
        self.key = Entry(self.row2, font=("verdana", 20))
        self.key.pack()
        
        # Encriptar ou Decriptar
        self.btn = Button(self.row3)
        self.btn.grid(row=0, column=1, sticky="WE")

        self.btn2 = Button(self.row3)
        self.btn2.grid(row=0, column=2, sticky="WE")
        
        # Mensagem 2
        self.msg2V = StringVar(self.root, value="Criptado")
        self.msg2 = Entry(self.row4, font=("verdana", 20))
        self.msg2.pack()        

        self.root.mainloop()
    

if __name__ == "__main__":
    app()
    
