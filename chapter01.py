#coding:utf-8

from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter
from collections import ChainMap

'''
1.namedtuple 就是实现tuple的重组  通过类的实例属性进行实现且采用了__slots__来节省看空间
2.deque 双端队列 GIL控制 线程安全的
3.defaultdict 默认字典  就是在初始化字典的时候默认了值（可调用对象）、
4.OrderedDict 有序字典 在python3中均已成为有序字典
5.Counter 计数器  在实例的时候将可迭代对象作为参数即可 获取的是字典形式 且会按照次数由大到小排列
6.ChainMap 就是连接 迭代对象 但是对for出来的数据时只展示唯一一个key 所以会出现遍历不全的现象
'''

'''
应用场景 对数据库的表增加一列
'''
t2 = ('wxt',23,'chapter')
User = namedtuple('User',('name','age','edu','school'))  #通过namedtuple获取一个类  且名字和所含参数
#user1 = User('mqy',22,'master') #将数据组装到实例方式1
user2 = User(*t2,'daxue') #直接将迭代对象进行拆包 *args **kwargs
#卸包方式  就是对应位置取值 获取不需要的可添加可变参数代替即可
#print(user1.name)
print(user2.name)


'''
扩展字典的值，进行组装符合需求
'''

s = 'sfjoajfiajf'
d1 = defaultdict(int) #将值默认为int类型且默认值为0
for i in s:
    d1[i]+=1   #进行操作计数
print(d1)

def return_dict():
    return {
        'name':'mqy',
        'age':23,
        'extra':{

        }
    }

d2 = defaultdict(return_dict)
for i in s:
    d2[i]
print(d2)
print(d2.popitem())
new_d = {}.fromkeys(s) #创建一个新字典需要重新接受才可获取
print(new_d)

'''
双端队列 进行通讯操作
'''

dq = deque()
dq.append('start1')
dq.appendleft('start2')
dq.append('start3')
print(dq.popleft())
print(dq)


'''
计数器 
'''
counter = Counter(s)  #进行统计 且生成字典将值大的优先排在前面
print(counter)
print(counter.most_common(2)) #输出前几
counter.update('sjfosjfso')
print(counter)

