import pandas as pd
import time
import random
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

# --- CONFIGURACIÓN ---
INPUT_CSV = 'datos_csv.csv'
OUTPUT_CSV = 'datos_jugadores_v2.csv'

def nuevo_driver():
    options = uc.ChromeOptions()
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-background-timer-throttling")
    options.add_argument("--disable-backgrounding-occluded-windows")
    options.add_argument("--disable-renderer-backgrounding")

    driver = uc.Chrome(
        use_subprocess=True,
        version_main=142,
        options=options
    )

    driver.set_page_load_timeout(15)
    driver.set_script_timeout(15)

    return driver


def procesar_jugadores():
    # 1. Cargar datos
    try:
        df = pd.read_csv(INPUT_CSV)
        # Obtenemos nombres únicos para no buscar lo mismo dos veces
        lista_jugadores = df['Jugador'].unique()
        print(f"📋 Cargados {len(lista_jugadores)} jugadores únicos para procesar.")
    except FileNotFoundError:
        print(f"❌ No se encontró el archivo {INPUT_CSV}")
        return

    print("🚀 Iniciando Chrome (esto puede tardar unos segundos)...")

    # --- CORRECCIÓN AQUÍ ---
    # Forzamos la versión 142 para que coincida con tu navegador instalado
    driver = uc.Chrome(use_subprocess=True, version_main=142)

    resultados = []

    try:
        for i, jugador in enumerate(lista_jugadores):

            print(f"[{i + 1}/{len(lista_jugadores)}] Buscando: {jugador}...")

            nombre_busqueda = jugador.replace(" ", "+")
            url = f"https://es.besoccer.com/buscar/{nombre_busqueda}"

            # --- RETRY AUTOMÁTICO POR JUGADOR ---
            intentos = 0
            exito = False

            while intentos < 3 and not exito:
                try:
                    driver.get(url)
                    time.sleep(random.uniform(2, 4))

                    # Resultados en lista (BeSoccer)
                    resultados_busqueda = driver.find_elements(By.CSS_SELECTOR, ".search-item-name a")
                    if len(resultados_busqueda) > 0:
                        resultados_busqueda[0].click()
                        time.sleep(random.uniform(2, 4))

                    # Intento de extraer la posición
                    try:
                        pos_elem = driver.find_element(By.CSS_SELECTOR, "span.rol-tag.desc-rol")
                        posicion = pos_elem.text.strip()
                        print(f"   ✓ Posición: {posicion}")
                    except:
                        print("   ⚠ No encontré la posición.")
                        posicion = "No encontrada"

                    resultados.append({
                        "Player": jugador,
                        "Posicion": posicion
                    })

                    exito = True  # Terminó sin errores

                except Exception as e:
                    intentos += 1
                    print(f"   ❌ Error con {jugador} (intento {intentos}/3): {e}")

                    # Reiniciar completamente el driver solo si hay error
                    print("   🔄 Reiniciando driver y reintentando...")
                    try:
                        driver.quit()
                    except:
                        pass

                    time.sleep(2)
                    driver = nuevo_driver()

            # Si después de 3 intentos no se consigue
            if not exito:
                print(f"   ⛔ No se pudo procesar {jugador} después de 3 intentos.")
                resultados.append({
                    "Player": jugador,
                    "Posicion": "ERROR"
                })

    except KeyboardInterrupt:
        print("\n🛑 Detenido por el usuario.")

    finally:
        print("Cerrando navegador...")
        # A veces el cierre falla si el proceso ya murió, lo ponemos en try/except
        try:
            driver.quit()
        except:
            pass

        if resultados:
            df_res = pd.DataFrame(resultados)
            df_res.to_csv(OUTPUT_CSV, index=False)
            print(f"\n💾 Guardado en {OUTPUT_CSV}")
            print(df_res.head())


if __name__ == "__main__":
    procesar_jugadores()