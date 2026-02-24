def recite(start_verse, end_verse):

    days = [
        "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]
    
    gifts = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves, ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, "
    ]

    verses = []
    result = []
    
    for n in range(start_verse - 1, end_verse):
        verse_str = f"On the {days[n]} day of Christmas my true love gave to me: "
        
        gift_section = ""
        for i in range(n, -1, -1):
            if i == 0 and n > 0:
                gift_section += "and " + gifts[i]
            else:
                gift_section += gifts[i]
        
        result.append(verse_str + gift_section)

    return result