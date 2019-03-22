import math

def tour(OOL,used,length,route): #Order of Location
    used.append(OOL)
    for i in range(N):
        if i in used:
            continue
 
        LOL= LBP(locations[OOL],locations[i]) #Legnth of Locations
            
        length[0]+=LOL

        if not length[1] is None: # 중간 가지치기를 위한 코드
            if length[0]>length[1]:
                length[0]-=LOL
 #               used.pop()
                return

        tour(i,used,length,route)
        length[0]-=LOL # 루트를 들어갔다가 다시 나올때의 과정.1
        used.pop()     # .2
    
 

    if len(used) is N:
        LOL= LBP(locations[used[0]],locations[used[N-1]]) #Legnth of Locations        
        length[0]+=LOL
        if length[1] is None: # 처음으로 제일 깊게 들어간 루트는 그냥 정답안에 입력
            del route[:]
            for i in range(N):
                route.append(used[i])

            length[1]=length[0]
        elif length[1] >length[0]: # 처음, 그 후부터는 루트의 길이가 정답에 있는 길이보다 짧다면 정답에 입력`
            del route[:]
            for i in range(N):
                route.append(used[i])
            length[1]=length[0]

        length[0]-=LOL
        return
   
 
      


def LBP(p1, p2): # 두점 사이의 거리를 반환하는 함수
    lop1=p1[0]-p2[0] # 두점의 X의 차이
    lop2=p1[1]-p2[1] # 두점의 Y의 차이
    ReLBP=math.sqrt((lop1*lop1)+(lop2*lop2)) #Result of LBP
    return ReLBP
    
        

filename=input()
file=open(filename,"r")
N=int(file.readline())
locations=[[0]*2 for i in range(N)]
for i in range(N): # 파일에서 좌표를 읽어 locations에 저장
    nums=file.readline().split("\n")[0] #좌표들
    locations[i]=nums.split(" ") # 
    locations[i][0]=int(locations[i][0])
    locations[i][1]=int(locations[i][1])
 
used=[]
route=[]
length=[0,None]


result=tour(i,used,length,route)




print(route,length[1]) # 결과 출력

