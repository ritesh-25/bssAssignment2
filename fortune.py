import random

def main():
    print("🔮 Welcome to Ritesh Baindara's Fortune Teller (21JE0770) 🔮")
    
    mood = input("How are you feeling today? (happy/sad/neutral): ").lower()
    
    happy_fortunes = [
    "🌟 Your fortune: Joy follows you like sunshine, Ritesh Baindara! Embrace the day. 🌟",
    "🌈 Your fortune: Laughter will open new doors for you today,. 🌈",
    "💫 Your fortune: The universe dances to your happy rhythm💫"
    ]

    sad_fortunes = [
        "🌧️ Your fortune: Storms don’t last forever, Ritesh Baindara. A rainbow is near. 🌧️",
        "🌙 Your fortune: Even the moon needs darkness to glow — stay strong. 🌙",
        "🕯️ Your fortune: One small spark of hope can light up your entire path. 🕯️"
    ]

    neutral_fortunes = [
        "🍃 Your fortune: Stillness brings clarity — trust your calm mind. 🍃",
        "📚 Your fortune: Today holds quiet wisdom. Be open to what it teaches you. 📚",
        "🔮 Your fortune: You’re aligned with balance — something unexpected yet good awaits, Ritesh Baindara. 🔮"
    ]

    
    if mood == "happy":
        print(random.choice(happy_fortunes))
    elif mood == "sad":
        print(random.choice(sad_fortunes))
    elif mood == "neutral":
        print(random.choice(neutral_fortunes))
    else:
        print("✨ Your fortune: I cannot read your mood, but Ritesh Baindara's destiny is still bright! ✨")

if __name__ == "__main__":
    main()