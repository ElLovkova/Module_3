
import re

def make_newstr(s):
    s_new = []
    for i in s:
        if len(i) < 5:
            s_new.append(i)
    return s_new




S = '''Было просто пасмурно, дуло с севера 
А к обеду насчитал сто градаций серого. 
Так всегда первого ноль девятого 
То ли весь мир сошёл с ума, то ли я - того... 
На столе записка от неё смятая 
Недопитый виски допиваю с матами. 
Посмотрю в окно, допишу главу 
Первое сентября, дворник жжёт листву. 
Cерым облакам наплевать на нас 
Если знаешь, как жить - живи 
Ты хотела плыть как все - так плыви!'''
S_wp = re.sub(r'[^\w\s]','', S)
s1 = S_wp.split()

print(make_newstr(s1))

