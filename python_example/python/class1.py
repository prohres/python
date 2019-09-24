from hero import *

myhero1 = Hero("Kozak", 5, "Ukrop")
myhero2 = Hero("Sotnuk", 6, "Patriot")

# MAIN +++++++++++++++++++++++++++++
myhero1.show_hero()
myhero2.move()
myhero1.level_up()
myhero1.show_hero()
myhero1.set_health(60)
myhero1.show_hero()