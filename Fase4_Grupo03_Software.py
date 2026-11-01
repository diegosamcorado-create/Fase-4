# Permite convertir los datos de Python a JSON y recuperarlos después.
import json

# Permite comprobar si el archivo existe y si está vacío.
import os


# Aquí se pueden agregar más dominios
dominios_permitidos = ["gmail", "outlook", "hotmail", "nivela"]

# Aquí se pueden agregar más terminaciones.
terminaciones_permitidas = ["com", "org", "net", "gt"]

# Aquí se pueden agregar más caracteres especiales.
caracteres_especiales = [
    ".", ",", ":", ";", "?", "!", "@", "#", "_", "-", "$", "%", "&", "*",
    "=", "(", ")", "[", "]", "{", "}"
]


def mostrar_inicio():
    # Mostrar las opciones y devolver el texto sin convertirlo a número.
    print("Inicio")
    print()
    print("1. Iniciar sesión")
    print("2. Finalizar sesión")
    return input("Elija un número: ")


def mostrar_requisitos():
    # Explicar el formato del usuario antes de pedir los datos.
    print()
    print("Requisitos para el nombre de usuario:")
    print("- Debe tener este orden exacto: nombre, símbolo @, dominio y terminación.")
    print("- El nombre debe estar todo en minúscula y sin espacios.")
    print("- Dominios permitidos: gmail, outlook, hotmail, nivela.")
    print("- Terminaciones permitidas: .com, .org, .net, .gt")
    print("- Ejemplo válido: juan@gmail.com")
    print()

    # Explicar las condiciones de la contraseña.
    print("Requisitos para la contraseña (sin importar el orden):")
    print("- Mínimo 8 caracteres.")
    print("- Al menos una letra mayúscula.")
    print("- Al menos una letra minúscula.")
    print("- Al menos un número.")
    print("- Al menos un carácter especial de esta lista: . , : ; ? ! @ # _ - $ % & * = ( ) [ ] { }")
    print()


def validar_usuario(usuario):
    # Comprobar que exista exactamente un símbolo @.
    if usuario.count("@") != 1:
        return False

    # Separar el nombre de la parte que contiene el dominio.
    partes_usuario = usuario.split("@")
    nombre = partes_usuario[0]
    dominio_y_terminacion = partes_usuario[1]

    # El nombre no puede estar vacío.
    if nombre == "":
        return False

    # Rechazar mayúsculas y espacios, incluidos tabulaciones y saltos de línea.
    for caracter in nombre:
        if caracter.isupper():
            return False
        if caracter.isspace():
            return False

    # Debe haber solo un punto entre el dominio y la terminación.
    partes_dominio = dominio_y_terminacion.split(".")
    if len(partes_dominio) != 2:
        return False

    dominio = partes_dominio[0]
    terminacion = partes_dominio[1]

    # Revisar que el dominio esté permitido.
    if dominio not in dominios_permitidos:
        return False

    # Revisar que la terminación esté permitida.
    if terminacion not in terminaciones_permitidas:
        return False

    return True


def validar_contrasena(contrasena):
    # Revisar primero el largo mínimo.
    if len(contrasena) < 8:
        return False

    # Estas variables indican qué condiciones se han encontrado.
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_especial = False

    # Recorrer la contraseña y revisar cada carácter.
    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
        if caracter.islower():
            tiene_minuscula = True
        if caracter.isdigit():
            tiene_numero = True
        if caracter in caracteres_especiales:
            tiene_especial = True

    # Todas las condiciones deben cumplirse.
    if tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial:
        return True

    return False


def iniciar_sesion():
    mostrar_requisitos()

    # Pedir ambos datos y validarlos por separado.
    usuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")
    usuario_valido = validar_usuario(usuario)
    contrasena_valida = validar_contrasena(contrasena)

    # Devolver el usuario si cumple todo, o un texto vacío si hay un fallo.
    if usuario_valido and contrasena_valida:
        return usuario

    return ""


# ==================== MÓDULO DE OBRAS ====================

# Listas y límites que se pueden ampliar más adelante.
caracteres_especiales_obras = [
    ".", ",", ":", ";", "?", "!", "@", "#", "_", "-", "$", "%", "&", "*",
    "=", "(", ")", "[", "]", "{", "}", "/"
]
zona_maxima = 25
anio_minimo = 2000
anio_maximo = 2100

# Orden en que se piden los datos al registrar una obra.
campos_obra = [
    "titulo", "descripcion", "cliente_nombre", "cliente_apellido", "zona",
    "direccion", "colonia", "informacion", "fecha_inicio", "fecha_fin",
    "presupuesto", "gerente_nombre", "gerente_apellido"
]

etiquetas_obras = {
    "titulo": "Título de obra",
    "descripcion": "Descripción",
    "cliente_nombre": "Nombre del cliente",
    "cliente_apellido": "Apellido del cliente",
    "zona": "Zona",
    "direccion": "Dirección",
    "colonia": "Colonia",
    "informacion": "Información adicional",
    "fecha_inicio": "Fecha de inicio estimada",
    "fecha_fin": "Fecha de finalización estimada",
    "presupuesto": "Presupuesto inicial en quetzales",
    "gerente_nombre": "Nombre del gerente de obra",
    "gerente_apellido": "Apellido del gerente de obra"
}

# Opciones del menú de actualizar: algunas agrupan varios campos.
opciones_edicion_obra = [
    ["titulo"],
    ["descripcion"],
    ["cliente_nombre", "cliente_apellido"],
    ["zona"],
    ["direccion"],
    ["colonia"],
    ["informacion"],
    ["fecha_inicio"],
    ["fecha_fin"],
    ["presupuesto"],
    ["gerente_nombre", "gerente_apellido"]
]
nombres_opciones_edicion_obra = [
    "Título de obra",
    "Descripción",
    "Cliente",
    "Zona",
    "Dirección",
    "Colonia",
    "Información adicional",
    "Fecha de inicio estimada",
    "Fecha de finalización estimada",
    "Presupuesto inicial",
    "Gerente de obra"
]


# ==================== ALMACENAMIENTO ====================

def cargar_obras():
    # Comprobar si existe el archivo en la carpeta de trabajo.
    if not os.path.exists("obras.json"):
        return []

    # Comprobar si el archivo tiene cero bytes, es decir, está vacío.
    if os.path.getsize("obras.json") == 0:
        return []

    # Abrir el archivo para leer texto en UTF-8.
    archivo = open("obras.json", "r", encoding="utf-8")
    # Leer todo el contenido del archivo como texto.
    contenido = archivo.read()
    # Cerrar el archivo después de leerlo.
    archivo.close()

    # Considerar vacío también un archivo que solo contiene espacios.
    if contenido.strip() == "":
        return []

    # Convertir el texto JSON en una lista de diccionarios de Python.
    lista_obras = json.loads(contenido)

    # Las obras guardadas antes de existir los códigos reciben uno ahora.
    hubo_cambios = False
    for posicion in range(len(lista_obras)):
        if "codigo" not in lista_obras[posicion]:
            obra_con_codigo = {"codigo": generar_codigo_obra(lista_obras)}
            obra_con_codigo.update(lista_obras[posicion])
            lista_obras[posicion] = obra_con_codigo
            hubo_cambios = True

    if hubo_cambios:
        guardar_obras(lista_obras)

    return lista_obras


