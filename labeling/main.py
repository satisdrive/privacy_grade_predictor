import json
import random

points2i = {"blocker":0,"bad":1,"neutral":2,"good":3}

def cleanse(line):
    import re
    return re.sub(" +"," ",re.sub("[^a-zA-Z0-9 .-]", '', re.sub("[\r\n]", ' ', str(line).lower())))

f = open('tosdr.json',encoding='utf-8')
trc = open('jsons/train.csv','w')
tec = open('jsons/test.csv','w')
vc = open('jsons/val.csv','w')
#print('name,pclass,point,score,quote',file=trc) # header
#print('name,pclass,point,score,quote',file=vc) # header
#print('name,pclass,point,score,quote',file=tec) # header
print('point,text',file=trc) # header
print('point,text',file=vc) # header
print('point,text',file=tec) # header
random.seed(4963)
for i,line in enumerate(f):
    jdata = json.loads(line)
    name = jdata["slug"]
    pclass = jdata["class"]
    r = random.randint(0,99)
    for pd in jdata["pointsData"]:
        qt = cleanse(jdata["pointsData"][pd]["quoteText"])
        score = jdata["pointsData"][pd]["tosdr"]["score"]
        point = jdata["pointsData"][pd]["tosdr"]["point"]
#        print('{0},{1},{2},{3},{4}'.format(name,pclass,point,score,qt), file=(trc if r < 60 else (vc if r < 80 else tec)))
#        print('{0},{1}'.format(points2i[point],qt), file=(trc if r < 60 else (vc if r < 80 else tec)))
        print('{0},{1}'.format(point,qt), file=(trc if r < 60 else (vc if r < 80 else tec)))
