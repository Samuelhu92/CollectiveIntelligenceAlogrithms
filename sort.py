def short_bubble_sort(a_list):
    exchanges=True
    pass_num=len(a_list)-1
    while pass_num>0 and exchanges:
        exchanges=False
        for i in range(pass_num):
            if a_list[i]>a_list[i+1]:
                exchanges=True
                a_list[i],a_list[i+1]=a_list[i+1],a_list[i]
        pass_num-=1

def selection_sort(a_list):
    for fill_slot in range(len(a_list)-1,0,-1):
        pos_of_max=0
        for location in range(1,fill_slot):
            if a_list[location]>a_list[pos_of_max]:
               pos_of_max=location
        a_list[fill_slot],a_list[pos_of_max]=a_list[pos_of_max],a_list[fill_slot]

def insertion_sort(a_list):
    for index in range(1,a_list):
        current_value=a_list[index]
        position=index
        low=0
        high=index-1
        while low<=high:
            mid=(low+high)/2
            if a_list[mid]<a_list[position]:
                low=mid+1
            else:
                high=mid-1
        while position > low:
            a_list[position]=a_list[position-1]
            position=position-1
        a_list[position]=current_value

def merge_sort(a_list):
    print('Splitting', a_list)
    if len(a_list)>1:
        mid=len(a_list)//2
        left_half=a_list[:mid]
        right_half=a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i=0;j=0;k=0;
        while i<len(left_half) and j<len(right_half):
            if left_half[i]<right_half[j]:
                a_list[k]=left_half[i]
                i+=1
            else:
                a_list[k]=right_half[j]
                j+=1
            k+=1
        while i<len(left_half):
            a_list[k]=left_half[i]
            i+=1
            k+=1
        while j<len(right_half):
            a_list[k]=right_half[j]
            j+=1
            k+=1
    print('Merging', a_list)

def quick_sort(a_list):
    quick_sort_helper(a_list,0,len(a_list)-1)

def quick_sort_helper(a_list,first,last):
    if first<last:
        split_point=partition(a_list,first,last)
        quick_sort_helper(a_list,first,split_point-1)
        quick_sort_helper(a_list,split_point+1,last)

def partition(a_list,first,last):
    pivot_value=a_list[first]
    left_mark=fisrt+1
    right_mark=last
    done=False
    while not done:
        while left_mark<=right_mark and a_list[left_mark]<=pivot_value:
            left_mark+=1
        while a_list[right_mark]>=pivot_value and right_mark >=left_mark:
            right_mark-=1
        if right_mark<left_mark:
            done=True
        else:
            temp=a_list[left_mark]
            a_list[left_mark]=a_list[right_mark]
            a_list[right_mark]=temp
    temp=a_list[first]
    a_list[first]=a_list[right_mark]
    a_list[right_mark]=temp
    return right_mark

def qsort(a_list):
    if len(a_list)<=1:
        return a_list
    else:
        pivot=a_list[0]
        return qsort([x for x in a_list[1:] if x<pivot])+[pivot]+qsort([x for x in a_list[1:] if x>=pivot])

def topSort(G):
    #Basically locate the node that has zero in-degree so that we could remove the node 
    #with no anymore operations. then we put it before the rest 
    count=dict((u,0) for u in G)
    for u in G:
        for v in G[u]:
            count[v]+=1
    Q=[u for u in G if count[u]==0]
    S=[]
    while Q:
        u=Q.pop()
        S.append(u)
        for v in G[u]:
            count[v]-=1
            if count[v]==0:
                Q.append(v)
    return S
 
def walk(G,s,S):
    P,Q=dict(),set()
    P[s]=None
    Q.add(s)
    while Q:
        u=Q.pop()
        for v in G[u].difference(P,S):
            Q.add(v)
            P[v]=u
def eulaWalk(G):
    #first of all check whether the graphy has euler circuit 
    for u in G:
        if len(list(G[u]))%2 ==1:
            return None

    P,Q,R=dict(),set(),dict()
    P[s]=None
    Q.add(s)
    while Q:
        u=Q.pop()

def components(G):
    comp=[]
    seen=set()
    for u in G:
        if u in seen: continue
        C=walk(G,u)
        seen.update(u)
        comp.append(C)
    return comp

#A straightforward method to find kth smallest number in a list
def partition(seq):
    pi,seq=seq[0],seq[1:]
    lo=[x for x in seq if x<pi]
    hi=[x for x in seq if x>pi]
    return pi,lo,hi

def select(seq,k):
    pi,lo,hi=partition(seq)
    m=len(lo)
    if m==k:return pi
    elif k<m:
        return select(lo,k)
    else:
        return select(hi,k-m-1)

def mergesort(seq):
    mid=len(seq)//2
    left=seq[:mid]
    right=seq[mid:]
    if len(left)>1: mergesort(left)
    if len(right)>1: mergesort(right)
    res=[]
    while left and right:
        if left[-1]>=right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()
    return (left or right) + res




