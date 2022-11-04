def solution(X,Pairs):

	#since max(X) == len(X), min(x) == 1
	# set n = max(X) = len(X)

    n = len(X)
    C = []
    B = []
    for i in range(n):
        #initialise array C for counting keys
		#C indexes correspond to all possible keys within 1..n
        C.append(0)
        B.append(0)
	#O(n)
    
    #start counting
    for i in range(n):
        key = X[i] #(convert to 1-index for my own sanity)
        C[key - 1] += 1 #increment count
    #O(n)
    # will result in array C == [1, 1, 1, 1, 2, 0] for e.g
    #where C[0] gives the count of '1's in array X

    #Create B array to show how many numbers are <= to each value

    for i in range(n):
        B[i] = C[i]

    for i in range(1,n):
        B[i] = B[i] + B[i-1]
    #e.g B => [1,2,3,4,6,6]

    #Given pairs Pairs { (a1,b1), (a2,b2), ... , (an,bn) }
    
    #iterate through pairs

    Z_arr = []

    for pair in Pairs:
        #check left and right boundaries
        count_less_left = 0
        count_less_right = 0
        
        left_key = pair[0]
        right_key = pair[1]
        
        #init Z
        Z = 0

        #consider cases where left_key < 1 and right_key > n
        if left_key < 1:
            #0 or negative, then take right values up to right_key
            count_less_left = 0
                        
            #check right_key, if > n, take all n values
            if right_key > n:
                #means left and right key are both out of bounds, return n
                Z = n
            else:
                count_less_right = B[right_key - 1]
                Z = count_less_right - count_less_left
        
        
        else: #normal case
            #check left key
            count_less_left = B[left_key - 1]
            #check right key
            count_less_right = B[right_key - 1]
            
            Z = count_less_right - count_less_left

            if C[left_key - 1] > 0:
                #if key was in X, add back the count subtracted
                Z += C[left_key - 1]
            
        Z_arr.append(Z)

    print(C)
    print(B)
    print(Pairs)
    print(Z_arr)
    return Z_arr

def main():
    X = [1,2,3,4,5,5,4,2]
    Pairs = [(-1,2), (0,10), (2,6), (3,5)]
    
    solution(X, Pairs)
    X.sort()
    print(X)

if __name__ == "__main__":
    main()
        

       
        

                 
        
        
        
            
     
