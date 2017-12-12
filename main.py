import pandas
import numpy
import statistics

src = pandas.read_csv('test.csv', index_col='PassengerId')
src2 = pandas.read_csv('train.csv', index_col='PassengerId')

def get_genders_count(data):
    # Функция возвращает кол-во мужчин и женщин [мужчины,женщины]
    males = 0
    females = 0
    for gender in data:
        if gender == 'male':
            males += 1
        else:
            females += 1
    return [males,females]

def get_embarked(data):
    # Функция возвращает сопоставление [типы портов] - [кол-во отправившихся из этих портов]
    ports = []
    counts = []
    for port in data:
        if ports.count(port) == 0:
            ports.append(port)
            counts.append(0)
        else:
            counts[ports.index(port)] += 1

    return (ports,counts)

def get_False_count(data):
    # Функция ищет кол-во нулей(False) в переданном поле
    f = 0
    for person in data:
        if person == 0:
            f += 1
    return f

def get_True_count(data):
    # Функция ищет кол-во единиц(True) в переданном поле
    t = 0
    for person in data:
        if person == 0:
            t += 1
    return t

def getGenderInInt(data):
    # Функция переводит пол (male/female) в числовое представление (1/0)
    res = []
    for d in data:
        if d == 'male':
            res.append(1)
        else:
            res.append(0)
    return res

def getNames(sexTarget,ageTarget=0):
    # Функция возвращает список имен всех лиц нужного пола, которые старше определенного возраста
    res = []
    allNames = list(src2['Name'])
    sex = list(src2['Sex'])
    age = list(src2['Age'])
    for i in range(len(allNames)):
        name = allNames[i]
        if (sex[i] == sexTarget and ageTarget <= age[i]):
            if (sex[i] == 'male'):
                if (name.find('(') != -1):
                    tmp = name.split('(')[0].split(' ')
                    index = -2
                    if (tmp[index] == 'Mr.' or tmp[index] == 'Master.'):
                        index = -1
                    res.append(tmp[index])
                else:
                    tmp = name.split('(')[0].split(' ')
                    index = -3
                    if (tmp[index] == 'Mr.' or tmp[index] == 'Master.'):
                        index = -2
                    res.append(tmp[index])
            else:
                if (name.find('(') != -1):
                    tmp = name.split('(')[0].split(' ')
                    index = -3
                    if (tmp[index] == 'Mrs.' or tmp[index] == 'Miss.'):
                        index = -2
                    res.append(tmp[index])
                else:
                    tmp = name.split('(')[0].split(' ')
                    index = -2
                    if (tmp[index] == 'Mrs.' or tmp[index] == 'Miss.'):
                        index = -1
                    res.append(tmp[index])
    return res

print('Кол-во мужчин | женщин')
print(get_genders_count(src2['Sex']))
print()

print('Сколько людей начали путь в различных портах')
print(get_embarked(src2['Embarked']))
print()

print('Сколько людей погибли')
print('{} из {}. Соотношение: {:.2%}'.format(get_False_count(src2['Survived']),len(src2),get_False_count(src2['Survived'])/len(src2)))
print()

print('Пассажиры первого, второго и третьего классов')
print(get_embarked(src['Pclass']))
print()

print('Кол-во супругов')
print(get_True_count(src2['SibSp']))
print()

print('Кол-во детей')
print(get_True_count(src2['Parch']))
print()

print('Коэффициент корреляции Пирсона между супругами и детьми')
print(numpy.corrcoef(src2['SibSp'],src2['Parch']))
print()

print('Коэффициент корреляции Пирсона между возрастом и параметром survival')
print(numpy.corrcoef(src2['Age'],src2['Survived']))
print()

print('Коэффициент корреляции Пирсона между полом человека и параметром survival')
print(numpy.corrcoef(getGenderInInt(src2['Sex']),src2['Survived']))
print()

print('Коэффициент корреляции Пирсона между классом, в котором пассажир ехал, и параметром survival')
print(numpy.corrcoef(src2['Pclass'],src2['Survived']))
print()

print('Средний возраст пассажиров')
print(src2['Age'].mean())

print('Возраст пассажиров: медиана')
print(src2['Age'].median())
print()

print('Cредняя цена за билет')
print(src2['Fare'].mean())

print('Цена за билет: медиана')
print(src2['Fare'].median())
print()

print('Cамое популярное мужское имя на корабле')
print(statistics.mode(getNames('male')))
print()

print('Cамое популярное мужское имя на корабле. Человек должен быть старше 15 лет')
print(statistics.mode(getNames('male',15)))
print()

print('Cамое популярное женское имя на корабле. Человек должен быть старше 15 лет')
print('Это не ошибка. Действительно, самое популярное женское имя на корабле - ...')
print(statistics.mode(getNames('female',15)))