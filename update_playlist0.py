import requests

# Lista de URLs PHP con token para obtener cada stream
urls_php = [
    "https://53ffe34dfb.stream.api.streamlatam.com/hls-url.php?token=O80SW4-TyU6VVJnMmkLSXQWeGkC",
    "https://da5aef90cb.stream.api.streamlatam.com/hls-url.php?token=C5qhwt-Qyh7bnJrPygwaTQadSg5",
    "https://f0a29b69f0.stream.api.streamlatam.com/hls-url.php?token=TCCmyj-VF5Ja3x8SRo1ZyoNAxo8",
	"https://dca610047d.stream.api.streamlatam.com/hls-url.php?token=DDOqZu-RFlFd19sThYpRDUdBBYg",
	"https://2bbf7695f7.stream.api.streamlatam.com/hls-url.php?token=j8AeGe-aiVLY0JCMhg9WSUzeBg0",
	"https://90b449c9f8.stream.api.streamlatam.com/hls-url.php?token=MVKpo0-TUtBdmplXBIocXAUFhIh",
	"https://fe64287420.stream.api.streamlatam.com/hls-url.php?token=UiNPYo-VXREVlx9YxcIRCsOKhcA",
	"https://807a284ada.stream.api.streamlatam.com/hls-url.php?token=PbBx5N-UH9IfjB4aBsgKAoLIRso",
    # agrega más URLs aquí
]

archivo_m3u8 = "playlist.m3u"

def obtener_url_m3u8(url_php):
    try:
        resp = requests.get(url_php)
        resp.raise_for_status()
        data = resp.json()
        url = data.get("url")
        if url:
            # Cambiar 'legacy.m3u8' por '0/chunklist.m3u8' para calidad FHD
            return url.replace("legacy.m3u8", "0/chunklist.m3u8")
        else:
            print(f"No se encontró la URL en la respuesta de {url_php}")
            return None
    except Exception as e:
        print(f"Error al obtener URL de {url_php}: {e}")
        return None

def actualizar_playlist(urls_php):
    contenido = "#EXTM3U\n"
    for i, url_php in enumerate(urls_php, start=1):
        url_m3u8 = obtener_url_m3u8(url_php)
        if url_m3u8:
            nombre_canal = f"ECDF{i}"
            contenido += f"#EXTINF:-1,{nombre_canal}\n{url_m3u8}\n"
    with open(archivo_m3u8, "w") as f:
        f.write(contenido)
    print(f"Archivo {archivo_m3u8} actualizado con {len(urls_php)} canales.")

if __name__ == "__main__":
    actualizar_playlist(urls_php)
