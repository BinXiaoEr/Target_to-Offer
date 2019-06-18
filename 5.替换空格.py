def replace_bank(strs):
    new_strs=[]
    for i in range(len(strs)):
        if strs[i]==' ':
            # strs[i]='%20'
            new_strs.append('%20')
        else:
            new_strs.append(strs[i])
    print(''.join(new_strs))


replace_bank('we are happy')