import folium
from folium.plugins import MarkerCluster

class Carte:

  def __init__(self,cp):
    self.cp = cp


  def sauve(self,conn):
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(lat) FROM fooding ")
    lat_m = cursor.fetchone()[0]
    cursor.execute("SELECT AVG(lon) FROM fooding ")
    lon_m = cursor.fetchone()[0]

    rest_map = folium.Map(location=[lat_m,lon_m],zoom_start=13, tiles='OpenStreetMap')
    marker_cluster = folium.plugins.MarkerCluster().add_to(rest_map)

    cursor.execute("SELECT Nom,Téléphone,lat,lon FROM fooding WHERE (instr(Code_Postal ,'{}')) ".format(self.cp))
    for elem in cursor.fetchall():
        if elem[2] is not None:
            marker = folium.Marker(location=(round(elem[2],6),round(elem[3],6)), popup=elem[0].strip().replace("'","")+' '+str(elem[1])[:15]).add_to(marker_cluster)
    rest_map.save('templates/map.html')
