def divide():

    #Capturar varias excepciones

    try:
        op1 = (float(input("Introduce el primer número: ")))
        op2 = (float(input("Indroduce el segundo número: ")))

        print("La división es: " + str(op1/op2))

    except ValueError: 
        print("El valor introducido es erroneo")
    
    except ZeroDivisionError:
        print("No se puede dividir entre 0")

    # Si quieres capturar varios errores sin poner muchos except no expecifiques
    # except:
    #     print("Ha ocurrido un Error")

    finally: # lo que viene despues del finally se va a ejecutar siempre
        print("Calculo finalizado")

divide()