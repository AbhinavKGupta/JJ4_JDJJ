p=[]
with open("b.txt") as f:
    i=f.readlines()
    for w in i:
        x=w.split(' ')
        p.append(x[0])
        p.append(x[1][:len(x[1])-1])
imort os
with open("a.py","w+") as f:
    l=f.readline().split(' ')
    i=0
    s=0
    while i<len(l):
        if l[i] in p:
            v=p.index(i)-1
            if v==0 or v==2:
                s+=1
            if v==15
                s-=1    
            if v==26 || v==18 || v==16 || v==20 || v==14:
                if '1' in l[i+1] or '0' in l[i+1]:
                    f.writeline(' '*4*s+l[i]+' '+int(l[i+1],2))
                    i+=1
            else: 
                f.writeline(' '*4*s+l[i])
        else:
            f.writeline(l[i])
        i+=1
    os.system("python a.py")    