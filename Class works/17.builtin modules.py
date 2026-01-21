# # Using datetime module to get today's date and its components :

from datetime import date,time
today=date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())

# Creating date objects using datetime module :

from datetime import date,time,datetime
now = datetime.now()
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Weekday (0=Monday):", now.weekday())
print("ISO Weekday (1=Monday):", now.isoweekday())

# Using datetime module to get current date and time and its components :  

from datetime import date,time ,datetime
now =datetime.now()
print(now)
print("year:",now.year)
print("month:",now.month)
print("day:",now.day)
print("hour:",now.hour)
print("minute:",now.minute)
print("second:",now.second)
print("microsecond:",now.microsecond)

# Formmatting date and times :

from datetime import date,time,datetime
now =datetime.now()
print(now)
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%H:%M:%S"))
print(now.strftime("%I:%M:%S"))
print(now.strftime("%A, %d %b %Y %I:%M:%S %p"))

# Performing date and time arithmetic using datetime module :

from datetime import date,time,datetime,timedelta
today = datetime.now()
now=datetime.now()
n=today-timedelta(days=5)
print(n)
h=now-timedelta(days=5)
print(n)
h=now-timedelta(hours=15)
print(h)

# collections :

from collections import Counter,defaultdict,deque
n='Subhash is a good boy.he can\'t ride bike.'.split()
res=Counter(n)
print(res)
# 
from collections import Counter,defaultdict,deque
n=[9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
res=Counter(n)
print(res)
# 
from collections import Counter,defaultdict,deque
n=[9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
res=defaultdict(str)
for i in n:
    res[i]+=str(i)
print(res)

# Queue :

from collections import Counter,defaultdict,deque
q=deque()
q.appendleft(10)
print(q)
q.appendleft(20)
print(q)
q.appendleft(30)
print(q)
q.pop()
print(q)

# snake and ladder game using deque :

p1=input("Enter player-1:")
p2=input("Enter player-2:")
p1_sc=0
p2_sc=0
winning_point=20
snakes={14:7,27:13,33:2,49:28,55:42,65:22,73:16,88:79,93:76,99:1}
ladders={4:24,12:30,25:44,32:53,46:61,58:72,66:87,75:86,82:95}
def dice():
    return random.randint(1,6)
def player_1():
    st=input("you want to[c]ontinue or [q]uit:").lower()
    if st=='c':
        d=dice()
        print(f"{p1} dice score:{d}")
        p1_sc+=d
        if p1_sc in snakes:
            p1_sc=snakes[p1_sc]
            print(f"{p1}-total score:{p1_sc}\n snake bite--------")
        print(f"{p1}-total score is:{p1_sc}")
    else:
        print(f"{p2} won the game!!!!")
        sys.exit()
def player_2():
    st=input("you want to[c]ontinue or [q]uit:").lower()
    if st=='c':
        d=dice()
        print(f"{p2} dice score:{d}")
        p2_sc+=d
        print(f"{p2}-total score is:{p2_sc}")
    else:
        print(f"{p1} won the game!!!!")
        sys.exit()
while p1_sc<winning_point and p2_sc<winning_point:
    player_1()
    player_2()