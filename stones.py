def solve_stones(r1, b1, r2, b2):
    dp = {}
    
    def optimal_play(r1, b1, r2, b2, alice_is_a):
        if r1 == 0 or b1 == 0:  
            return 0.0
        if r2 == 0 or b2 == 0:  
            return 1.0
            
        state = (r1, b1, r2, b2, alice_is_a)
        if state in dp:
            return dp[state]
        

        if alice_is_a:
           
            max_prob = 0.0
          
            for p in range(101):
                p_red = p / 100.0
                p_blue = 1.0 - p_red
                
              
                prob_if_guess_red = (
                    p_red * optimal_play(r1-1, b1, r2, b2, False) +  
                    p_blue * optimal_play(r1, b1, r2-1, b2, False)  
                )
                
                
                prob_if_guess_blue = (
                    p_red * optimal_play(r1, b1, r2, b2-1, False) + 
                    p_blue * optimal_play(r1, b1-1, r2, b2, False)   
                )
                
                
                prob = min(prob_if_guess_red, prob_if_guess_blue)
                max_prob = max(max_prob, prob)
                
        else:
        
            min_prob = 1.0
         
            for p in range(101):
                p_red = p / 100.0
                p_blue = 1.0 - p_red
                
             
                prob_if_guess_red = (
                    p_red * optimal_play(r1, b1, r2-1, b2, True) + 
                    p_blue * optimal_play(r1-1, b1, r2, b2, True)   
                )
                
                
                prob_if_guess_blue = (
                    p_red * optimal_play(r1, b1-1, r2, b2, True) + 
                    p_blue * optimal_play(r1, b1, r2, b2-1, True)   
                )
                
                
                prob = max(prob_if_guess_red, prob_if_guess_blue)
                min_prob = min(min_prob, prob)
            
            max_prob = min_prob
            
        dp[state] = max_prob
        return max_prob
    
    return optimal_play(r1, b1, r2, b2, True)


print(f"{solve_stones(1,1,1,1):.6f}")  
print(f"{solve_stones(1,2,3,4):.6f}")  