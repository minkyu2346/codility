def solution(S, P, Q):
    result=[]
    for i ,v in zip(P,Q):

        new_list= S[i:v+1]
        

        if new_list.find("A")!=-1:

            result.append(1)
            continue

        if new_list.find("C")!=-1:

            result.append(2)
            continue
        if new_list.find("G")!=-1:

            result.append(3)
            continue
        
        else:

            result.append(4)
        
    return result
