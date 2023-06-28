def main():
    s= input()
    s2= convert(s)
    print(s2)

def convert(s):
    s = s.replace(":)","🙂")
    s = s.replace(":(","🙁")
    return s

main()