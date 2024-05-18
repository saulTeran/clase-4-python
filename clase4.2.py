while True:   
    print("""ingrese la talla
        S (50$)
        M (55$)
        L (60$)
        XL (65$)
        XXL (70$)""")
    talla=input().upper()
    print("ingrese cantidad")
    cantidad=int(input())
    precio=0
    match talla:
        case "S":
            precio=50
        case "M":
            precio=55
        case "L":
            precio=60
        case "XL":
            precio=65
        case "XXL":
            precio=70
        case _:
            print("talla invalida")
    tallaValida=(talla=="S" or talla=="M" or talla=="L" or talla =="XL")
    total=precio*cantidad
    descuento=0
    if cantidad>=6 and cantidad<=11:
        descuento=0.05
    elif cantidad>=12 and cantidad<=24:
        descuento=0.1
    elif cantidad > 24:
        descuento=0.15

    montoDescontar=total*descuento
    totalDescuento=total-montoDescontar

    if precio>0:
        print(f"""talla seleccionada: {talla}
    precio: {precio}
    cantidad a llevar: {cantidad}
    total a pagar: {total}
    descuento obtenido: {descuento*100}
    monto a descontar: {montoDescontar}
    total a pagar: {totalDescuento}""")

    if not tallaValida:
        print("no se puede procesar la venta")
    print("presione espacio para detener las ventas")
    resp=input()
    if resp==" ":
     break