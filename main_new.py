import matplotlib.pyplot as plot
from friends_age import FriendsAge
from id_from_username import IDFromUsername

getID = IDFromUsername(input())
ID = getID.execute()

getAges = FriendsAge(ID)
ages = getAges.execute()

max_age = max(ages)

array = [0] * (max_age + 1) # Сформируем массив из нулей размером с максимальный возраст + 1


for age in ages:
   array[age] += 1

for index, value in enumerate(array):
   if value != 0:
        res = str(index) + ' '
        for i in range(value):
            res += '#'
        print(res)
####

#uname = input('Имя пользователя: ')
#uclient = IDFromUsername(uname)
#uid = uclient.execute()

#friends_client = FriendsAge(uid)
#friends = friends_client.execute()

#for (age, count) in ages:
 #   print('{} {}'.format(int(age), '#' * count))

fig, ax = plot.subplots()
rects = ax.bar(list(map(lambda x: x[0], enumerate(array))), list(map(lambda x: x[1], enumerate(array))), 1)

plot.xlabel('Age')
plot.ylabel('Count')
plot.title('Friends')
plot.subplots_adjust()
plot.show()