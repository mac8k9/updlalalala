import requests

# Lista de URLs PHP con token para obtener cada stream
urls_php = [
    "https://53ffe34dfb.stream.api.streamlatam.com/hls-url.php?token=1h26og-MXU4MGoZYmtucSdoKGtnO3xxMWhqMjExdTtzJjwiZTNzfHBkamtlYTBxbXV2bn5g",
    "https://da5aef90cb.stream.api.streamlatam.com/hls-url.php?token=auBnmD-YWhIaGhJfxs2cwQ4NRs_OV8hLBgyMGEsBWNxBWw_FWtxXyB5GjNnMS0BNXdVPmMQ",
    "https://f0a29b69f0.stream.api.streamlatam.com/hls-url.php?token=BxzR7J-QmVwVDJqciMKKQobOCMDY1ECISAOakIhPV8rC08yLVcrUQN0Ig89EiA5CS1bHW4o",
	"https://dca610047d.stream.api.streamlatam.com/hls-url.php?token=kTPnt8-a0laaHFDXgk2angyFAk_ICMrDQoyKWsNF2NoeWYeB2toIypYCDN-OwwTNW4pNEIC",
	"https://2bbf7695f7.stream.api.streamlatam.com/hls-url.php?token=NE8hEF-TlgybkBmT2EwWwYXBWE5EV0OHGI0GE4cf2VZB0MPb21ZXQ9JYDVPHh17M19XEVNq",
	"https://90b449c9f8.stream.api.streamlatam.com/hls-url.php?token=1li9Ky-MXFjP04ZZjBhVTloLDBoH2JxNTNlFjE1LjRXODwmPjxXYnBgMWRBYTQqYlFobno7",
	"https://fe64287420.stream.api.streamlatam.com/hls-url.php?token=mBD6Dm-bV9OMEFFSB1uWi00Ah1nEHYtGx5qGW0bAztYLGAIEzNYdixOHGtOPRoHbV58MlQW",
	"https://807a284ada.stream.api.streamlatam.com/hls-url.php?token=lMFTg7-bFBMUmJERx8MeXc1DR8FMywsFBwIOmwUAVl7dmEHEVF7LC1BHgltPBUFD30mM1sU",
	"https://f072c02ed2.stream.api.streamlatam.com/hls-url.php?token=X8svLK-WCV5cElwMiouUgsBeConGFAYYSkqEVhhNHtQClVyJHNQUBk0KytGCGAwLVZaBy4h",
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
            nombre_canal = f"EF{i}"
            contenido += f"#EXTINF:-1,{nombre_canal}\n{url_m3u8}\n"
    with open(archivo_m3u8, "w") as f:
        f.write(contenido)
    print(f"Archivo {archivo_m3u8} actualizado con {len(urls_php)} canales.")

if __name__ == "__main__":
    actualizar_playlist(urls_php)



