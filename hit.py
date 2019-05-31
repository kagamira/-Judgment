import sys

# 自キャラの座標を聞く
my_input = []
my = []
my_input +=input('x座標 y座標 幅 高さを半角で入力せよ。スペースで間を区切って>>').split()
for s in my_input:
    my.append(int(s))

# 敵キャラの数を聞く
print('敵の数は？')
e_num=int(input())

# 敵キャラの座標を聞く
e_list=[]
es_list=[]
count=0
for i in range(e_num):
    count += 1
    print('%d体目のx座標 y座標 幅 高さを半角で入力せよ。スペースで間を区切って' % (count))
    e_list += input().split()

for s in e_list:
    es_list.append(int(s))

# 当たっているか判定
hit_list=[]
count=0
for i in range(e_num):
    count += 1
    if my[2] * my[3] > es_list[2] * es_list[3]:
        if my[0] <= es_list[0] and es_list[0] <= my[0] + my[2]:
            if my[1] <= es_list[1] and es_list[1] <= my[1] + my[3]:
                hit_list += str(count)
        elif my[0] <= es_list[0] + es_list[2] and es_list[0] + es_list[2] <= my[0] + my[2]:
            if my[1] <= es_list[1] + es_list[3] and es_list[1] + es_list[3] <= my[1] + my[3]:
                hit_list += str(count)
    else:
        if es_list[0] <= my[0] and my[0] <= es_list[0] + es_list[2]:
            if es_list[1] <= my[1] and my[1] <= es_list[1] + es_list[3]:
                hit_list += str(count)
        elif es_list[0] <= my[0] + my[2] and my[0] + my[2] <= es_list[0] + es_list[2]:
            if es_list[1] <= my[1] + my[3] and my[1] + my[3] <= es_list[1] + es_list[3]:
                hit_list += str(count)
    del es_list[0:4]

# 結果を出力する
count = 0
while count < len(hit_list):
    print('敵機%sが当たり' % (hit_list[count]))
    count += 1