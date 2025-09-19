def main(argv):
    if len(argv) == 1 or argv[1] == '':
        print('no name specified')
        return None
    else:
        name = argv[1]
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
    print(answer)
    if answer < drempel:
        print(f'{name} is a girl')
    else:
        print(f'{name} is a boy')
    return answer < drempel
import sys
if __name__ == '__main__':
    main(sys.argv)
