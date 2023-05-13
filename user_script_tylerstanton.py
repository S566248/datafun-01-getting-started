string1 = input("Please enter movie 1's score:")
string2 = input("Please enter movie 2's score:")
string3 = input("Please enter movie 3's score:")

int1 = int(string1)
int2 = int(string2)
int3 = int(string3)

scores = (int1, int2, int3)

lowest_score = min(scores)
highest_score = max(scores)
total_of_scores = sum(scores)
average_of_scores = round(total_of_scores / len(scores))
product_of_scores = round(int1*int2*int3)
