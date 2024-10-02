def descobrir_interruptores():
    print("Primeira ida:")
    print("Ligando interruptor 1...")
    print("Desligando interruptor 1 e ligando interruptor 2...")

    print("\nSegunda ida:")
    sala_lampadas = [False, False, False]  
    sala_lampadas[0] = True  
    sala_lampadas[1] = True  

    for i, estado_lampada in enumerate(sala_lampadas):
        if estado_lampada:
            print(f"A lâmpada {i + 1} está acesa e está conectada ao interruptor 1.")
        else:
            print(f"A lâmpada {i + 1} está desligada.")
            if i == 1:
                print(f"A lâmpada {i + 1} está morna, então está conectada ao interruptor 2.")
            else:
                print(f"A lâmpada {i + 1} está fria, então está conectada ao interruptor 3.")
descobrir_interruptores()