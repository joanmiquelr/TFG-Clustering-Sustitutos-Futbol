import LanusStats as ls  #GitHub
import pandas as pd

fbref = ls.Fbref()


datos = fbref.get_all_player_season_stats('Big 5 European Leagues', "2024-2025", save_csv=False)
print(datos[0])
df = pd.DataFrame(datos[0])  # datos[1] son las estadisticas de los porteros, no nos interesan
df.to_csv("Big_5_European_Leagues_all_stats_LanusStats", index=False)




