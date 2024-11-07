import bisect

def previous_intervals(I):
    # finding p[j]
    p=[]
    start=[task[0] for task in I]
    finish=[task[1] for task in I]  # this list is sorted
    
    for i in range(len(I)):
        idx=bisect.bisect(finish,start[i])-1
        p.append(idx)
    print("ARRAY P[j] is ",p) 
    # p will look like this [-1, -1, -1, 0, 1, 0, 2, 4]
    return p


def find_solution(j):
    # backtracking
    if j==-1:
        return
    else:
        if( I[j][2]+ compute_opt(p[j]) >= OPT[j-1]):
            O.append(I[j])
            find_solution(p[j])
        else:
            find_solution(j-1)
def compute_opt(j):
    # use recursive formula max(Wj) +OPT(p(j)),opt(j-1)
    if j==-1:
        return 0
    elif (0<=j) and (j<len(OPT)): # reuse the opt values we have computed before
        return OPT[j]
    else:
        return max(I[j][2]+ compute_opt(p[j]),compute_opt(j-1))


def weighted_interval(I):
    #find optimal for each of the subproblem -->opt(j)
    for j in range(len(I)):
        opt_j=compute_opt(j)
        OPT.append(opt_j)   
    print("Optimal Weight Array ",OPT)
    print("Optimal total  weight ",OPT[-1])
    find_solution(len(I)-1)
    return OPT[-1]

if __name__=='__main__':
   #OPT for optimal weight till that interval , O for best jobs to pick

   OPT = []
   O=[]

# jobs-->(start,end,weight)
   t1=(0,3,3)
   t2=(1,4,2)
   t3=(0,5,4)
   t4=(3,6,1)
   t5=(4,7,2)
   t6=(3,9,5)
   t7=(5,10,2)
   t8=(8,10,1)

   I=[t1,t2,t3,t4,t5,t6,t7,t8]

   I.sort(key= lambda tup:tup[1])
   print("Sorted according to the finsih time ",I)
   p=previous_intervals(I)

   optimal_solution=weighted_interval(I)
