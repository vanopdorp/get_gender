from main import main

jongens = ['Mohammed', 'Ali', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas','joep','Daan','Owen','Lucas','julan','john','chris','mattijs','sem','lars','finn','luuk','mees','thijs','sam','max','levi','noud','boaz','milan','david','mats','matz','wahib','matteo','noah','ben','tim','jens','joris','senn','youssef','alexander','manon','eddy','artemis']
meisjes = ['Ailynn','sophie','Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia','Daana','feline','Fabienne','Luna','Julia','Anna','tess','lisa','linde','lotte','noor','femke','sara','milou','evi','maud','elyse','yara','livia','zoe','eva','lena','lilly','meisje','rose','rose','amelia','lily','chloe','isabel','nora','camille','elsa','clara','anais','juliette','lucie','alice','seline','ilse']
for i,name in enumerate(jongens):
    jongens[i] = name.capitalize()
for i,name in enumerate(meisjes):
    meisjes[i] = name.capitalize()

jongens = set(jongens)
meisjes = set(meisjes)
print(jongens)
def test_jongen(name):
    # main expects argv-like list, first element is script name
    result = main(['jongenofmeisje.py', name])
    return result is False  # jongen: False (is not a girl)

def test_meisje(name):
    result = main(['jongenofmeisje.py', name])
    return result is True  # meisje: True (is a girl)

faulty_names = []
fault, correct = 0, 0
for jongen in jongens:
    if not test_jongen(jongen):
        faulty_names.append(jongen)
        fault += 1
    else:
        correct += 1
for meisje in meisjes:
    if not test_meisje(meisje):
        faulty_names.append(meisje)
        fault += 1
    else:
        correct += 1
print(faulty_names)
percentage_correct = correct / (correct + fault) * 100
print(f'Correct: {correct}, Faulty: {fault}, Percentage correct: {percentage_correct}%')
