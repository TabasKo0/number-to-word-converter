import sys
n=input("Enter your number")
if int(n)==0:
    print("zero")
    sys.exit()
for i in range(len(n)):
    if n[i]!='0':
        n=n[i:]
        break
l=len(n)

n2=n[::-1]
o=["thousand","million","billion","trillion","quadrillion"]
v1=o[:l//3][::-1]

def conv(n2):
    v2=[]
    while n2!="":
        v2=[n2[:3][::-1]]+v2
        n2=n2[3:]
    return v2
    
def namkaran(v2):
    te=["ten", "eleven","twelve","thirteen","fourteen","sixteen","seventeen","eighteen","nineteen"]
    ty=[" ","ten","twenty","thirty","forty","fifty","sixty",
    "seventy","eighty","ninety"]
    one=["","one","two","three","four","five","six",
     "seven","eight","nine"]
    v3=[]
    if len(v2[0])==2:
        v2[0]="0"+v2[0]
    elif len(v2[0])==1:
        v2[0]="00"+v2[0]
    for i in v2:
        if i[0]=="0":
            h=""
        else:
            h=" hundred "
        if i[1]=="1":
            w=one[int(i[0])]+h+te[int(i[2])]
        else:
            w=one[int(i[0])]+h+ty[int(i[1])]+" "+one[int(i[2])]
        v3.append(w)
        w=""
    return v3  
v3= namkaran(conv(n2)) 
v1=o[:l//3][::-1]
the_word=""
for j in range((len(v1)+len(v3))):
    if j%2==0:
        the_word+=v3[j//2]+" "
    elif v3[j//2]!="  ":
        the_word+=v1[j//2]+" "
print(the_word.lstrip())