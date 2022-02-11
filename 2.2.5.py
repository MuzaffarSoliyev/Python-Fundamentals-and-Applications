import datetime

year, month, day = map(int, input().strip().split())
days = int(input())
result = datetime.datetime(year, month, day) + datetime.timedelta(days=days)
print(result.year, result.month, result.day)
