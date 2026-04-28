class DSU:
    def __init__(self, n):
        self.parent = [index for index in range(n)]
        self.rank = [1 for index in range(n)]

    def findParent(self, child):
        if child != self.parent[child]:
            self.parent[child] = self.findParent(self.parent[child])
        return self.parent[child]

    def union(self, child1, child2):
        parent1, parent2 = self.findParent(child1), self.findParent(child2)
        if parent1 == parent2:
            return 0
        else:
            if self.rank[parent1] > self.rank[parent2]:
                self.rank[parent1] += self.rank[parent2]
                self.parent[parent2] = parent1
            else:
                self.rank[parent2] += self.rank[parent1]
                self.parent[parent1] = parent2
            return 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU(len(accounts))
        mail_id_map = defaultdict(int)
        for index in range(len(accounts)):
            name, emails = accounts[index][0], accounts[index][1:]
            for email in emails:
                if email in mail_id_map and mail_id_map[email] != index:
                    dsu.union(index, mail_id_map[email])
                else:
                    mail_id_map[email] = index

        mails_per_account = [[] for index in range(len(accounts))]
        for mail, parent in mail_id_map.items():
            mails_per_account[dsu.findParent(parent)].append(mail)


        print(mails_per_account)

        result_list = []
        for index in range(len(accounts)):
            if mails_per_account[index]:
                tmp = [accounts[index][0]]
                mails_per_account[index].sort()
                tmp.extend(mails_per_account[index])
                result_list.append(tmp)

        return result_list




        
        

            



        