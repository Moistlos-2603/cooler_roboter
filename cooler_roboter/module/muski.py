from pybricks.hubs import EV3Brick

def alle_meine_entchen(ev3: EV3Brick, tempo=200, volume=5):
  ev3.speaker.set_volume(volume)

  ev3.speaker.play_notes(['C4/4', 'D4/4', 'E4/4', 'F4/4','G4/2','G4/2',
                          'A4/4','A4/4','A4/4','A4/4','G4/1',
                          'A4/4','A4/4','A4/4','A4/4','G4/1',
                          'F4/4','F4/4','F4/4','F4/4','E4/2','E4/2',
                          'D4/4','D4/4','D4/4','D4/4','C4/1'], tempo)