def guardar_obras(lista_obras):
    # Abrir para escribir: crea el archivo o reemplaza su contenido.
    archivo = open("obras.json", "w", encoding="utf-8")
    # Guardar la lista completa como JSON, con sangría y tildes legibles.
    json.dump(lista_obras, archivo, indent=4, ensure_ascii=False)
    # Cerrar el archivo para completar la escritura.
    archivo.close()


# ==================== VALIDACIONES ====================

def solo_digitos(texto):
    # Un texto vacío no cuenta como número.
    if texto == "":
        return False

    # Comparar con los dígitos de 0 a 9 evita errores al usar int().
    for caracter in texto:
        if caracter not in "0123456789":
            return False

    return True


def texto_permitido(texto):
    # Admitir letras, números, espacios y los especiales permitidos.
    for caracter in texto:
        if not caracter.isalpha() and not caracter.isdigit() and caracter != " " and caracter not in caracteres_especiales_obras:
            return False

    return True


def validar_titulo_obra(texto):
    # El campo no puede estar vacío.
    if texto == "":
        return False

    # El primer carácter debe ser una letra mayúscula.
    if not texto[0].isalpha() or not texto[0].isupper():
        return False

    return texto_permitido(texto)


def validar_nombre_persona(texto):
    # Sirve para nombres y apellidos del cliente y del gerente.
    if texto == "":
        return False

    # El primer carácter debe ser una letra mayúscula.
    if not texto[0].isalpha() or not texto[0].isupper():
        return False

    # Solo letras, espacios (nombres compuestos) y guiones.
    for caracter in texto:
        if not caracter.isalpha() and caracter != " " and caracter != "-":
            return False

    return True


def validar_zona(texto):
    if not solo_digitos(texto):
        return False

    numero = int(texto)
    return numero >= 1 and numero <= zona_maxima


def validar_direccion(texto):
    if texto == "":
        return False

    return texto_permitido(texto)


def validar_colonia(texto):
    return validar_direccion(texto)


def validar_monto(texto):
    # Formato: dígitos y, de forma opcional, un punto con 1 o 2 decimales.
    partes = texto.split(".")
    if len(partes) > 2:
        return False

    if not solo_digitos(partes[0]):
        return False

    if len(partes) == 2:
        if not solo_digitos(partes[1]) or len(partes[1]) > 2:
            return False

    # El presupuesto debe ser mayor que cero.
    return float(texto) > 0


def dias_del_mes(mes):
    if mes == 2:
        return 29

    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30

    return 31


def fecha_a_tupla(fecha):
    # Convertir "05/03/2027" en (2027, 3, 5) para poder comparar fechas.
    partes = fecha.split("/")
    return (int(partes[2]), int(partes[1]), int(partes[0]))


def formatear_monto(presupuesto):
    return "Q " + format(float(presupuesto), ",.2f")


def titulo_repetido(lista_obras, titulo, titulo_actual):
    # Comparar sin distinguir mayúsculas de minúsculas.
    for obra in lista_obras:
        if obra["titulo"].lower() == titulo.lower() and titulo.lower() != titulo_actual.lower():
            return True

    return False


def validar_codigo_obra(texto):
    # Formato: las letras OBR seguidas de al menos 3 dígitos. Ejemplo: OBR001.
    if len(texto) < 6:
        return False

    if texto[:3] != "OBR":
        return False

    return solo_digitos(texto[3:])


def generar_codigo_obra(lista_obras):
    # El código nuevo es el número más alto que ya existe, más uno.
    mayor = 0
    for obra in lista_obras:
        codigo = obra.get("codigo", "")
        if validar_codigo_obra(codigo) and int(codigo[3:]) > mayor:
            mayor = int(codigo[3:])

    return "OBR" + str(mayor + 1).zfill(3)


# ==================== ENTRADA DE DATOS ====================

def pedir_numero_en_rango(texto_pedido, minimo, maximo, max_digitos):
    # Pide un número entero y devuelve el texto, o "regresar_uno" si escribe 0.
    while True:
        dato = input(texto_pedido + " (0 para cancelar): ").strip()

        if dato == "0":
            return "regresar_uno"

        if solo_digitos(dato) and len(dato) <= max_digitos and int(dato) >= minimo and int(dato) <= maximo:
            return dato

        print("Error: escriba un número entero del " + str(minimo) + " al " + str(maximo) + ".")


def pedir_fecha(etiqueta, fecha_minima, fecha_maxima):
    # Un dato válido se devuelve como [fecha]; una cancelación, como señal.
    while True:
        print(etiqueta + " (día/mes/año)")

        dia = pedir_numero_en_rango("Día", 1, 31, 2)
        if dia == "regresar_uno":
            return "regresar_uno"

        mes = pedir_numero_en_rango("Mes", 1, 12, 2)
        if mes == "regresar_uno":
            return "regresar_uno"

        anio = pedir_numero_en_rango("Año", anio_minimo, anio_maximo, 4)
        if anio == "regresar_uno":
            return "regresar_uno"

        # Comprobar que el día exista en ese mes.
        if int(dia) > dias_del_mes(int(mes)):
            print("Error: esa fecha no existe. El mes " + mes + " tiene como máximo " + str(dias_del_mes(int(mes))) + " días.")
        else:
            fecha = dia.zfill(2) + "/" + mes.zfill(2) + "/" + anio
            fecha_valida = True

            if fecha_minima != "" and fecha_a_tupla(fecha) < fecha_a_tupla(fecha_minima):
                print("Error: la fecha de finalización no puede ser anterior a la de inicio (" + fecha_minima + ").")
                fecha_valida = False

            if fecha_maxima != "" and fecha_a_tupla(fecha) > fecha_a_tupla(fecha_maxima):
                print("Error: la fecha de inicio no puede ser posterior a la de finalización (" + fecha_maxima + ").")
                fecha_valida = False

            if fecha_valida:
                return [fecha]


