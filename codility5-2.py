def solution(A, B, K):
    
    B_Div = divmod(B,K)[0]
    
    
    A_div= divmod(A,K)
    if A_div[1]==0:
        A_Div_new= div[0]-1
    else: 
        A_Div_new= div[0]

        
    return B_Div-A_Div_new
