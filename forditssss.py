#szeretem a hunglish kodolas stilust
#készítette: Zolimester
class EnchantmentTranslator:
    letters = {
    "a": "ᔑ",
    "b": "ʖ",
    "c": "ᓵ",
    "d": "↸",
    "e": "ᒷ",
    "f": "⎓",
    "g": "⊣",
    "h": "⍑",
    "i": "╎",
    "j": "⋮",
    "k": "ꖌ",
    "l": "ꖎ",
    "m": "ᒲ",
    "n": "リ",
    "o": "𝙹",
    "p": "!¡",
    "q": "ᑑ",
    "r": "∷",
    "s": "ᓭ",
    "t": "ℸ",
    "u": "⚍",
    "v": "⍊",
    "w": "∴",
    "x": "̇/",
    "y": "||",
    "z": "⨅"
}

    @classmethod
    def translate(cls, text):
        fordit = ""
        for char in text:
            fordit += cls.letters.get(char.lower(), char) + " "  
        return fordit.strip()

input_text = input("Írj szöveget: ")
fordit = EnchantmentTranslator.translate(input_text)
print("Fordítás:", fordit)
