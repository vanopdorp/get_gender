def get_gender(name):
    name = name.lower()
    alfabet_as_a_string = 'aceyfgqhibvklnodrstuwjxpzm'
    vector = []
    alfabet = {}
    for index,token in enumerate(alfabet_as_a_string):
        alfabet[token] = index
    for t in name:
        vector.append(alfabet[t])
    conditions = ['<','>','<=','>=','==','!=']
    answer= (vector[0] + vector[1])* (vector[len(vector)-1])
    drempel = 110
    return answer < drempel
import sys
if __name__ == '__main__':
    if get_gender(sys.argv[1]):
        print(sys.argv[1],"is a girl")
    else:
        print(sys.argv[1],"is a boy")
