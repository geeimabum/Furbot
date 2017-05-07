
def get(data):
  #Nick
  if 'U07LZH5TK' in data['user']:
    user = 'nick'
    #user = 'nik'
  #Tyler
  elif 'U07DQPVSR' in data['user']:
    user = 'tyler'
    #user = 'tylar'
  #Boris
  elif 'U07DRSRDL' in data['user']:
    user = 'boris'
    #user = 'bons'
  #Devon
  elif 'U07DPQ6MQ' in data['user']:
    user = 'devon'
  #Jimmy
  elif 'U07DMSK1C' in data['user']:
    user = 'jimmy'
  #Otto
  elif 'U0BPQAGBH' in data['user']:
    user = 'otto'
  #Ryan
  elif 'U0LMKLV37' in data['user']:
    user = 'ryan'
    #user = 'rian'
  #Tim Gee
  elif 'U0AKWUK0T' in data['user']:
    user = 'tim'
    #user = 'timmy'
  #Tim Johnson
  elif 'U03M4FN3T' in data['user']:
    user = 'gatekeeper'
  #Sully
  elif 'U0FLY63DX' in data['user']:
    user = 'sully'
    #user = 'gymmy'
  #Cameron Fyfe
  elif 'U1QPDU9C5' in data['user']:
    user = 'cameron'
    #user = 'kameron'
  #Jay LaFave
  elif 'U1ZBQGQ9E' in data['user']:
    user = 'jay'
  #Nicole Steere
  elif 'U34P4801Z' in data['user']:
    user = 'nicole'
  #Nicole Steere
  elif 'U3VPUC202' in data['user']:
    user = 'ross'
  #Eric West
  elif 'U07E2QQCV' in data['user']:
    user = 'eric'
  #Adam Wojcik
  elif 'U08E3U0AJ' in data['user']:
    user = 'adam'
  #Jeffffff
  elif 'U0LMPBY6A' in data['user']:
    user = 'jefffffffff'
  #Unknown
  else:
    user = 'human'
  
  return user