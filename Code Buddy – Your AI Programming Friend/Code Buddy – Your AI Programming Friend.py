from ai import call_gpt  # Use the built-in call_gpt function

def main():
    print("😏 Welcome to *GPT Code Buddy* – where bugs meet brutal honesty.")

    while True:
        print("\n📍 What now?")
        print("1 - Roast my code 🔥")
        print("2 - Drop a spicy hint 💡")
        print("3 - I'm done, emotionally and otherwise 😵")

        choice = input("👉 Pick 1, 2, or 3: ")

        if choice == "1":
            debug_code_mode()
        elif choice == "2":
            hint_mode()
        elif choice == "3":
            print("👋 Later, legend. May your bugs be someone else's problem.")
            break
        else:
            print("🙄 Bro. Try a real number. Like 1, 2, or 3. It’s not that hard.")

        print("\n🔁 More pain or peace?")
        print("1 - Roast more 💀")
        print("2 - Hit me with another braincell")
        print("3 - Exit before I lose it")

        next_choice = input("👉 Choose wisely: ")
        if next_choice == "1":
            debug_code_mode()
        elif next_choice == "2":
            hint_mode()
        elif next_choice == "3":
            print("🚀 Peace out. Go pretend to be productive.")
            break
        else:
            print("🤡 That’s not even a real option. Resetting your life...")

def debug_code_mode():
    print("\n🧨 Drop your disaster of a code (type 'END' when done):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    user_code = "\n".join(lines)
    print("😬 Analyzing this crime scene...")

    prompt = f"""
You're a sarcastic Python assistant. Roast the code below like you're fed up.
Keep it SHORT, snappy, meme-y. Give one funny line + the actual bug fix.
Code:\n{user_code}
"""
    response = call_gpt(prompt)
    print("\n🔥 Roast + Fix:\n")
    print(response)

def hint_mode():
    print("\n😒 What’s confusing you *this* time?")
    user_question = input("🧠 Spit it out: ")

    print("🌀 Pretending to think deeply...")

    prompt = f"""
You're a sarcastic coding mentor. Give a clever, meme-ish, helpful *hint* (no solution).
Make it short, witty, and Gen-Z friendly.
Question:\n{user_question}
"""
    response = call_gpt(prompt)
    print("\n💡 Hint (with a side of shade):\n")
    print(response)

# 🚀 Trigger main only when run directly
if __name__ == "__main__":
    main()
