import os
import random
import datetime
import subprocess

def get_commit_days_for_week(year, week_num):
    # Seed with year and week number so it's consistent for the whole week
    random.seed(f"{year}-{week_num}")
    num_days = random.randint(3, 5)
    days = random.sample(range(7), num_days)
    return set(days)

def make_commit():
    files = ["daily_log.txt", "progress.md", "inspiration.txt"]
    quotes = [
        "Keep pushing forward.",
        "Code never lies, comments sometimes do.",
        "Refactoring is a journey.",
        "Small steps every day.",
        "Consistency is key.",
        "Another day, another bug fixed.",
        "Automating the boring stuff.",
        "Green squares incoming!",
        "Learning and growing.",
        "Just keep coding."
    ]
    
    file_to_mod = random.choice(files)
    quote = random.choice(quotes)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(file_to_mod, "a", encoding="utf-8") as f:
        f.write(f"\n[{now}] {quote}\n")
        
    with open("commit_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now}] Updated {file_to_mod}\n")
        
    subprocess.run(["git", "add", file_to_mod, "commit_log.txt"])
    subprocess.run(["git", "commit", "-m", f"Automated commit: {quote}"])

def main():
    now = datetime.datetime.now()
    year, week_num, weekday = now.isocalendar()
    
    # Reseed with current time for randomizing number of commits during this specific run
    random.seed()
    
    commit_days = get_commit_days_for_week(year, week_num)
    
    # isocalendar weekday is 1-7, range 0-6 matches typical indexing
    if weekday - 1 in commit_days: 
        # Generate between 1 to 5 commits per run (since it runs 3 times a day, total 3-15 per day)
        num_commits = random.randint(1, 5)
        print(f"Today is a commit day! Making {num_commits} commits.")
        for _ in range(num_commits):
            make_commit()
    else:
        print("Today is not a commit day. Resting.")

if __name__ == "__main__":
    main()
