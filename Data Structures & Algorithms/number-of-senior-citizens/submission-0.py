class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for index in range(len(details)):
            phone, gender, age, seat = details[index][0:10], details[index][10:11], details[index][11:13], details[index][13:]
            if int(age) > 60:
                cnt += 1
        return cnt
