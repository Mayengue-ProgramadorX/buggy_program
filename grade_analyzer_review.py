scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]


def get_statistics(scores):
    """Calculate total, average, highest, and lowest scores."""

    if not scores:
        return None

    return {
        "total_scores": len(scores),
        "average": sum(scores) / len(scores),
        "highest": max(scores),
        "lowest": min(scores)
    }


def passing_failing(scores):
    """Count passing and failing scores."""

    passing = sum(score >= 60 for score in scores)

    return {
        "passing": passing,
        "failing": len(scores) - passing
    }


def grade_distribution(scores):
    """Count grades using a dictionary."""

    grades = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0
    }

    for score in scores:

        if score >= 90:
            grades["A"] += 1

        elif score >= 80:
            grades["B"] += 1

        elif score >= 70:
            grades["C"] += 1

        elif score >= 60:
            grades["D"] += 1

        else:
            grades["F"] += 1

    return grades


def display_report(scores):
    """Display the complete report."""

    stats = get_statistics(scores)

    if stats is None:
        print("No scores available.")
        return

    results = passing_failing(scores)
    grades = grade_distribution(scores)

    total = stats["total_scores"]

    print("\n=== Grade Analyzer ===")

    print(f"Total Scores: {total}")
    print(f"Average: {stats['average']:.1f}")
    print(f"Highest: {stats['highest']}")
    print(f"Lowest: {stats['lowest']}")

    print()

    print(
        f"Passing: {results['passing']} "
        f"({(results['passing'] / total) * 100:.1f}%)"
    )

    print(
        f"Failing: {results['failing']} "
        f"({(results['failing'] / total) * 100:.1f}%)"
    )

    print()

    print("Grade Distribution:")
    print(f"A: {grades['A']} students")
    print(f"B: {grades['B']} students")
    print(f"C: {grades['C']} students")
    print(f"D: {grades['D']} students")
    print(f"F: {grades['F']} students")


def add_scores(scores):
    """Allow the user to add new scores."""

    print("\n--- Add More Scores ---")

    while True:

        user_input = input(
            "Enter a score or type 'done' to finish: "
        ).strip()

        if user_input.lower() == "done":
            break

        try:
            new_score = int(user_input)

            # Validate range
            if not 0 <= new_score <= 100:
                print("Score must be between 0 and 100.")
                continue

            scores.append(new_score)

            print("\nScore added successfully!")

            # Recalculate and display updated report
            display_report(scores)

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():

    display_report(scores)

    add_scores(scores)


if __name__ == "__main__":
    main()