import sqlite3
import pandas as pd
import random
DBgame = sqlite3.connect('Tronj_db.sqlite3')
game = DBgame.cursor()
daa=game.execute(
		"SELECT * from Tronj_company_details;")
DBgame.commit()
print(daa)
dat=pd.DataFrame(daa)
print(dat)
n	 = random.randint(10000,( 99999))
print(n)
print(dat.iloc[0:1])