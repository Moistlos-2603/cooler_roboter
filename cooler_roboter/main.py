#!/usr/bin/env pybricks-micropython
from chaosgame import Chaosgame_Dreieck
from main_controler import Main_Controler

    
# roboter = Main_Controler()
# roboter.run_z_grad(80)





Chaosgame = Chaosgame_Dreieck(init_punkte=((70, 100), (10,10), (130, 10)))
Chaosgame.game()