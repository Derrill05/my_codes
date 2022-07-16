# My Mad libs program
print("LET'S ALL HAVE FUN HERE !!\n")
print("Welcome to Mad libs ! Choose your own words and fill them in to create an interesting story. Have fun !!\n ")

#Prompt the user for a number of words that can fill a story
Time = input("Enter the time of the day: ")
Family_Member = input("Family Member: ")
NOUN = input("Enter a noun: ")
Verb = input("Enter a verb: ")
Adjective = input("Enter an adjective: ")
Place = input("Enter a place: ")
Number = input("Enter a number: ")
Adverb = input("Enter an adverb: ")
Noun = input("Enter a noun: ")

#Print your story while filling in the user's inputs
mad_libs = (f"Today I woke up in the {Time} only to find my {Family_Member} playing with my {NOUN}. I tried to kick him out but he {Verb} loudly.I held the {Adjective} boy's hand, took him to a  {Place} and bought him {Number} biscuits to calm him down.He {Adverb} calmed down. End of my {Noun}.")
print(mad_libs)
            
#text to speech output
import gtts

text=mad_libs
tts=gtts.gTTS(mad_libs)
tts.save("mad_libs.mp3")