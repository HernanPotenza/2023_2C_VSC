# if value.replace(".","",1).isdigit() == True:
#                 valor_normalizado = float(value)

#                 ```python
# txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# txt2 = "My name is {0}, I'm {1}".format("John",36)
# txt3 = "My name is {}, I'm {}".format("John",36)
# ```

obtener_email_lambda = lambda nombre, apellido: f"{nombre[0]}.{apellido}@utn-fra.com.ar"
print(obtener_email_lambda("Facundo", "Falcone"))