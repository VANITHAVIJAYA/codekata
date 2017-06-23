 def anti_vowel(text):
        vow = ["a", "e", "i", "o", "u"]
        chars = []
        for i in text:
            chars.append(i)
        for i in chars:
            if i.lower() in vow:
                chars.remove(i)
        return "".join(chars)
        a=input("Enter the String:")
        print(anti_vowel(a))
        print(anti_vowel("Hello World"))
