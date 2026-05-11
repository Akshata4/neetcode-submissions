class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = []
        for i in details:
            if int(i[11:13]) > 60:
                print(i[11:13])
                res.append(i)
        return len(res)