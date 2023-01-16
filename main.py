from tkinter import *
# vigenere  cipher

def cipherSolver(msg, key, tipo):
    alpha_map = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z', ' '
        ]

    msg = ''.join(list(char for char in msg.lower() if char in alpha_map))
    key = ''.join(key.split(' ')).lower()
    resp = tipo

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
        if not resp:
            soma = msg_i + key_i
        else:
            soma = msg_i - key_i

        if soma>= 26:
            soma -= 26
        
        msg2 += alpha_map[soma]

        # incremento do indice da chave
        if key_aux+1 == len(key):
            key_aux = 0
        else:
            key_aux += 1
    print(msg2)
    return msg2



class app:
    def __init__(self, master=None):
        # Constantes
        self.BG_COLOUR = "#bbaabb"
        self.BUTTON_BG_COLOUR = "#aa1a44"
        self.BUTTON_BG_COLOUR = "#aaaaff"
        self.FONT_COLOR = "#111177"

        # configuração do root
        self.root = Tk()
        self.root.title("Vigenere Cipher")
        self.root.geometry("500x450+30+30")
        self.root.maxsize(500, 450)
        self.root.resizable(0, 0)
        self.root.config(bg=self.BG_COLOUR)


        # Confifurando as Rows
        self.row1 = Frame(self.root, height=100, bg=self.BG_COLOUR)
        self.row1.pack_propagate(0)
        self.row2 = Frame(self.root, height=100, bg=self.BG_COLOUR)
        self.row2.pack_propagate(0)
        self.row3 = Frame(self.root, height=100, bg=self.BG_COLOUR)
        self.row3.pack_propagate(0)
        self.row3.columnconfigure(0, weight=1)
        self.row3.columnconfigure(1, weight=1)
        self.row4 = Frame(self.root, height=100, bg=self.BG_COLOUR)
        self.row4.pack_propagate(0)

        # Container position
        self.row1.pack(pady=(50, 0), fill="both")
        self.row2.pack(pady=(25, 0), fill="both")
        self.row3.pack(pady=(25, 0), fill="both")
        self.row4.pack(pady=(25, 0), fill="both")

        # Mensagem
        self.msgV = StringVar(self.root, "Sua mensagem: ")
        self.msg = Entry(self.row1, font=("verdana", 20), textvariable=self.msgV, fg=self.FONT_COLOR)
        self.msg.bind("<FocusIn>", self.handle_focus)

        # Key
        self.keyV = StringVar(self.root, value="Sua key")
        self.key = Entry(self.row2, font=("verdana", 20), textvariable=self.keyV, fg=self.FONT_COLOR)
        self.key.bind("<FocusIn>", self.handle_focus)
        
        # Encriptar ou Decriptar Buttons
        self.btn = Button(self.row3, text="ENCRIPTAR", font=("verdana 12 bold"), height=2, fg=self.FONT_COLOR,
                            bg=self.BUTTON_BG_COLOUR, command = lambda: self.criptacao(0)
                            )
        self.btn2 = Button(self.row3, text="DECRIPTAR", font=("verdana 12 bold"), height=2, fg=self.FONT_COLOR,
                            bg=self.BUTTON_BG_COLOUR, command = lambda: self.criptacao(1)
                            )
                                    
        # Mensagem 2
        self.msg2V = StringVar(self.root, value="Criptado")
        self.msg2 = Entry(self.row4, font=("verdana", 20), fg=self.FONT_COLOR, state="readonly",
                        textvariable=self.msg2V)

        # Position/ Packing
        self.msg.pack(expand="true")
        self.key.pack(expand="true")
        self.btn.grid(row=0, column=0, sticky="WE", padx=(50,5))
        self.btn2.grid(row=0, column=1, sticky="WE", padx=(5, 50))
        self.msg2.pack(expand="true")

        self.root.mainloop()
    
    def handle_focus(self, event):
        if event.widget == self.msg:
            self.msgV.set("")
        if event.widget == self.key:
            self.keyV.set("")

    def criptacao(self, tipo=0):
        # Função dos botões
        # tipo 0 é pra encripitar e 1 pra decriptar
        valor1 = self.msgV.get()
        valor2 = self.keyV.get()
        valor3 = cipherSolver(valor1, valor2, tipo)
        self.msg2V.set(valor3)


if __name__ == "__main__":
    app()
    
