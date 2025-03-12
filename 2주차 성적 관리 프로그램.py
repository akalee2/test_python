# 성적 관리 프로그램 알고리즘 
# 2차원 배열 활용해 학생 12345 점수 입력받기
# for문 활용해서 학생들 순서대로 영어,c-언어,파이썬 성적 입력받기
# 입력 받은 걸로 총점, 평균 계산
# 입력 받은 걸로 백분위점수 grade로 변환해 학점
# 총점 높은 순으로 등수 계산

# 5명의 학생, 3개의 과목(영어, C언어, 파이썬)을 위한 2차원 배열 선언
students = [[0] * 3 for _ in range(5)]  # 5명의 학생, 각 학생마다 3개의 과목 성적
results = [[0] * 8 for _ in range(5)]  # 5명의 학생, 번호, 성적, 총점, 평균, 학점, 순위 저장

# 5명의 학생 성적 입력
for i in range(5):
    print(f"{i + 1}번 학생의 성적을 입력해주세요.")
    students[i][0] = int(input("영어 성적: "))
    students[i][1] = int(input("C언어 성적: "))
    students[i][2] = int(input("파이썬 성적: "))

# 각 학생의 총점, 평균, 백분위, 학점 계산
for i in range(5):
    total_score = sum(students[i])  # 각 학생의 총점
    average = total_score / 3  # 평균
    percent = (total_score / 300) * 100  # 백분위 계산
    
    # 학점 계산 (4.5점 만점 기준)
    if percent >= 90:
        grade = 4.5
    elif percent >= 85:
        grade = 4.0
    elif percent >= 80:
        grade = 3.5
    elif percent >= 75:
        grade = 3.0
    elif percent >= 70:
        grade = 2.5
    elif percent >= 65:
        grade = 2.0
    elif percent >= 60:
        grade = 1.5
    else:
        grade = 0.0
    
    # 결과 배열에 학생 번호, 성적, 총점, 평균, 학점, 순위 저장
    results[i][0] = i + 1  # 학생 번호
    results[i][1] = students[i][0]  # 영어 성적
    results[i][2] = students[i][1]  # C언어 성적
    results[i][3] = students[i][2]  # 파이썬 성적
    results[i][4] = total_score  # 총점
    results[i][5] = average  # 평균
    results[i][6] = grade  # 학점

# 총점 높은 순으로 학생 순위 매기기
sorted_results = sorted(enumerate(results), key=lambda x: x[1][4], reverse=True)

# 순위 정보 추가
for rank, (index, _) in enumerate(sorted_results, start=1):
    results[index][7] = rank  # 순위 정보 추가

# 성적 결과 출력
print("\n학생 성적 결과:")
print("학생 번호  영어 성적  C언어 성적  파이썬 성적  총점  평균  학점  순위")
for i in range(5):
    print(f"{results[i][0]:>8}  {results[i][1]:>6}  {results[i][2]:>6}  {results[i][3]:>6}  {results[i][4]:>4}  {results[i][5]:>5.2f}  {results[i][6]:>4.1f} | {results[i][7]:>2}")
