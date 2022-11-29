def generate_hashtag(s):
    s = s.title()
    s = s.split()
    s = ''.join(s)
    s = f"#{s}"
    if len(s) > 140 :
        return False
    return s


print(generate_hashtag('c i n   '))
# '#CodewarsIsNice'
