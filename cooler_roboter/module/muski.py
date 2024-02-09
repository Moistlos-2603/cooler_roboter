from pybricks.hubs import EV3Brick

def alle_meine_entchen(ev3: EV3Brick, tempo=200, volume=5):
  ev3.speaker.set_volume(volume)

  ev3.speaker.play_notes(['A3/8','C4/8','D4/4','D4/4','D4/8','E4/8','F4/4','F4/4',
                          'F4/8','G4/8','E4/4','E4/4','D4/8','C4/8','C4/8','D4/3',
                          'A3/8','C4/8','D4/4','D4/4','D4/8','E4/8','F4/4','F4/4',
                          'F4/8','G4/8','E4/4','E4/4','D4/8','C4/8','D4/2',
                          'A3/8','C4/8','D4/4','D4/4','D4/8','F4/8','G4/4','G4/4',
                          'G4/8','A4/8','A#4/4','A#4/4','A4/8','G4/8','A4/8','D4/3',
                          'D4/8','E4/8','F4/4','F4/4','G4/4','A4/8','D4/3',
                          'D4/8','F4/8','E4/4','E4/4','F4/8','D4/8','E4/1'], tempo)
