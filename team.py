class Teams:
  def __init__(self, members):
    self.__myTeam = members

  def __len__(self):
    return len(self.__myTeam)
  
  def __contains__(self, x):
      return x in self.__myTeam
  
  def __iter__(self):
      return iter(self.__myTeam)

def main():
 classmates = Teams(['John', 'Steve', 'Tim'])
 print (len(classmates))
 print('Tim in team: ', 'Tim' in classmates)
 print('Sam in team: ', 'Sam' in classmates)

 for c in classmates:
    print(c)
        
 print('Does len method exists: ', "__len__" in dir(classmates))

main()

