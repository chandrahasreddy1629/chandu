list = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,100,100],
    [21,22,23,100,100]
]
n = len(list)

max = list[0][0]+ list[0][1] + list[1][0]  + list[1][1]
for i in range(0,n-1) :
    for j in range(0,n-1):
         if(list[i][j] + list[i][j+1] + list[i+1][j] + list[i+1][j+1] > max):
            max = list[i][j] + list[i][j+1] + list[i+1][j] + list[i+1][j+1]        
print(max)
            


        
            
            
