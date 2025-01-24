import os
import time

def run_multiwfn_and_rename(file):
    # Define el nombre del archivo de comandos estático
    comandos_base = 'comando_multiwfn.txt'  # Aquí usas tu archivo de comandos específico
    
    # Verifica que el archivo comando_multiwfn.txt existe
    if not os.path.exists(comandos_base):
        print(f"Error: El archivo {comandos_base} no existe en el directorio actual.")
        return
    
    # Leer el contenido del archivo de comandos
    with open(comandos_base, 'r') as f:
        comandos = f.readlines()
    
    # Extraer el nombre base del archivo sin la extensión
    base_name = os.path.splitext(file)[0]
    
    # Crear un archivo temporal para los comandos
    temp_commands = 'temp_comando_multiwfn.txt'
    with open(temp_commands, 'w') as f_out:
        # Copiar los comandos del archivo base
        f_out.writelines(comandos)
        # Aquí puedes agregar cualquier otro comando específico que requiera Multiwfn
        f_out.write("func1.cub\n")  # Comando ejemplo para que Multiwfn lo ejecute
        f_out.write("0\n")  # Finaliza el comando
        f_out.write("func2.cub\n")  # Otro comando de ejemplo
    
    # Ejecutar Multiwfn para el archivo actual usando el archivo de comandos temporal
    os.system(f"Multiwfn.exe {file} < {temp_commands}")
    
    # Esperar un poco para asegurar que los archivos se generen completamente
    time.sleep(2)  # Ajusta el tiempo si es necesario para que los archivos se generen
    
    # Renombrar los archivos generados a nombres específicos basados en el archivo .wfn
    if os.path.exists('func1.cub'):
        os.rename('func1.cub', f'{base_name}_func1.cub')
    if os.path.exists('func2.cub'):
        os.rename('func2.cub', f'{base_name}_func2.cub')

    # Renombrar también otros archivos de salida que puedas tener
    if os.path.exists('CPprop.txt'):
        os.rename('CPprop.txt', f'{base_name}_CPprop.txt')
    if os.path.exists('CPs.txt'):
        os.rename('CPs.txt', f'{base_name}_CPs.txt')

    # Eliminar el archivo temporal de comandos después de su uso
    os.remove(temp_commands)

    print(f"Proceso completado para {file}")

# Ejemplo de uso:
# Asegúrate de reemplazar 'example.wfn' con el nombre de archivo correcto en el directorio
wfn_files = [f for f in os.listdir('.') if f.endswith('.wfn')]  # Archivos .wfn en el directorio actual

# Iterar sobre todos los archivos .wfn
for wfn_file in wfn_files:
    run_multiwfn_and_rename(wfn_file)
