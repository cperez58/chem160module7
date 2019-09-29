def palind2(s):
    alist=list(s)
    alist.reverse()
    revs="".join(alist)
    if revs==s:
        return True
    return False
print(palind2("ratsliveonoevilstar"))
print(palind2("abcdedcaba"))