def pedir_dato_obra(campo, lista_obras, titulo_actual, obra_ref):
    # Usar la misma pantalla de entrada al registrar y al actualizar.
    # Un dato válido se devuelve como [dato]; una cancelación, como señal.
    # obra_ref guarda los datos ya conocidos para comparar las fechas.

    if campo == "fecha_inicio":
        return pedir_fecha(etiquetas_obras[campo], "", obra_ref.get("fecha_fin", ""))

    if campo == "fecha_fin":
        return pedir_fecha(etiquetas_obras[campo], obra_ref.get("fecha_inicio", ""), "")

    while True:
        dato = input(etiquetas_obras[campo] + " (0 para cancelar): ").strip()

        # El cero devuelve el control a la pantalla que pidió el dato.
        if dato == "0":
            return "regresar_uno"

        if campo == "titulo":
            if not validar_titulo_obra(dato):
                print("Error: el título no puede estar vacío; debe empezar con una letra mayúscula y contener solo letras, números, espacios o los caracteres especiales permitidos.")
            elif titulo_repetido(lista_obras, dato, titulo_actual):
                print("Error: ya existe una obra con ese título.")
            else:
                return [dato]

        elif campo == "cliente_nombre" or campo == "cliente_apellido" or campo == "gerente_nombre" or campo == "gerente_apellido":
            if not validar_nombre_persona(dato):
                print("Error: " + etiquetas_obras[campo] + " no puede estar vacío; debe empezar con una letra mayúscula y contener solo letras, espacios o guiones.")
            else:
                return [dato]

        elif campo == "zona":
            if not validar_zona(dato):
                print("Error: la zona debe ser un número entero del 1 al " + str(zona_maxima) + ".")
            else:
                return [str(int(dato))]

        elif campo == "direccion" or campo == "colonia":
            if not validar_direccion(dato):
                print("Error: " + etiquetas_obras[campo] + " no puede estar vacío y solo admite letras, números, espacios o los caracteres especiales permitidos.")
            else:
                return [dato]

        elif campo == "presupuesto":
            if not validar_monto(dato):
                print("Error: escriba un número mayor que cero, sin comas ni símbolos, con hasta 2 decimales. Ejemplo: 150000.50")
            else:
                # Guardar siempre con dos decimales.
                return [format(float(dato), ".2f")]

        elif campo == "descripcion":
            if dato == "":
                print("Error: la descripción no puede estar vacía.")
            else:
                return [dato]

        else:
            # Información adicional admite cualquier texto o Enter.
            return [dato]


# ==================== REGISTRAR ====================

def registrar_obra(lista_obras):
    print("Título de obra: debe empezar con una letra mayúscula, no puede repetirse y admite letras, números, espacios y estos caracteres especiales:")
    print(". , : ; ? ! @ # _ - $ % & * = ( ) [ ] { } /")
    print("Cliente y Gerente de obra: nombre y apellido deben empezar con una letra mayúscula y contener solo letras, espacios o guiones.")
    print("Zona: número entero del 1 al " + str(zona_maxima) + ".")
    print("Fechas: se piden por separado día, mes y año. La finalización no puede ser anterior al inicio.")
    print("Presupuesto inicial: en quetzales, mayor que cero, sin comas. Ejemplo: 150000.50")
    print("El campo Información adicional es opcional: si no desea escribir nada, solo presione Enter.")
    print("En cualquier momento escriba 0 para cancelar el registro y volver al menú de Obras.")

    # El código se genera solo; no se pide al usuario.
    obra_nueva = {"codigo": generar_codigo_obra(lista_obras)}
    indice = 0

    # Pedir los campos en orden, conservando los que ya fueron válidos.
    while indice < len(campos_obra):
        campo = campos_obra[indice]
        resultado = pedir_dato_obra(campo, lista_obras, "", obra_nueva)

        # Estas señales deben subir sin mostrar otra pantalla intermedia.
        if resultado == "menu_principal" or resultado == "finalizar_sesion":
            return resultado

        if resultado == "regresar_uno":
            print("Registro cancelado. No se guardó ninguna obra.")
            return "regresar_uno"

        obra_nueva[campo] = resultado[0]
        indice = indice + 1

    # Agregar únicamente cuando todos los campos estén completos.
    lista_obras.append(obra_nueva)
    # Guardar inmediatamente la lista completa en el archivo JSON.
    guardar_obras(lista_obras)
    print("Obra registrada correctamente")
    print("Código de la obra: " + obra_nueva["codigo"])
    print("Guarde este código: lo necesitará para buscar la obra.")
    return "regresar_uno"


# ==================== VER ====================

def ver_detalle_obra(obra):
    while True:
        print("Código de obra: " + obra["codigo"])
        print("Título de obra: " + obra["titulo"])
        print("Descripción: " + obra["descripcion"])
        print("Cliente: " + obra["cliente_nombre"] + " " + obra["cliente_apellido"])
        print("Zona: " + obra["zona"])
        print("Dirección: " + obra["direccion"])
        print("Colonia: " + obra["colonia"])

        if obra["informacion"] == "":
            print("Información adicional: Sin información adicional")
        else:
            print("Información adicional: " + obra["informacion"])

        print("Fecha de inicio estimada: " + obra["fecha_inicio"])
        print("Fecha de finalización estimada: " + obra["fecha_fin"])
        print("Presupuesto inicial: " + formatear_monto(obra["presupuesto"]))
        print("Gerente de obra: " + obra["gerente_nombre"] + " " + obra["gerente_apellido"])

        print("1. Regresar uno")
        print("2. Regresar al menú principal")
        print("3. Finalizar sesión")
        opcion = input("Elija un número: ").strip()

        if opcion == "1":
            return "regresar_uno"
        elif opcion == "2":
            return "menu_principal"
        elif opcion == "3":
            return "finalizar_sesion"
        else:
            print("Opción inválida. Elija un número del 1 al 3.")


# ==================== LISTA DE OBRAS (VER Y ACTUALIZAR) ====================

def listar_obras(lista_obras, indices, modo):
    # indices: posiciones en lista_obras de las obras que se muestran.
    # modo: "ver" abre el detalle y "editar" abre el menú de actualizar.
    while True:
        if len(indices) == 0:
            print("No hay obras registradas")
            return "regresar_uno"

        for numero in range(len(indices)):
            obra = lista_obras[indices[numero]]
            print(str(numero + 1) + ". " + obra["codigo"] + " - " + obra["titulo"] + " (" + obra["cliente_nombre"] + " " + obra["cliente_apellido"] + ")")

        numero_regresar = len(indices) + 1
        numero_menu = len(indices) + 2
        numero_finalizar = len(indices) + 3
        print(str(numero_regresar) + ". Regresar uno")
        print(str(numero_menu) + ". Regresar al menú principal")
        print(str(numero_finalizar) + ". Finalizar sesión")
        opcion = input("Elija un número: ").strip()

        if opcion == str(numero_regresar):
            return "regresar_uno"
        elif opcion == str(numero_menu):
            return "menu_principal"
        elif opcion == str(numero_finalizar):
            return "finalizar_sesion"
        else:
            opcion_valida = False
            # Buscar por comparación de textos, sin convertir a int().
            for numero in range(len(indices)):
                if opcion == str(numero + 1):
                    opcion_valida = True

                    if modo == "ver":
                        resultado = ver_detalle_obra(lista_obras[indices[numero]])
                    else:
                        resultado = editar_obra(lista_obras, indices[numero])

                    if resultado == "menu_principal" or resultado == "finalizar_sesion":
                        return resultado
                    # regresar_uno repite esta lista, la pantalla anterior.

            if not opcion_valida:
                print("Opción inválida. Elija un número del 1 al " + str(numero_finalizar) + ".")


# ==================== BUSCAR ====================

