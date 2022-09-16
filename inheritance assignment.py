
#parent class = the class being inherited from
class Team:
    name = 'Input Team'
    email = ' '
    password = 'GoTeam'

#child classes
#adds additional attributes or methods to Team class without having to either completely(cont.)
#duplicate the class or modify the existing class
class Player(Team):
    position = 'WR'
    minimun_wage = 660,000

class Coach(Team):
    role = 'Head Coach'
    Highest_paid = 15,000,000
