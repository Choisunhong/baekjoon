import sys
input = sys.stdin.readline
from collections import defaultdict

def solution(id_list, report, k):
    unique_report = set()
    for r in report:
        reporter, reported = r.split()
        unique_report.add((reporter, reported))

    # 신고당한 횟수 계산
    report_count = defaultdict(int)
    for reporter, reported in unique_report:
        report_count[reported] += 1

    # 정지된 유저 추출
    banned_users = set()
    for user, count in report_count.items():
        if count >= k:
            banned_users.add(user)

    # 각 유저가 누구를 신고했는지 저장
    report_map = defaultdict(set)
    for reporter, reported in unique_report:
        report_map[reporter].add(reported)

    # 결과 메일 수 계산
    answer = [0] * len(id_list)
    for i, user in enumerate(id_list):
        for reported in report_map[user]:
            if reported in banned_users:
                answer[i] += 1

    return answer
