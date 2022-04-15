def generate_hashtag(s):
    s_ = '#'+ ''.join([w.capitalize() for w in s.split()])
    if len(s_) > 140 or not s :
        return False
    return s_
