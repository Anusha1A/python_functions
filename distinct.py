def solve(s, k):
   i = 0
   ret = []
   mp, to_print = {}, ""
   while i < len(s):
      if i % k == 0 and i != 0:
         ret.append(to_print)
         mp, to_print = {}, ""
      if s[i] not in mp.keys():
         mp[s[i]] = 0
         to_print += s[i]
      i += 1
   ret.append(to_print)
   return ret

s = "aabdddddcghssas"
k = 3
print(solve(s, k))