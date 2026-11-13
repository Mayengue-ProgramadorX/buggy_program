# buggy_program.py — Contains 4 bugs. Find and fix them all.

def calculate_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    
    above_average = []
    for num in numbers:
        if num > average:
            above_average.append(num)
    
    return {
        "total": total,
        "average": average,
        "above_average": above_average,
        "above_count": len(above_average)
    }

scores = [85, 92, 78, 95, 88, "70", 93]

new_scores = [] #to store the newly converted scores
#For convert str to int
for score in scores:
    new_scores.append(int(score)) #it will convert and add it to the new score list

result = calculate_stats(new_scores)

print(f"Total: {result['total']}")
print(f"Average: {result['average']}")
print(f"Above average: {result['above_count']} scores")