def buscar_obras(lista_obras):
    while True:
        if len(lista_obras) == 0:
            print("No hay obras registradas")
            return "regresar_uno"

        # Se acepta también en minúscula: se convierte a mayúscula.
        codigo = input("Código de obra (0 para cancelar): ").strip().upper()

        # El cero regresa al menú de Obras.
        if codigo == "0":
            return "regresar_uno"

        if not validar_codigo_obra(codigo):
            print("Error: el código debe empezar con OBR seguido de números, sin espacios. Ejemplo: OBR001.")
        else:
            obra_encontrada = None
            for obra in lista_obras:
                if obra["codigo"] == codigo:
                    obra_encontrada = obra

            if obra_encontrada is None:
                print("No se encontró ninguna obra con el código " + codigo)
            else:
                resultado = ver_detalle_obra(obra_encontrada)
                if resultado == "menu_principal" or resultado == "finalizar_sesion":
                    return resultado
                # regresar_uno repite la pantalla para escribir otro código.


# ==================== ACTUALIZAR ====================

def valor_actual_obra(obra, campos):
    # Texto que se muestra como "Dato actual" para una o dos columnas.
    if campos[0] == "presupuesto":
        return formatear_monto(obra["presupuesto"])

    if campos[0] == "informacion" and obra["informacion"] == "":
        return "Sin información adicional"

    texto = obra[campos[0]]
    if len(campos) == 2:
        texto = texto + " " + obra[campos[1]]

    return texto


def preguntar_otra_edicion_obra():
    while True:
        print("¿Desea editar otro valor?")
        print("1. Sí")
        print("2. No")
        opcion = input("Elija un número: ").strip()

        if opcion == "1" or opcion == "2":
            return opcion

        print("Opción inválida. Elija 1 o 2.")


def editar_obra(lista_obras, indice_obra):
    # Este diccionario pertenece a la lista: cambiarlo actualiza la lista.
    obra = lista_obras[indice_obra]
    total = len(opciones_edicion_obra)

    while True:
        print("Indique el dato que desea modificar")
        for numero in range(total):
            print(str(numero + 1) + ". " + nombres_opciones_edicion_obra[numero])
        print(str(total + 1) + ". Regresar uno")
        print(str(total + 2) + ". Regresar al menú principal")
        print(str(total + 3) + ". Finalizar sesión")
        opcion = input("Elija un número: ").strip()

        if opcion == str(total + 1):
            return "regresar_uno"
        elif opcion == str(total + 2):
            return "menu_principal"
        elif opcion == str(total + 3):
            return "finalizar_sesion"
        else:
            campos = []
            for numero in range(total):
                if opcion == str(numero + 1):
                    campos = opciones_edicion_obra[numero]

            if len(campos) == 0:
                print("Opción inválida. Elija un número del 1 al " + str(total + 3) + ".")
            else:
                print("Dato actual: " + valor_actual_obra(obra, campos))

                # Reunir los datos nuevos; si se cancela alguno, no se cambia nada.
                datos_nuevos = {}
                cancelado = False

                for campo in campos:
                    if not cancelado:
                        resultado = pedir_dato_obra(campo, lista_obras, obra["titulo"], obra)

                        if resultado == "menu_principal" or resultado == "finalizar_sesion":
                            return resultado

                        if resultado == "regresar_uno":
                            cancelado = True
                        else:
                            datos_nuevos[campo] = resultado[0]

                # Si se canceló con 0, el ciclo repite este menú de datos.
                if not cancelado:
                    for campo in datos_nuevos:
                        obra[campo] = datos_nuevos[campo]

                    # Guardar el cambio antes de preguntar si desea otro.
                    guardar_obras(lista_obras)
                    print("Dato actualizado correctamente")

                    respuesta = preguntar_otra_edicion_obra()
                    if respuesta == "2":
                        # Volver a la lista de obras, un nivel arriba.
                        return "regresar_uno"
                    # Con Sí, el ciclo repite el menú de esta obra.


def actualizar_obras(lista_obras):
    todas = []
    for posicion in range(len(lista_obras)):
        todas.append(posicion)

    return listar_obras(lista_obras, todas, "editar")


# ==================== MENÚ DE OBRAS ====================

def modulo_obras():
    # Leer el archivo una sola vez al entrar al módulo.
    lista_obras = cargar_obras()

    while True:
        print("Módulo de Obras")
        print()
        print("1. Registrar obra")
        print("2. Buscar obra")
        print("3. Actualizar obra")
        print("4. Regresar uno")
        print("5. Regresar al menú principal")
        print("6. Finalizar sesión")
        opcion = input("Elija un número: ").strip()
        resultado = ""

        if opcion == "1":
            resultado = registrar_obra(lista_obras)
        elif opcion == "2":
            resultado = buscar_obras(lista_obras)
        elif opcion == "3":
            resultado = actualizar_obras(lista_obras)
        elif opcion == "4":
            # Regresar solo un nivel: al menú que abrió este módulo.
            return "regresar_uno"
        elif opcion == "5":
            # Esta señal siempre debe llegar al menú principal.
            return "menu_principal"
        elif opcion == "6":
            return "finalizar_sesion"
        else:
            print("Opción inválida. Elija un número del 1 al 6.")

        # Propagar estas decisiones sin volver a mostrar este menú.
        if resultado == "menu_principal" or resultado == "finalizar_sesion":
            return resultado
        # Con regresar_uno, el ciclo vuelve al menú de Obras.


# ==================== MÓDULO DE MATERIALES ====================

# Lista que se puede ampliar más adelante.
categorias_materiales = [
    "Cemento y concreto", "Acero y hierro", "Madera", "Bloques y ladrillos",
    "Plomería", "Electricidad", "Pintura y acabados", "Otros"
]

# Orden en que se piden los datos al registrar un material.
campos_material = ["codigo", "nombre", "categoria", "cantidad", "costo", "fecha_entrega", "lugar_entrega"]

etiquetas_materiales = {
    "codigo": "Código",
    "nombre": "Nombre",
    "categoria": "Categoría",
    "cantidad": "Cantidad",
    "costo": "Costo por unidad en quetzales",
    "fecha_entrega": "Fecha de entrega",
    "lugar_entrega": "Lugar de entrega",
    "cantidad_transferir": "Cantidad a transferir",
    "lugar_nuevo": "Lugar de destino"
}


# ==================== ALMACENAMIENTO ====================

def cargar_materiales():
    # Comprobar si existe el archivo en la carpeta de trabajo.
    if not os.path.exists("materiales.json"):
        return []

    # Comprobar si el archivo tiene cero bytes, es decir, está vacío.
    if os.path.getsize("materiales.json") == 0:
        return []

    # Abrir el archivo para leer texto en UTF-8.
    archivo = open("materiales.json", "r", encoding="utf-8")
    # Leer todo el contenido del archivo como texto.
    contenido = archivo.read()
    # Cerrar el archivo después de leerlo.
    archivo.close()

    # Considerar vacío también un archivo que solo contiene espacios.
    if contenido.strip() == "":
        return []

    # Convertir el texto JSON en una lista de diccionarios de Python.
    lista_materiales = json.loads(contenido)
    return lista_materiales


