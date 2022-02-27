from pymongo import MongoClient

# Crea un’istanza del client
client = MongoClient("mongodb://localhost:27017/")

# Accede ad un database (se non presente, allora è creato)
db = client["reserve"]

# Accedo ad una collezione (se non presente, allora è creata)
posts = db["posts"]

# Accedo ad una collezione (se non presente, allora è creata)
