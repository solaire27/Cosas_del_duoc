descuento = "DESC"
vip = "VIP"
inicio = input("Cúanto cuesta el producto que deseas comprar?($precio) ").strip(" ").strip(".").strip(",")
if inicio.startswith("$") and len(inicio) > 3:
    if inicio[1:].isdigit():
        valid = input("Ingrese su código de descuento: ").upper().strip(" ")
        pr = inicio.strip("$")
        pr = int(pr)
        if valid.startswith("DESC"):
            precio = (pr * 0.9)
            precio = f"{precio:0f}"
            print(f"Su valor final es {precio}")
        elif valid.startswith("VIP"):
            precio = (pr * 0.85)
            precio = f"{precio:0f}"
            print(f"Su valor final es {precio}")
        else:
            print(f"Su valor final es {inicio}")

    else:
        print("Por favor ingresa un precio válido")
else:
    print("Por favor ingrese un precio válido")