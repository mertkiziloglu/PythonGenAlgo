
import numpy as np

#if Ask for sequences from the user
#sequence_1 = input("Enter or paste sequence 1:")
#sequence_2 = input("Enter or paste sequence 2:")

sequence_1 = "ATTCTTA"
sequence_2 = "TTTCT"

#Create Matrices
main_matrix = np.zeros((len(sequence_1)+1,len(sequence_2)+1))   #Create a matrix with the size of the sequences
match_checker_matrix = np.zeros((len(sequence_1),len(sequence_2)))

# Providing the scores for match ,mismatch and gap_penalty
match = 1
mismatch = -1
gap_penalty = -2

#Fill the match checker matrix accrording to match or mismatch
for i in range(len(sequence_1)):
    for j in range(len(sequence_2)):
        if sequence_1[i] == sequence_2[j]:
            match_checker_matrix[i][j]= match
        else:
            match_checker_matrix[i][j]= mismatch

#print(match_checker_matrix)

#Filling up the matrix using Needleman_Wunsch algorithm
#STEP 1 : Initialisation
for i in range(len(sequence_1)+1):
    main_matrix[i][0] = i*gap_penalty
for j in range(len(sequence_2)+1):
    main_matrix[0][j] = j * gap_penalty

#STEP 2 : Matrix Filling
for i in range(1,len(sequence_1)+1):
    for j in range(1,len(sequence_2)+1):
        main_matrix[i][j] = max(main_matrix[i-1][j-1]+match_checker_matrix[i-1][j-1],
                                main_matrix[i-1][j]+gap_penalty,
                                main_matrix[i][j-1]+ gap_penalty)

print(main_matrix)

# STEP 3 : Traceback

aligned_1 = ""
aligned_2 = ""

sequence_len = len(sequence_1)
sequence2_len = len(sequence_2)

while(sequence_len > 0 and sequence2_len > 0):

    if (sequence_len >0 and sequence2_len > 0 and main_matrix[sequence_len][sequence2_len] == main_matrix[sequence_len - 1][sequence2_len - 1]+ match_checker_matrix[sequence_len - 1][sequence2_len - 1]):

        aligned_1 = sequence_1[sequence_len - 1] + aligned_1
        aligned_2 = sequence_2[sequence2_len - 1] + aligned_2

        sequence_len = sequence_len - 1
        sequence2_len = sequence2_len - 1
    
    elif(sequence_len > 0 and main_matrix[sequence_len][sequence2_len] == main_matrix[sequence_len - 1][sequence2_len] + gap_penalty):
        aligned_1 = sequence_1[sequence_len - 1] + aligned_1
        aligned_2 = "-" + aligned_2

        sequence_len = sequence_len - 1
    else:
        aligned_1 = "-" + aligned_1
        aligned_2 = sequence_2[sequence2_len - 1] + aligned_2

        sequence2_len = sequence2_len - 1

#test
print(aligned_1)
print(aligned_2)

# Working :)