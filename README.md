#  Edit Distance
 
 > Author: \<Joy Haddad ID:862222610\>

## Instructions
 > * Make sure you have Python 3 installed.
 > * Run the script `min_distance.py` using the command:
 > * Enter the two words or strings for which you want to calculate the minimum edit distance when prompted.
 > 
 > # Example user input:
 > * x = "clarks"
 > * y = "kirk"
 > * This will output all the operations and return the minimum edit distance (4)

## Algorithm
The Minimum Edit Distance algorithm utilizes a technique called dynamic programming to determine the smallest number of operations needed to transform one word into another. It achieves this by constructing a chart, which is a two-dimensional matrix. Each cell within the chart corresponds to the minimum edit distance between specific substrings of the two words being compared. The algorithm systematically populates the chart by examining the characters of the two words and identifying the operation with the lowest cost among substitution, deletion, and insertion. By iteratively analyzing each character and updating the corresponding cell in the chart, the algorithm progressively computes the minimum edit distance. Ultimately, the minimum edit distance can be found in the final cell of the chart, representing the overall transformation required to convert one word into the other.