def guardar_materiales(lista_materiales):
    # Abrir para escribir: crea el archivo o reemplaza su contenido.
    archivo = open("materiales.json", "w", encoding="utf-8")
    # Guardar la lista completa como JSON, con sangría y tildes legibles.
    json.dump(lista_materiales, archivo, indent=4, ensure_ascii=False)
    # Cerrar el archivo para completar la escritura.
    archivo.close()


# ==================== ENTRADA DE DATOS ====================

def pedir_dato_material(campo, lista_materiales, material_ref):
    # Usar la misma pantalla de entrada al registrar y al transferir.
    # Un dato válido se devuelve como [dato]; una cancelación, como señal.
    # material_ref es el material que se transfiere (vacío al registrar).

    if campo == "fecha_entrega":
        return pedir_fecha(etiquetas_materiales[campo], "", "")

    while True:
        if campo == "categoria":
            for indice in range(len(categorias_materiales)):
                print(str(indice + 1) + ". " + categorias_materiales[indice])

        dato = input(etiquetas_materiales[campo] + " (0 para cancelar): ").strip()

        # El cero devuelve el control a la pantalla que pidió el dato.
        if dato == "0":
            return "regresar_uno"

        if campo == "codigo":
            if not validar_codigo(dato):
                print("Error: el código debe tener 3 letras MAYÚSCULAS de A a Z seguidas de 3 dígitos de 0 a 9, sin espacios. Ejemplo: MAT001.")
            else:
                codigo_repetido = False
                for material in lista_materiales:
                    if material["codigo"] == dato:
                        codigo_repetido = True

                if codigo_repetido:
                    print("Error: el código ya está registrado en otro material.")
                else:
                    return [dato]

        elif campo == "nombre":
            if not validar_nombre(dato):
                print("Error: el nombre no puede estar vacío; debe empezar con una letra mayúscula y contener solo letras, números, espacios o los caracteres especiales permitidos.")
            else:
                return [dato]

        elif campo == "categoria":
            # Comparar textos evita convertir entradas extrañas con int().
            for indice in range(len(categorias_materiales)):
                if dato == str(indice + 1):
                    return [categorias_materiales[indice]]
            print("Error: elija un número del 1 al " + str(len(categorias_materiales)) + " para la categoría.")

        elif campo == "cantidad":
            if not solo_digitos(dato) or int(dato) < 1:
                print("Error: la cantidad debe ser un número entero mayor que cero.")
            else:
                return [str(int(dato))]

        elif campo == "cantidad_transferir":
            if not solo_digitos(dato) or int(dato) < 1 or int(dato) > int(material_ref["cantidad"]):
                print("Error: escriba un número entero del 1 al " + material_ref["cantidad"] + ".")
            else:
                return [str(int(dato))]

        elif campo == "costo":
            if not validar_monto(dato):
                print("Error: escriba un número mayor que cero, sin comas ni símbolos, con hasta 2 decimales. Ejemplo: 25.50")
            else:
                # Guardar siempre con dos decimales.
                return [format(float(dato), ".2f")]

        else:
            # Lugar de entrega y lugar de destino.
            if not validar_direccion(dato):
                print("Error: el lugar no puede estar vacío y solo admite letras, números, espacios o los caracteres especiales permitidos.")
            elif campo == "lugar_nuevo" and dato.lower() == material_ref["lugar_entrega"].lower():
                print("Error: el lugar de destino debe ser distinto al lugar actual.")
            else:
                return [dato]


# ==================== REGISTRAR ====================

def registrar_material(lista_materiales):
    print("Código: 3 letras MAYÚSCULAS de A a Z y 3 dígitos de 0 a 9, sin repetirse. Ejemplo: MAT001.")
    print("Nombre: debe empezar con una letra mayúscula y no quedar vacío.")
    print("Se admiten letras, números, espacios y estos caracteres especiales:")
    print(". , : ; ? ! @ # _ - $ % & * = ( ) [ ] { } /")
    print("Categoría: elija una de las opciones numeradas.")
    print("Cantidad: número entero mayor que cero.")
    print("Costo: por unidad, en quetzales, mayor que cero y sin comas. Ejemplo: 25.50")
    print("Fecha de entrega: se piden por separado día, mes y año.")
    print("En cualquier momento escriba 0 para cancelar el registro y volver al menú de Materiales.")

    material_nuevo = {}
    indice = 0

    # Pedir los campos en orden, conservando los que ya fueron válidos.
    while indice < len(campos_material):
        campo = campos_material[indice]
        resultado = pedir_dato_material(campo, lista_materiales, {})

        if resultado == "regresar_uno":
            print("Registro cancelado. No se guardó ningún material.")
            return "regresar_uno"

        material_nuevo[campo] = resultado[0]
        indice = indice + 1

    # Agregar únicamente cuando todos los campos estén completos.
    lista_materiales.append(material_nuevo)
    # Guardar inmediatamente la lista completa en el archivo JSON.
    guardar_materiales(lista_materiales)
    print("Material registrado correctamente")
    return "regresar_uno"


# ==================== TRANSFERENCIA ====================

def transferir_material(lista_materiales, indice_material):
    # Este diccionario pertenece a la lista: cambiarlo actualiza la lista.
    material = lista_materiales[indice_material]
    print("Material: " + material["nombre"] + " (" + material["codigo"] + ")")
    print("Cantidad disponible: " + material["cantidad"])
    print("Lugar actual: " + material["lugar_entrega"])

    # Reunir todos los datos antes de cambiar nada: si se cancela, no se modifica el material.
    datos = {}
    for campo in ["cantidad_transferir", "lugar_nuevo", "codigo"]:
        # El código solo se pide si se transfiere una parte de la cantidad.
        if campo != "codigo" or datos["cantidad_transferir"] != material["cantidad"]:
            if campo == "codigo":
                print("Se transfiere solo una parte: el material transferido se registrará con un código nuevo.")

            resultado = pedir_dato_material(campo, lista_materiales, material)

            if resultado == "regresar_uno":
                print("Transferencia cancelada. No se modificó ningún material.")
                return "regresar_uno"

            datos[campo] = resultado[0]

    if datos["cantidad_transferir"] == material["cantidad"]:
        # Se transfiere todo: el material cambia de lugar.
        material["lugar_entrega"] = datos["lugar_nuevo"]
    else:
        # Se transfiere una parte: queda el resto en el lugar actual y se crea un registro nuevo.
        material_nuevo = {
            "codigo": datos["codigo"],
            "nombre": material["nombre"],
            "categoria": material["categoria"],
            "cantidad": datos["cantidad_transferir"],
            "costo": material["costo"],
            "fecha_entrega": material["fecha_entrega"],
            "lugar_entrega": datos["lugar_nuevo"]
        }
        material["cantidad"] = str(int(material["cantidad"]) - int(datos["cantidad_transferir"]))
        lista_materiales.append(material_nuevo)

    # Guardar el cambio en el archivo JSON.
    guardar_materiales(lista_materiales)
    print("Transferencia realizada correctamente")
    return "regresar_uno"


