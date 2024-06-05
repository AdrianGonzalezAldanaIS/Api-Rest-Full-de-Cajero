import os.path

codigo = ''
def contador(programa):
    count = 0
    com_multi = False
    try:
        archivo = open(programa, 'r', encoding='utf-8') 
        for linea in archivo:
            linea = linea.strip()
            #print(not linea)
            if not linea:
                continue
            #verifica el prefijo '#'
            if linea.startswith("#"):
                continue
            if linea[0:3] == '"""':
                if linea[-3:] == '"""' and len(linea) != 3: #comentario multilínea
                    continue
                else:
                    com_multi = not com_multi
                    continue
            if com_multi:
                continue
            count += 1
    except FileNotFoundError as error:
        print(error)
    return count


routes_files = ['cajero_back\\src\\dao\\TarjetaDAO.py',  'cajero_back\\src\\database\\postgres_db.py',  'cajero_back\\src\\interfaces\\ITarjeta.py', 'cajero_back\\src\\models\\Tarjeta.py', 'cajero_back\\src\\models\\UsuarioDetalle.py', 'cajero_back\\src\\routes\\TarjetasRoutes.py',  'cajero_back\\src\\services\\ServicioTarjeta.py', 'cajero_back\\src\\utils\\Dateformat.py', 'cajero_back\\src\\app.py', 'cajero_back\\src\\config.py', 'cajero_front\\src\\consumo\\cliente_api.py', 'cajero_front\\src\\consumo\\cliente_consumo.py', 'cajero_front\\src\\consumo\\cliente_servicio.py', 'cajero_front\\src\\formularios\\tarjeta_forms.py', 'cajero_front\\src\\templates\\base.html', 'cajero_front\\src\\templates\\formularios\\cliente.html', 'cajero_front\\src\\templates\\formularios\\ingresar.html', 'cajero_front\\src\\templates\\formularios\\nip.html', 'cajero_front\\src\\app.py', 'cajero_front\\src\\config.py']

def contador_archivos(routes_files):
    result = 0
    if len(routes_files) != 0:
        if isinstance(routes_files, list):
            for archivo in routes_files:
                count = contador(archivo)
                print(f"Archivo: {archivo} tiene {count} lineas")
                result = result + count
        else:
            raise BaseException("El argumento debe ser una lista")
    else:
        raise BaseException("La lista esta vacia")
    return result
    
print(f"El total de líneas son: {contador_archivos(routes_files)}")