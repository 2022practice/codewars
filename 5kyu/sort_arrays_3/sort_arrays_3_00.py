def sort_me(courses): 
    courses = [ s.split('-') for s in courses ]
    courses_sorted = sorted(courses, key=lambda l: (l[1],l[0]))
    l = ['-'.join(elem) for elem in courses_sorted]
    return l



assert sort_me(['aeb-1305', 'site-1305', 'play-1215', 'web-1304', 'site-1304', 'beb-1305']) == ["play-1215", "site-1304", "web-1304", "aeb-1305", "beb-1305", "site-1305"]

