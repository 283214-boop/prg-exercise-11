from sorting import random_numbers

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        x = self.scores[index]
        if x >= 90:
            return "A"
        elif x >= 80:
            return "B"
        elif x >= 70:
            return "C"
        elif x >= 60:
            return "D"
        elif x >= 50:
            return "E"
        else:
            x >= 0
            return "F"

    def find(self, score):
        found_indexes = []
        for i in range(len(self.scores)):
           if self.scores[i] == score:
               found_indexes.append(i)
        return found_indexes

    def get_sorted(self):
        scores_copy = self.scores.copy()
        n = len(scores_copy)
        for i in range(n):
            for j in range(0, n - i - 1):
                if scores_copy[j] > scores_copy[j + 1]:
                    scores_copy[j], scores_copy[j + 1] = scores_copy[j + 1], scores_copy[j]
        return scores_copy

def main():
    results = StudentsGrades( [85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(f"Počet studentů: {results.count()}")
    print("=*" * 30)
    for i in range(results.count()):
        bodiky = results.get_by_index(i)
        znamecky = results.get_grade(i)
        print(f"Student {i}: {bodiky} points - {znamecky}")
    print("=*" * 30)
    perfect_scores = results.find(100)
    print(f"Indexy studentů s plným počtem bodů: {perfect_scores}")
    print(f"Seřazené výsledky: {results.get_sorted()}")
    print("\n--- TEST S NÁHODNÝMI DATY ---")
    nahodna_data = random_numbers(30, 0, 100)
    random_results = StudentsGrades(nahodna_data)
    print(f"Počet náhodných studentů: {random_results.count()}")
    print(f"Seřazené náhodné výsledky: {random_results.get_sorted()}")




if __name__=="__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(results.count())  # 9
    print(results.get_by_index(2))  # 91
    print(results.scores)
    print(results.get_grade(2))  # A (91 bodů)
    print(results.get_grade(6))  # A (100 bodů)
    print(results.get_grade(7))  # F (38 bodů)
    print(results.find(100))  # [6]
    print(results.find(50))  # [4]
    print(results.find(77))  # []
    print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny
    print(main())
