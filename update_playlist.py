import requests

url_php = "https://53ffe34dfb.stream.api.streamlatam.com/hls-url.php?token=O80SW4-TyU6VVJnMmkLSXQWeGkC"
archivo_m3u8 = "playlist.m3u"

def obtener_url_m3u8():
    resp = requests.get(url_php)
    resp.raise_for_status()
    data = resp.json()
    url = data.get("url")
    if url:
        return url.replace("legacy.m3u8", "0/chunklist.m3u8")
    else:
        raise ValueError("No se encontró la URL en la respuesta")

def actualizar_playlist(url_m3u8):
    contenido = f"#EXTM3U\n#EXTINF:-1,Canal Ejemplo\n{url_m3u8}\n"
    with open(archivo_m3u8, "w") as f:
        f.write(contenido)

if __name__ == "__main__":
    url = obtener_url_m3u8()
    actualizar_playlist(url)
