import random
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

resume = "resume"


def zodiac_sign_function():
    zodiac_sign = input("Please enter your zodiac sign: ").strip().lower()
    return zodiac_sign

def zodiac_sign_checker():
    while True:
        if zodiac_sign == "capricorn" or "aquarius" or "pisces" or "aries" or "taurus" or "gemini" or "cancer" or "leo" or "virgo" or "libra" or "scorpio" or "sagittarius":
            return input(f"If you would like to see a few traits of this star sign, please type yes: ")




    
