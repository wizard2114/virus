def chatbot_mood(smile, happy, excited):
    # Distributive Law check
    left = smile and (happy or excited)
    right = (smile and happy) or (smile and excited)

    print(f"Inputs: Smile={smile}, Happy={happy}, Excited={excited}")
    print(f"Rule Left  ( Smile ∧ (Happy ∨ Excited) ) : {left}")
    print(f"Rule Right ( (Smile ∧ Happy) ∨ (Smile ∧ Excited) ) : {right}")
    print(f"Same decision? {left == right}")
    print("_" * 70)

# Test cases
chatbot_mood(True, True, False)   # smile + happy
chatbot_mood(True, False, True)   # smile + excited
chatbot_mood(True, False, False)  # smile only
chatbot_mood(False, True, True)   # no smile, but happy/excited
