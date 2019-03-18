class Place:

  def __init__(self,id, Nom, Adresse, city, Code_Postal,  telephone, lat,lon):
    self.id = id
    self.Nom = Nom
    self.Adresse = Adresse
    self.city = city
    self.Code_Postal = Code_Postal
    self.telephone = telephone
    self.lat= lat
    self.lon = lon

  def get_places(conn):

    cur = conn.cursor()

    cur.execute("""SELECT * FROM fooding;""")

    Places = [{"name":elem[0], "address":elem[1], "postcode":elem[2], "city":elem[3]} for elem in cur.fetchall()]

    cur.close()

    return Places
