
def process_scores(scores):
    print("Average:", sum(scores)/len(scores))
    print("Highest:", max(scores))
    print("Lowest:", min(scores))
scores = list(map(float, input("Enter the scores separated by spaces: ").split()))
process_scores(scores)


