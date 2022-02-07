def solution(A, B, K):
    
    RE = divmod(B,K)[0]
    
    
    div= divmod(A,K)
    if div[1]==0:
        C= div[0]-1
    else: 
        C= div[0]

        
    return RE-C
