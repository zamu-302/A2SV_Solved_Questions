class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        seen=defaultdict(int)
        res=[]
        for domain in cpdomains:
            count,dom=domain.split()
            count=int(count)
            seen[dom]+=count
            pos=dom.find('.')+1
            while pos>0:
                seen[dom[pos:]]+=count
                pos=dom.find('.',pos)+1
        for dom,count in seen.items():
            res.append(f'{count} {dom}')
        return res

        