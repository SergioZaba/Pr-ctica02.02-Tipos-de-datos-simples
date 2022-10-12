precio_usuario = str(input("Escriba el dinero que cuesta el producto"
                           " en euros y centimos con dos decimales\n"))
print("son", precio_usuario[:precio_usuario.find(",")], "euros y",
      precio_usuario[-2::], "centimos.")