# ==================== BUSCAR ====================

def ver_detalle_material(material):
    while True:
        print("Código: " + material["codigo"])
        print("Nombre: " + material["nombre"])
        print("Categoría: " + material["categoria"])
        print("Cantidad: " + material["cantidad"])
        print("Costo por unidad: " + formatear_monto(material["costo"]))
        print("Fecha de entrega: " + material["fecha_entrega"])
        print("Lugar de entrega: " + material["lugar_entrega"])

        print("1. Regresar uno")
        print("2. Regresar al menú principal")
        print("3. Finalizar sesión")
        opcion = input("Elija un número: ").strip()

        if opcion == "1":
            return "regresar_uno"
        elif opcion == "2":
            return "menu_principal"
        elif opcion == "3":
            return "finalizar_sesion"
        else:
            print("Opción inválida. Elija un número del 1 al 3.")


def listar_materiales(lista_materiales, modo):
    # modo: "ver" abre el detalle y "transferir" inicia la transferencia.
    while True:
        if len(lista_materiales) == 0:
            print("No hay materiales registrados")
            return "regresar_uno"

        for indice in range(len(lista_materiales)):
            material = lista_materiales[indice]
            print(str(indice + 1) + ". " + material["nombre"] + " (" + material["codigo"] + ")")

        numero_regresar = len(lista_materiales) + 1
        numero_menu = len(lista_materiales) + 2
        numero_finalizar = len(lista_materiales) + 3
        print(str(numero_regresar) + ". Regresar uno")
        print(str(numero_menu) + ". Regresar al menú principal")
        print(str(numero_finalizar) + ". Finalizar sesión")
        opcion = input("Elija un número: ").strip()

        if opcion == str(numero_regresar):
            return "regresar_uno"
        elif opcion == str(numero_menu):
            return "menu_principal"
        elif opcion == str(numero_finalizar):
            return "finalizar_sesion"
        else:
            opcion_valida = False
            # Buscar por comparación de textos, sin convertir a int().
            for indice in range(len(lista_materiales)):
                if opcion == str(indice + 1):
                    opcion_valida = True

                    if modo == "ver":
                        resultado = ver_detalle_material(lista_materiales[indice])
                    else:
                        resultado = transferir_material(lista_materiales, indice)

                    if resultado == "menu_principal" or resultado == "finalizar_sesion":
                        return resultado
                    # regresar_uno repite esta lista, la pantalla anterior.

            if not opcion_valida:
                print("Opción inválida. Elija un número del 1 al " + str(numero_finalizar) + ".")


# ==================== MENÚ DE MATERIALES ====================

def modulo_materiales():
    # Leer el archivo una sola vez al entrar al módulo.
    lista_materiales = cargar_materiales()

    while True:
        print("Módulo de Materiales")
        print()
        print("1. Registrar material")
        print("2. Transferencia de material")
        print("3. Buscar materiales")
        print("4. Regresar uno")
        print("5. Regresar al menú principal")
        print("6. Finalizar sesión")
        opcion = input("Elija un número: ").strip()
        resultado = ""

        if opcion == "1":
            resultado = registrar_material(lista_materiales)
        elif opcion == "2":
            resultado = listar_materiales(lista_materiales, "transferir")
        elif opcion == "3":
            resultado = listar_materiales(lista_materiales, "ver")
        elif opcion == "4":
            # Regresar solo un nivel: al menú que abrió este módulo.
            return "regresar_uno"
        elif opcion == "5":
            # Esta señal siempre debe llegar al menú principal.
            return "menu_principal"
        elif opcion == "6":
            return "finalizar_sesion"
        else:
            print("Opción inválida. Elija un número del 1 al 6.")

        # Propagar estas decisiones sin volver a mostrar este menú.
        if resultado == "menu_principal" or resultado == "finalizar_sesion":
            return resultado
        # Con regresar_uno, el ciclo vuelve al menú de Materiales.


# Listas que se pueden ampliar más adelante.
caracteres_especiales_herramientas = [
    ".", ",", ":", ";", "?", "!", "@", "#", "_", "-", "$", "%", "&", "*",
    "=", "(", ")", "[", "]", "{", "}"
]
estados_herramientas = ["Bueno", "Regular", "Malo", "En mantenimiento"]


# ==================== ALMACENAMIENTO ====================

def cargar_herramientas():
    # Comprobar si existe el archivo en la carpeta de trabajo.
    if not os.path.exists("herramientas.json"):
        return []

    # Comprobar si el archivo tiene cero bytes, es decir, está vacío.
    if os.path.getsize("herramientas.json") == 0:
        return []

    # Abrir el archivo para leer texto en UTF-8.
    archivo = open("herramientas.json", "r", encoding="utf-8")
    # Leer todo el contenido del archivo como texto.
    contenido = archivo.read()
    # Cerrar el archivo después de leerlo.
    archivo.close()

    # Considerar vacío también un archivo que solo contiene espacios.
    if contenido.strip() == "":
        return []

    # Convertir el texto JSON en una lista de diccionarios de Python.
    lista_herramientas = json.loads(contenido)
    return lista_herramientas


def guardar_herramientas(lista_herramientas):
    # Abrir para escribir: crea el archivo o reemplaza su contenido.
    archivo = open("herramientas.json", "w", encoding="utf-8")
    # Guardar la lista completa como JSON, con sangría y tildes legibles.
    json.dump(lista_herramientas, archivo, indent=4, ensure_ascii=False)
    # Cerrar el archivo para completar la escritura.
    archivo.close()


# ==================== VALIDACIONES ====================

def validar_nombre(texto):
    # El campo no puede estar vacío.
    if texto == "":
        return False

    # El primer carácter debe ser una letra mayúscula.
    if not texto[0].isalpha() or not texto[0].isupper():
        return False

    # Admitir letras, números, espacios y los especiales permitidos.
    for caracter in texto:
        if not caracter.isalpha() and not caracter.isdigit() and caracter != " " and caracter not in caracteres_especiales_herramientas:
            return False

    return True


def validar_codigo(texto):
    # El código debe tener exactamente seis caracteres.
    if len(texto) != 6:
        return False

    # Las tres primeras posiciones solo admiten letras de A a Z.
    for caracter in texto[:3]:
        if caracter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return False

    # Las tres últimas posiciones solo admiten dígitos de 0 a 9.
    for caracter in texto[3:]:
        if caracter not in "0123456789":
            return False

    return True


def validar_marca(texto):
    # Por ahora igual que el nombre; se cambiará más adelante
    return validar_nombre(texto)


def validar_ubicacion(texto):
    # Por ahora igual que el nombre; se cambiará más adelante
    return validar_nombre(texto)


