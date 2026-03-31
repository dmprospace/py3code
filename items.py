# random sales dictionary
sales = { 'apple': 2 } #, 'orange': 3, 'grapes': 4 }

sales['apple']={}
sales['orange']={}
sales['grapes']={}


items = sales.items()
print('Original items:', items)


sales['apple']['q_colums']=['a','b']
sales['apple']['q_rows']=[('f11','f12'),('f21','f22'),('f31','f32')]
sales['apple']['count']=9

sales['orange']['q_colums']=['a','b']
sales['orange']['q_rows']=[('f11','f12'),('f21','f22'),('f31','f32')]
sales['orange']['count']=3

sales['grapes']['q_colums']=['a','b']
sales['grapes']['q_rows']=[('f11','f12'),('f21','f22'),('f31','f32')]
sales['grapes']['count']=7


print('Updated items:', items)


for i in sales.items():
    #j=i.items()
    print(i[1])


x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
y={k: v for k, v in sorted(sales.items(), key=lambda item: item[1]['count'], reverse=True)}

print(x)
print(y)