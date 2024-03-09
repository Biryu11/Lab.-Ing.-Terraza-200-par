while True:
    print("El codigo se ejecuta al menos una vez.")

    respuesta = input("Desea seguir continuando? (Si/No): ".lower())

    assert respuesta in ["si", "no"], "Responder por favor con SI o NO"

    if respuesta == "no":
        break