def pedir_dato_herramienta(campo, lista_herramientas, codigo_actual):
    # Usar la misma pantalla de entrada al registrar y al actualizar.
    # Un dato válido se devuelve como [dato]; una cancelación, como señal.
    # Así, escribir menu_principal en un campo no provoca navegación.
    etiquetas = {
        "nombre": "Nombre",
        "codigo": "Código",
        "marca": "Marca",
        "ubicacion": "Ubicación",
        "estado": "Estado",
        "descripcion": "Descripción",
        "comentarios": "Comentarios"
    }

    while True:
        if campo == "estado":
            for indice in range(len(estados_herramientas)):
                print(str(indice + 1) + ". " + estados_herramientas[indice])

        dato = input(etiquetas[campo] + " (0 para cancelar): ").strip()

        # El cero devuelve el control a la pantalla que pidió el dato.
        if dato == "0":
            return "regresar_uno"

        if campo == "nombre" or campo == "marca" or campo == "ubicacion":
            if campo == "nombre":
                dato_valido = validar_nombre(dato)
            elif campo == "marca":
                dato_valido = validar_marca(dato)
            else:
                dato_valido = validar_ubicacion(dato)

            if not dato_valido:
                print("Error: " + etiquetas[campo] + " no puede estar vacío; debe empezar con una letra mayúscula y contener solo letras, números, espacios o los caracteres especiales permitidos.")
            else:
                return [dato]

        elif campo == "codigo":
            if not validar_codigo(dato):
                print("Error: el código debe tener 3 letras MAYÚSCULAS de A a Z seguidas de 3 dígitos de 0 a 9, sin espacios. Ejemplo: TAL001.")
            else:
                codigo_repetido = False
                for herramienta in lista_herramientas:
                    if herramienta["codigo"] == dato and dato != codigo_actual:
                        codigo_repetido = True

                if codigo_repetido:
                    print("Error: el código ya está registrado en otra herramienta.")
                else:
                    return [dato]

        elif campo == "estado":
            # Comparar textos evita convertir entradas extrañas con int().
            for indice in range(len(estados_herramientas)):
                if dato == str(indice + 1):
                    return [estados_herramientas[indice]]
            print("Error: elija un número del 1 al " + str(len(estados_herramientas)) + " para el estado.")

        else:
            # Descripción y Comentarios admiten cualquier texto o Enter.
            return [dato]


# ==================== REGISTRAR ====================

def registrar_herramientas(lista_herramientas):
    print("Nombre, Marca y Ubicación: deben empezar con una letra mayúscula y no quedar vacíos.")
    print("Se admiten letras, números, espacios y estos caracteres especiales:")
    print(". , : ; ? ! @ # _ - $ % & * = ( ) [ ] { }")
    print("Código: 3 letras MAYÚSCULAS de A a Z y 3 dígitos de 0 a 9, sin repetirse. Ejemplo: TAL001.")
    print("Estado: elija una de las opciones numeradas.")
    print("Los campos Descripción y Comentarios son opcionales: si no desea escribir nada, solo presione Enter.")
    print("En cualquier momento escriba 0 para cancelar el registro y volver al menú de Herramientas.")

    campos = ["nombre", "codigo", "marca", "ubicacion", "estado", "descripcion", "comentarios"]
    herramienta_nueva = {}
    indice = 0

    # Pedir los campos en orden, conservando los que ya fueron válidos.
    while indice < len(campos):
        campo = campos[indice]
        resultado = pedir_dato_herramienta(campo, lista_herramientas, "")

        # Estas señales deben subir sin mostrar otra pantalla intermedia.
        if resultado == "menu_principal" or resultado == "finalizar_sesion":
            return resultado

        if resultado == "regresar_uno":
            print("Registro cancelado. No se guardó ninguna herramienta.")
            return "regresar_uno"

        herramienta_nueva[campo] = resultado[0]
        indice = indice + 1

    # Agregar únicamente cuando todos los campos estén completos.
    lista_herramientas.append(herramienta_nueva)
    # Guardar inmediatamente la lista completa en el archivo JSON.
    guardar_herramientas(lista_herramientas)
    print("Herramienta registrada correctamente")
    return "regresar_uno"


# ==================== ACTUALIZAR ====================

def preguntar_otra_edicion():
    while True:
        print("¿Desea editar otro valor?")
        print("1. Sí")
        print("2. No")
        opcion = input("Elija un número: ").strip()

        if opcion == "1" or opcion == "2":
            return opcion

        print("Opción inválida. Elija 1 o 2.")


def editar_herramienta(lista_herramientas, indice_herramienta):
    # Este diccionario pertenece a la lista: cambiarlo actualiza la lista.
    herramienta = lista_herramientas[indice_herramienta]
    campos = ["nombre", "codigo", "marca", "ubicacion", "estado", "descripcion", "comentarios"]

    while True:
        print("Indique el dato que desea modificar")
        print("1. Nombre")
        print("2. Código")
        print("3. Marca")
        print("4. Ubicación")
        print("5. Estado")
        print("6. Descripción")
        print("7. Comentarios")
        print("8. Regresar uno")
        print("9. Regresar al menú principal")
        print("10. Finalizar sesión")
        opcion = input("Elija un número: ").strip()

        if opcion == "8":
            return "regresar_uno"
        elif opcion == "9":
            return "menu_principal"
        elif opcion == "10":
            return "finalizar_sesion"
        else:
            campo = ""
            for indice in range(len(campos)):
                if opcion == str(indice + 1):
                    campo = campos[indice]

            if campo == "":
                print("Opción inválida. Elija un número del 1 al 10.")
            else:
                valor_actual = herramienta[campo]
                if campo == "descripcion" and valor_actual == "":
                    valor_actual = "Sin descripción"
                elif campo == "comentarios" and valor_actual == "":
                    valor_actual = "Sin comentarios"
                print("Dato actual: " + valor_actual)

                resultado = pedir_dato_herramienta(campo, lista_herramientas, herramienta["codigo"])

                if resultado == "menu_principal" or resultado == "finalizar_sesion":
                    return resultado

                # Si se canceló con 0, el ciclo repite este menú de datos.
                if resultado != "regresar_uno":
                    herramienta[campo] = resultado[0]
                    # Guardar el cambio antes de preguntar si desea otro.
                    guardar_herramientas(lista_herramientas)
                    print("Dato actualizado correctamente")

                    respuesta = preguntar_otra_edicion()
                    if respuesta == "2":
                        # Volver a la lista de herramientas, un nivel arriba.
                        return "regresar_uno"
                    # Con Sí, el ciclo repite el menú de esta herramienta.


