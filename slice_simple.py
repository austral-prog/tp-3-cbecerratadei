def slice_simple():
    texto = "Awesome"
    awe = (texto[0:3]).lower()
    eso = (texto[2:5]).lower()
    awesome = texto[0:4].lower() + texto[-3:].lower()

    print(awe)
    print(eso)
    print(awesome)
slice_simple()
