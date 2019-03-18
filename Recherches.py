class Recherche:

  def __init__(self, Nom, Adresse, city, Code_Postal,telephone, lat,lon):
    self.Nom = Nom
    self.Adresse = Adresse
    self.city = city
    self.Code_Postal = Code_Postal
    self.telephone = telephone
    self.lat= lat
    self.lon = lon


  def find_place(conn, cp=75):

    cur = conn.cursor()
    cur.execute("SELECT Nom,Téléphone,lat,lon FROM fooding WHERE (instr(Code_Postal ,'{}')) ".format(cp))


    while True:
      tple = cur.fetchone()
      if tple is None :
        break
      is_find = tple[0]
      if Recherche.is_place_available(conn, cp):
        return is_find
    return None



  def is_place_available (conn, cp):
    cur = conn.cursor()

    request = "SELECT * FROM fooding WHERE instr(Code_Postal ,'{}') "
    cur.execute(request.format(cp))

    if cur.fetchone() is None : return False

    request = "SELECT * FROM fooding WHERE instr(Code_Postal ,'{}') "
    cur.execute(request.format(cp))

    return cur.fetchone()
