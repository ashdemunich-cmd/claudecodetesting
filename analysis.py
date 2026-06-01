import statistics

scores = {
    "Alice": 92,
    "Bob": 78,
    "Charlie": 85,
    "Diana": 95,
    "Ethan": 61,
    "Fiona": 73,
    "George": 88,
    "Hannah": 54,
    "Ivan": 79,
    "Julia": 91,
    "Kevin": 67,
    "Laura": 83,
    "Mike": 70,
    "Nina": 96,
    "Oscar": 58,
}

values = list(scores.values())

print("=== Test Score Analysis ===\n")

print(f"Students:   {len(values)}")
print(f"Mean:       {statistics.mean(values):.1f}")
print(f"Median:     {statistics.median(values):.1f}")
print(f"Std Dev:    {statistics.stdev(values):.1f}")
print(f"High:       {max(values)}  ({max(scores, key=scores.get)})")
print(f"Low:        {min(values)}  ({min(scores, key=scores.get)})")

print("\n=== Grade Distribution ===\n")

def letter_grade(score):
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"

buckets = {"A": [], "B": [], "C": [], "D": [], "F": []}
for name, score in scores.items():
    buckets[letter_grade(score)].append(name)

for grade, students in buckets.items():
    bar = "#" * len(students)
    print(f"  {grade}  {bar:<15} {len(students)} student(s): {', '.join(students) if students else '-'}")

print("\n=== Passing vs Failing ===\n")

passing = [(n, s) for n, s in scores.items() if s >= 60]
failing = [(n, s) for n, s in scores.items() if s < 60]

print(f"  Passing (>=60): {len(passing)}")
print(f"  Failing  (<60): {len(failing)}")
if failing:
    print(f"  At risk: {', '.join(n for n, _ in failing)}")
