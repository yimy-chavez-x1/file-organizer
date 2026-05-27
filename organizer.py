from pathlib import Path
import shutil 

EXTENSIONES = {
    ".mp4": "Videos",
    ".mp3": "Music",
    ".jpg": "Imagenes",
    ".png": "Imagenes",
    ".jpeg": "Imagenes",
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".doc": "Documentos",
    ".xlsx": "Documentos",
    ".pptx": "Documentos",
    ".exe": "Instaladores"
}

def organizar_descargas():
    descargas = Path.home() / "Downloads"
    for archivo in descargas.iterdir():
        if archivo.is_file():
            extension = archivo.suffix.lower()
            if extension in EXTENSIONES:
                destino = descargas / EXTENSIONES[extension]
                destino.mkdir(exist_ok=True)
                shutil.move(str(archivo), str(destino / archivo.name))

organizar_descargas()