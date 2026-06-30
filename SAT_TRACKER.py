#SAT_STUDY_TRACKER



import csv

choice = 0

while choice != 6:

    print("\n===== SAT STUDY TRACKER =====")
    print("1. Add Study Record")
    print("2. Add Practice Test")
    print("3. View Study Records")
    print("4. View Practice Test Scores")
    print("5. Analyze Scores")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        date = input("Enter Date: ")
        hours = input("Enter Study Hours: ")
        subject = input("Enter Subject: ")
        topics = input("Enter Topics Learned: ")

        f = open("study.csv", "a", newline="")
        writer = csv.writer(f)

        writer.writerow([date, hours, subject, topics])

        f.close()

        print("Study record added.")

    elif choice == 2:

        date = input("Enter Practice Test Date: ")
        score = int(input("Enter Score: "))

        f = open("practice.csv", "a", newline="")
        writer = csv.writer(f)

        writer.writerow([date, score])

        f.close()

        print("Practice test added.")

    elif choice == 3:

        f = open("study.csv", "r")
        reader = csv.reader(f)

        print("\nDate\tHours\tSubject\tTopics")

        for row in reader:
            print(row)

        f.close()

    elif choice == 4:

        f = open("practice.csv", "r")
        reader = csv.reader(f)

        print("\nDate\tScore")

        for row in reader:
            print(row)

        f.close()

    elif choice == 5:

        scores = []
        dates = []

        f = open("practice.csv", "r")
        reader = csv.reader(f)

        for row in reader:
            dates.append(row[0])
            scores.append(int(row[1]))

        f.close()

        latest_score = scores[-1]
        latest_date = dates[-1]
        best_score = max(scores)

        print("\nLatest Test Date:", latest_date)
        print("Latest Score:", latest_score)
        print("Best Score:", best_score)

        if len(scores) == 1:
            print("Only one test available.")

        else:

            previous_best = max(scores[:-1])

            if latest_score > previous_best:
                print("Latest score is better than all previous scores.")

            elif latest_score == previous_best:
                print("Latest score is equal to the previous best score.")

            else:
                print("Latest score is lower than the previous best score.")

    elif choice == 6:

        print("Thank You!")

    else:

        print("Invalid Choice")