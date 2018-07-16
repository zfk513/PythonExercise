'''
def get_middle(s):
   return s[(len(s)-1)//2:len(s)//2+1]
'''
def get_middle(s):
    #len(s)=int(len(s))
    return s[((1+len(s))//2)-1] if len(s)%2!=0 else s[(len(s)//2)-1:(len(s)//2)+1]
print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("of"))