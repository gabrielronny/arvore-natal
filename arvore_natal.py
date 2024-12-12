def imprimir_arvore_de_natal(altura):
    for i in range(altura):
        # Espaços em branco para centralizar a árvore
        print(" " * (altura - i - 1), end="")
        
        # Asteriscos para formar a camada da árvore
        print("*" * (2 * i + 1))

    # Imprimir o tronco da árvore
    print(" " * (altura - 1) + "|")

    # Imprimir "HOHOHO" em estilo de terminal
    print()
    hohoho = [ 
        "________  ________  __        ______  ________        __    __   ______  ________   ______   __              __    __   ______   __    __   ______   __    __   ______  ",
        "|        \|        \|  \      |      \|        \      |  \  |  \ /      \|        \ /      \ |  \            |  \  |  \ /      \ |  \  |  \ /      \ |  \  |  \ /      \ ",
        "| $$$$$$$$| $$$$$$$$| $$       \$$$$$$ \$$$$$$$$      | $$\ | $$|  $$$$$$\\$$$$$$$$|  $$$$$$\| $$            | $$  | $$|  $$$$$$\| $$  | $$|  $$$$$$\| $$  | $$|  $$$$$$\ ",
        "| $$__    | $$__    | $$        | $$      /  $$       | $$$\| $$| $$__| $$  | $$   | $$__| $$| $$            | $$__| $$| $$  | $$| $$__| $$| $$  | $$| $$__| $$| $$  | $$",
        "| $$  \   | $$  \   | $$        | $$     /  $$        | $$$$\ $$| $$    $$  | $$   | $$    $$| $$            | $$    $$| $$  | $$| $$    $$| $$  | $$| $$    $$| $$  | $$",
        "| $$$$$   | $$$$$   | $$        | $$    /  $$         | $$\$$ $$| $$$$$$$$  | $$   | $$$$$$$$| $$            | $$$$$$$$| $$  | $$| $$$$$$$$| $$  | $$| $$$$$$$$| $$  | $$",
        "| $$      | $$_____ | $$_____  _| $$_  /  $$___       | $$ \$$$$| $$  | $$  | $$   | $$  | $$| $$_____       | $$  | $$| $$__/ $$| $$  | $$| $$__/ $$| $$  | $$| $$__/ $$",
        "| $$      | $$     \| $$     \|   $$ \|  $$    \      | $$  \$$$| $$  | $$  | $$   | $$  | $$| $$     \      | $$  | $$ \$$    $$| $$  | $$ \$$    $$| $$  | $$ \$$    $$",
        " \$$       \$$$$$$$$ \$$$$$$$$ \$$$$$$ \$$$$$$$$       \$$   \$$ \$$   \$$   \$$    \$$   \$$ \$$$$$$$$       \$$   \$$  \$$$$$$  \$$   \$$  \$$$$$$  \$$   \$$  \$$$$$$ ",                                                                                                                                                                   
    ]

    for linha in hohoho:
        print(" " * (altura - len(linha) // 2) + linha)
    print("")

if __name__ == "__main__":
    try:
        altura = int(input("Digite a altura da árvore de Natal: "))
        if altura > 0:
            imprimir_arvore_de_natal(altura)
        else:
            print("Por favor, insira um número inteiro positivo.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro positivo.")