def actualizar_herramientas(lista_herramientas):
    while True:
        if len(lista_herramientas) == 0:
            print("No hay herramientas registradas")
            return "regresar_uno"

        for indice in range(len(lista_herramientas)):
            herramienta = lista_herramientas[indice]
            print(str(indice + 1) + ". " + herramienta["nombre"] + " (" + herramienta["codigo"] + ")")

        numero_regresar = len(lista_herramientas) + 1
        numero_menu = len(lista_herramientas) + 2
        numero_finalizar = len(lista_herramientas) + 3
        print(str(numero_regresar) + ". Regresar uno")
        print(str(numero_menu) + ". Regresar al menú principal")
        print(str(numero_finalizar) + ". Finalizar sesión")
        opcion = input("Elija un número: ").strip()

        if opcion == str(numero_regresar):
            return "regresar_uno"
        elif opcion == str(numero_menu):
            return "menu_principal"
        elif opcion == str(numero_finalizar):
            return "finalizar_sesion"
        else:
            opcion_valida = False
            # Buscar por comparación de textos, sin convertir a int().
            for indice in range(len(lista_herramientas)):
                if opcion == str(indice + 1):
                    opcion_valida = True
                    resultado = editar_herramienta(lista_herramientas, indice)
                    if resultado == "menu_principal" or resultado == "finalizar_sesion":
                        return resultado
                    # regresar_uno repite esta lista, la pantalla anterior.

            if not opcion_valida:
                print("Opción inválida. Elija un número del 1 al " + str(numero_finalizar) + ".")


# ==================== VER ====================

def ver_detalle_herramienta(herramienta):
    while True:
        print("Nombre: " + herramienta["nombre"])
        print("Código: " + herramienta["codigo"])
        print("Marca: " + herramienta["marca"])
        print("Ubicación: " + herramienta["ubicacion"])
        print("Estado: " + herramienta["estado"])

        if herramienta["descripcion"] == "":
            print("Descripción: Sin descripción")
        else:
            print("Descripción: " + herramienta["descripcion"])

        if herramienta["comentarios"] == "":
            print("Comentarios: Sin comentarios")
        else:
            print("Comentarios: " + herramienta["comentarios"])

        print("1. Regresar uno")
        print("2. Regresar al menú principal")
        print("3. Finalizar sesión")
        opcion = input("Elija un número: ").strip()

        if opcion == "1":
            return "regresar_uno"
        elif opcion == "2":
            return "menu_principal"
        elif opcion == "3":
            return "finalizar_sesion"
        else:
            print("Opción inválida. Elija un número del 1 al 3.")


def ver_herramientas(lista_herramientas):
    while True:
        if len(lista_herramientas) == 0:
            print("No hay herramientas registradas")
            return "regresar_uno"

        for indice in range(len(lista_herramientas)):
            herramienta = lista_herramientas[indice]
            print(str(indice + 1) + ". " + herramienta["nombre"] + " (" + herramienta["codigo"] + ")")

        numero_regresar = len(lista_herramientas) + 1
        numero_menu = len(lista_herramientas) + 2
        numero_finalizar = len(lista_herramientas) + 3
        print(str(numero_regresar) + ". Regresar uno")
        print(str(numero_menu) + ". Regresar al menú principal")
        print(str(numero_finalizar) + ". Finalizar sesión")
        opcion = input("Elija un número: ").strip()

        if opcion == str(numero_regresar):
            return "regresar_uno"
        elif opcion == str(numero_menu):
            return "menu_principal"
        elif opcion == str(numero_finalizar):
            return "finalizar_sesion"
        else:
            opcion_valida = False
            for indice in range(len(lista_herramientas)):
                if opcion == str(indice + 1):
                    opcion_valida = True
                    resultado = ver_detalle_herramienta(lista_herramientas[indice])
                    if resultado == "menu_principal" or resultado == "finalizar_sesion":
                        return resultado
                    # regresar_uno repite esta lista, la pantalla anterior.

            if not opcion_valida:
                print("Opción inválida. Elija un número del 1 al " + str(numero_finalizar) + ".")


# ==================== MENÚ DE HERRAMIENTAS ====================

def modulo_herramientas():
    # Leer el archivo una sola vez al entrar al módulo.
    lista_herramientas = cargar_herramientas()

    while True:
        print("Módulo de Herramientas")
        print()
        print("1. Registrar herramientas")
        print("2. Actualizar herramientas")
        print("3. Ver herramientas")
        print("4. Regresar uno")
        print("5. Regresar al menú principal")
        print("6. Finalizar sesión")
        opcion = input("Elija un número: ").strip()
        resultado = ""

        if opcion == "1":
            resultado = registrar_herramientas(lista_herramientas)
        elif opcion == "2":
            resultado = actualizar_herramientas(lista_herramientas)
        elif opcion == "3":
            resultado = ver_herramientas(lista_herramientas)
        elif opcion == "4":
            # Regresar solo un nivel: al menú que abrió este módulo.
            return "regresar_uno"
        elif opcion == "5":
            # Esta señal siempre debe llegar al menú principal.
            return "menu_principal"
        elif opcion == "6":
            return "finalizar_sesion"
        else:
            print("Opción inválida. Elija un número del 1 al 6.")

        # Propagar estas decisiones sin volver a mostrar este menú.
        if resultado == "menu_principal" or resultado == "finalizar_sesion":
            return resultado
        # Con regresar_uno, el ciclo vuelve al menú de Herramientas.


def menu_principal():
    # Repetir el menú al regresar de cada módulo.
    while True:
        print("Seleccione una opción")
        print("1. Obras")
        print("2. Materiales")
        print("3. Herramientas")
        print("4. Finalizar sesión")
        opcion = input("Elija un número: ").strip()

        if opcion == "1":
            # Guardar el texto que devuelve el módulo.
            resultado = modulo_obras()
            if resultado == "finalizar_sesion":
                # Volver a main(), que ya tiene un return después del menú.
                return
            # Con "regresar_uno" o "menu_principal", el ciclo muestra
            # otra vez este menú. Por ahora, ambos llevan a esta pantalla.
        elif opcion == "2":
            # Guardar el texto que devuelve el módulo.
            resultado = modulo_materiales()
            if resultado == "finalizar_sesion":
                # Volver a main(), que ya tiene un return después del menú.
                return
            # Con "regresar_uno" o "menu_principal", el ciclo muestra
            # otra vez este menú. Por ahora, ambos llevan a esta pantalla.
        elif opcion == "3":
            # Herramientas comunica su decisión igual que los otros módulos.
            resultado = modulo_herramientas()
            if resultado == "finalizar_sesion":
                # Devolver la señal a main(), que ya termina tras el menú.
                return resultado
            # Las otras dos señales permiten repetir el menú principal.
        elif opcion == "4":
            return
        else:
            print("Opción inválida. Elija un número entero del 1 al 4.")

def main():
    # Mantener el contador dentro de esta función al volver a Inicio.
    intentos_fallidos = 0

    while True:
        opcion = mostrar_inicio()

        if opcion == "1":
            usuario = iniciar_sesion()

            if usuario != "":
                print("Bienvenido " + usuario)
                print()
                menu_principal()
                return
            else:
                # Un fallo en uno o ambos datos cuenta como un solo intento.
                intentos_fallidos = intentos_fallidos + 1
                print("Error, inténtelo de nuevo")

                # Terminar al tercer fallo sin volver a mostrar Inicio.
                if intentos_fallidos == 3:
                    print("Límite de intentos alcanzado. Vuelva a iniciar el programa para volver a intentarlo")
                    return

        elif opcion == "2":
            return
        else:
            # Las opciones inválidas no modifican los intentos fallidos.
            print("Opción inválida. Elija 1 o 2.")


main()
