import random

def main():
    print("🔮 Welcome to Ritesh Baindara's Fortune Teller (21JE0770) 🔮")
    
    mood = input("How are you feeling today? (happy/sad/neutral/excited/stressed/confused): ").lower()
    
    happy_fortunes = [
    "✨ Your fortune: Joy follows you like sunshine, Ritesh Baindara! Embrace the day. ✨",
    "✨ Your fortune: Laughter will open new doors for you today,. ✨",
    "✨ Your fortune: The universe dances to your happy rhythm✨"
    ]

    sad_fortunes = [
        "✨ Your fortune: Storms do not last forever, Ritesh Baindara. A rainbow is near. ✨",
        "✨ Your fortune: Even the moon needs darkness to glow — stay strong. ✨",
        "✨ Your fortune: One small spark of hope can light up your entire path. ✨"
    ]

    neutral_fortunes = [
        "✨ Your fortune: Stillness brings clarity — trust your calm mind. ✨",
        "✨ Your fortune: Today holds quiet wisdom. Be open to what it teaches you. ✨",
        "✨ Your fortune: You are aligned with balance — something unexpected yet good awaits, Ritesh Baindara. ✨"
    ]

    excited_fortunes = [
    "✨ Your fortune: Let your excitement fuel bold action today, Ritesh Baindara! ✨",
    "✨ Your fortune: The spark within you, Ritesh Baindara, will light up others' lives. ✨",
    "✨ Your fortune: Your passion is contagious — amazing things are just ahead! ✨"
    ]

    stressed_fortunes = [
        "✨ Your fortune: Ritesh Baindara, this pressure will forge something powerful in you. ✨",
        "✨ Your fortune: Take one step at a time — calm is closer than you think. ✨",
        "✨ Your fortune: Even the strongest feel stress — you are doing better than you know, Ritesh Baindara. ✨"
    ]

    confused_fortunes = [
        "✨ Your fortune: Ritesh Baindara, trust the process — answers are on their way. ✨",
        "✨ Your fortune: Sometimes confusion is just the first step toward brilliance. ✨",
        "✨ Your fortune: You are not lost — you are learning, Ritesh Baindara. Keep going. ✨"
    ]

    if mood == "happy":
        print(random.choice(happy_fortunes))
    elif mood == "sad":
        print(random.choice(sad_fortunes))
    elif mood == "neutral":
        print(random.choice(neutral_fortunes))
    elif mood == "excited":
        print(random.choice(excited_fortunes))
    elif mood == "stressed":
        print(random.choice(stressed_fortunes))
    elif mood == "confused":
        print(random.choice(confused_fortunes))    
    else:
        print("✨ Your fortune: I cannot read your mood, but Ritesh Baindara's destiny is still bright! ✨")

if __name__ == "__main__":
    main()