subl = ''
i = 0
if not s:
    print('')
elif len(s) == 1:
    print(s)
else:
    while 0 <= i < len(s):
        curr = s[i]
        subt = s[i]
        for j in range(i + 1, len(s)):
            if s[j] >= curr:
                subt += s[j]
                curr = s[j]
            else:
                break
        if len(subl) < len(subt):
            subl = subt
        i = j
        if len(s[i:]) <= len(subl):
            break
print(subl)
