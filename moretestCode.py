mySentence = 'plays tonight'

team_list = ['saints','browns','seahawks']

def team_function(name):
    lst = []
    for i in team_list:
        msg = '{} {} {}'.format(name,mySentence,i)
    return lst
