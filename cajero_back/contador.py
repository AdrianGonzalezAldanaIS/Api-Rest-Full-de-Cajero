from src.exceptions.ArchivoException import ArchivoException
import os.path

codigo = ''
def contador(programa):
    count = 0
    com_multi = False
    try:
        archivo = open(programa, 'r') 
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

routes_files = ['src\\database\\db.py', 'src\\exceptions\\BdException.py', 'src\\models\\entities\\Tarjeta.py', 'src\\models\\services\\ServicioTarjeta.py', 'src\\models\\ITarjeta.py', 'src\\models\\TarjetaDAO.py', 'src\\routes\\TarjetasRoutes.py', 'src\\tests\\test_conn_bd.py', 'src\\tests\\test_querys_tarjetas.py', 'src\\utils\Dateformat.py', 'src\\app.py', 'src\\config.py']

def contador_archivos(routes_files):
    result = 0
    if len(routes_files) != 0:
        if isinstance(routes_files, list):
            for archivo in routes_files:
                count = contador(archivo)
                print(f"Archivo: {archivo} tiene {count} lineas")
                result = result + count
        else:
            raise ArchivoException("El argumento debe ser una lista")
    else:
        raise ArchivoException("La lista esta vacia")
    return result
    
print(f"El total de líneas son: {contador_archivos(routes_files)}")