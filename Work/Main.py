# 5kyu The Hashtag Generator

def generate_hashtag(s):
    if s:
        string = '#'+''.join([i.capitalize() for i in s.lstrip().split()])
        if len(string) <= 140:
            return string
        else:
            return False
    else:
        return False