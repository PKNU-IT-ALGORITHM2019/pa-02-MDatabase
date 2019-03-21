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
        length[0]-=LOL
        used.pop()
    
 

    if len(used) is N:
        LOL= LBP(locations[used[0]],locations[used[N-1]]) #Legnth of Locations        
        length[0]+=LOL
        if length[1] is None:
            del route[:]
            for i in range(N):
                route.append(used[i])

            length[1]=length[0]
        elif length[1] >length[0]:
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
for i in range(N):
    #if i is 0:
        result=tour(i,used,length,route)
        used.pop()
 #   elif result_temp
 #   else:
  #      result_temp= tour(i,used,length,route)
   #     used.pop()
   #     if result> result_temp:
   #         result=result_temp





print(route,length[1])

#print(LBP(locations[0],locations[1])) # test of LBP = sucess



#print(locations)