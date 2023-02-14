# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:16:45 2023

@author: Vinicius Marques Regitano
"""
from numba import njit
import numpy as np

@njit
def egg_dropping_fill_matrix(n_floors, n_eggs):
    
    egg_trials_matrix = np.zeros((n_floors +1, n_eggs +1 ))
    
    for floors in range(n_floors +1):
        for eggs in range(n_eggs+1):
        
        
            
            # Basic cases: 
            #     - Cases we have 0 egg we'll need no (0) trial
            #     - Cases we have 1 egg left we'll need the number of floors of trials
            #     - Cases we have 1 floor left we'll need 1 more trial
                        
            if eggs == 0:
                egg_trials_matrix[0][eggs] = 0
                continue
            
            elif eggs == 1:
                egg_trials_matrix[floors][1] = floors
                continue
            
            elif floors == 1:
                egg_trials_matrix[1][eggs] = 1
                continue
                
            # If no basic cases, we'll fill the matrix calculating the elements using the previous calculated elements
            # In order to already have the elements calculated, we need to calculate from top-left to bottom-right
            
            else:
                
                # An out of range possible number of trials
                egg_trials_matrix[floors][eggs] = n_floors + 1
                    
                for possible_floor in range(floors):
                    
                    case_egg_breaks = egg_trials_matrix[possible_floor-1][eggs-1] + 1
                    
                    case_egg_non_break= egg_trials_matrix[floors-possible_floor][eggs] + 1
                    
                    possible_number_trials = max(case_egg_breaks, case_egg_non_break)
                    
                    egg_trials_matrix[floors][eggs] = min(egg_trials_matrix[floors][eggs], possible_number_trials)
                    
                
    return egg_trials_matrix



if __name__=="__main__":
    
    trials_102_2 = egg_dropping_fill_matrix(102, 2)
    
    trials_2022_10 = egg_dropping_fill_matrix(2022, 10)
    
    print("Minimum quantity trial for a 102 building with 2 eggs is: {}\n".format(trials_102_2[102][2]))
    
    print("Minimum quantity trial for a 2022 building with 10 eggs is: {}\n".format(trials_2022_10[2022][10]))
    
    print("For example, the matrix of floors x eggs of minimum trials for the 102 building and 2 eggs is:")
    print("0 egg, 1 egg, 2 eggs\n", trials_102_2)
    
