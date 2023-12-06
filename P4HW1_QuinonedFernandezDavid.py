# CTI-110
# P4HW1 - Score List
# Quinonez Fernandez,David
# 11/12/2023

# Function to calculate letter grade based on average score
def calculate_letter_grade(average_score):
    if average_score >= 90:
        return 'A'
    elif 80 <= average_score < 90:
        return 'B'
    elif 70 <= average_score < 80:
        return 'C'
    elif 60 <= average_score < 70:
        return 'D'
    else:
        return 'F'

# Main function
def main():
    # Prompt user for the number of scores
    num_scores = int(input("Enter the number of scores you would like to enter: "))

    # Initialize an empty list to store scores
    score_list = []

    # Loop to collect scores
    for i in range(num_scores):
        valid_score = False
        
        # Loop until a valid score is entered
        while not valid_score:
            try:
                # Ask for a score and attempt to convert to float
                score = float(input(f"Enter score #{i + 1}: "))
                
                # Check if the score is valid (between 0 and 100)
                if 0 <= score <= 100:
                    valid_score = True
                    
                else:
                    print()
                    print("INVALID score entered!!!")
                    print("Score should be between 0 and 100.")
                    
                    score = float(input(f"Enter score #{i + 1} again: "))
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
            


        # Add the valid score to the list
        score_list.append(score)
        
    print()        
    print("--------------Results-----------")

    # Display the lowest score
    lowest_score = min(score_list)
    print(f"Lowest score  : {lowest_score}")

    # Remove the lowest score from the list
    score_list.remove(lowest_score)

    # Display the score list after dropping the lowest score
    print("Modified List :", score_list)

    # Calculate the average of scores in the modified list
    average_score = sum(score_list) / len(score_list)
    print(f"Scores Average: {average_score:.2f}")

    # Determine and display the letter grade for the calculated average
    letter_grade = calculate_letter_grade(average_score)
    print(f"Grade         : {letter_grade}")

# Call the main function
if __name__ == "__main__":
    main()
    
print("-" * 35)
