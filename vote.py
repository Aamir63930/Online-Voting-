import matplotlib.pyplot as plt
import pandas as pd
import os

def read_votes_from_csv(file_path, candidates):
    try:
        if not os.path.exists(file_path):
            print(f"❌ Error: The file at '{file_path}' does not exist.")
            return {}

        df = pd.read_csv(file_path)
        if df.empty:
            print("❌ The CSV file is empty.")
            return {}

        print("\n📋 Available columns in the CSV:")
        print(df.columns)

        vote_column = "Choose Your Candidate"  

        if vote_column not in df.columns:
            print(f"❌ Column '{vote_column}' not found in CSV.")
            return {}

        print("\n🔍 Vote column preview:")
        print(df[vote_column].value_counts(dropna=False))


        votes = {candidate.strip().capitalize(): 0 for candidate in candidates}

        for vote in df[vote_column]:
            vote_clean = str(vote).strip().capitalize()
            if vote_clean in votes:
                votes[vote_clean] += 1
            else:
                print(f"⚠️ Invalid vote detected: '{vote}'")

        return votes

    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return {}


def display_results(votes):
    print("\n🗳️ Voting Results:")
    total_votes = sum(votes.values())

    if total_votes == 0:
        print("❌ No votes were cast.")
        return

    for candidate, vote_count in votes.items():
        percentage = (vote_count / total_votes) * 100
        print(f"{candidate}: {vote_count} votes ({percentage:.2f}%)")

    winner = max(votes, key=votes.get)
    print(f"\n🏆 Winner: {winner}")

    labels = list(votes.keys())
    sizes = list(votes.values())
    colors = ['pink', 'gold', 'lightgreen', 'skyblue'][:len(labels)]

    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    plt.title('Voting Results')
    plt.axis('equal')
    plt.show()


def main():
    candidates = ['Aamir', 'Mankameshwar', 'Zaid', 'Devesh']
    file_path = r"C:\\Users\\Aamir Khan\\Downloads\\Voting Form (Responses) - Form responses 1 (4).csv"

    votes = read_votes_from_csv(file_path, candidates)
    display_results(votes)


if __name__ == "__main__":
    main()







