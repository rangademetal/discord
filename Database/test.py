from Connect import Connection
import random


db = Connection('localhost', 'root', 'Sad1996.', 'discord2')

database = db.connect()

point = db.get_point_lust(database, 'mainitaiete#0483')
print('Point:', point)
username = db.get_id_user(database, 'mainitaiete#0483')
print('ID:', username)
point = point + 1


if random.randint(0, 100) > 50:
	db. update_points(database, point, username)

print(db.get_point_lust(database, 'mainitaiete#0483'))