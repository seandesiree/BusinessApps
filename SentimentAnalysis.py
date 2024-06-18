def read_feedback(filename):
    try:
        with open(filename, "r") as file:
            feedback = []
            for line in file:
                comment = line.strip()
                feedback.append(comment)
            return feedback
    except FileNotFoundError:
        []



def categorizer(feedback):
    positive_words = "amazing", "enjoy", "beautiful", "wonderful", "memorable", "excellent", "enlightening", "fantastic"
    negative_words = "bad", "disappointing", "poor", "lackluster"
    good = 0 
    bad = 0

    for item in feedback:
        if any(word in item for word in positive_words):
            good += 1
        elif any(word in item for word in negative_words): 
            bad += 1
        
    return good, bad



def main():
    feedback = read_feedback("travelblogentries.txt")
    if not feedback:
        print("No feedback available." )
        return
    else:
        print(categorizer(feedback))

main()
