#Adam Jones

 # 24 NOV 2025

  # P4HW1 

  # this assignments allows person to input 3 grades

import bisect

scores = []
num_scores = int(input("How many scores will you enter (up to 100): "))

# --- Input (no IF statements, only WHILE loops) ---
for i in range(1, num_scores + 1):
    score = float(input(f"Enter score {i}: "))
    
    # Repeat until score is non-negative (allowed because WHILE ≠ IF)
    while score < 0:
        print("Score cannot be negative. Please try again.")
        score = float(input(f"Enter score {i}: "))
    
    scores.append(score)

# --- Lowest score ---
lowest = min(scores)

# --- Modified list (remove ONE lowest value) ---
modified_scores = scores.copy()
modified_scores.remove(lowest)

# --- Average ---
average = sum(modified_scores) / len(modified_scores)

# --- Letter grade (NO IF STATEMENTS!) ---
# Use bisect to locate grade by numeric threshold
boundaries = [60, 70, 80, 90]        # cutoff points
grades = ["F", "D", "C", "B", "A"]   # mapped results

index = bisect.bisect(boundaries, average)
grade = grades[index]

print("-------Results-------")
print("\nResults:")
print("Lowest score:", lowest)
print("Modified list:", modified_scores)
print("Scores average:", format(average, ".2f"))
print("Grade:", grade)


      
