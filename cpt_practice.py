all_zodiacs = ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"]
capricorn_traits = ["Resourceful", "Reliable", "Resilient", "Diciplined", "Ambitious"]
aquarius_traits = ["Intellectual", "Innovative", "Open-minded", "Witty", "Humanitarian"]
pisces_traits = ["Compassionate", "Empathetic", "Creative", "Gentle", "Selfless"]
aries_traits = ["Courageous", "Honest", "Determined", "Passionate", "Independant"]
taurus_traits = ["Patient", "Loyal", "Hardworking", "Grounded", "Appreciative"]
gemini_traits = ["Adaptable", "Eloquent", "Curious", "Quick-witted", "Versatile"]
cancer_traits = ["Devoted", "Creative", "Nurturing", "Intuitive", "Tenacious"]
leo_traits = ["Bold", "Generous", "Faithful", "Authoritative", "Enthusiastic"]
virgo_traits = ["Meticulous", "Helpful", "Diligent", "Sympathetic", "Humble"]
libra_traits = ["Artistic", "Clever", "Charming", "Social", "Gracious"]
scorpio_traits = ["Strategic", "Alluring", "Mysterious", "Perceptive", "Ardent"]
sagittarius_traits = ["Adventerous", "Funny", "Honest", "Enthusiastic", "Idealistic"]


# I was struggling a lot on how to get month and date to ask properly and leave room for other things I needed to incorporate
while True:
    month = input("What month is your birthday: ").strip().lower()   
    date = int(input("What day of the month is your birthday?(1-31): "))


    

# I was trying, but did not think there was a way to incorporate parameters in this function
def zodiac_sign():
    while True:
        if  month == ("january" or "february" or "march" or "april" or "may" or "june" or "july" or "september" or "october" or "november" or "december") and date <= 31:
            while True:
                if month == "december" and date >= 22 or month == "january" and date <= 19:
                    return "You are a Capricorn!"
                elif month == "january" and date >= 20 or month == "february" and date <= 18:
                    return "You are an Aquarius"
                elif month == "february" and date >= 19 and date <= 29 or month == "march" and date <= 20:
                    return "You are a Pisces"
                elif month == "march" and date >= 21 or month == "april" and date <= 19:
                    return "You are an Aries"
                elif month == "april" and date >= 20 or month == "may" and date <= 20:
                    return "You are a Taurus"














    

    




