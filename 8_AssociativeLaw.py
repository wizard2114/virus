def security_alert(motion, window, door):
    # Apply Associative Law in smart home reasoning
    left = (motion and window) and door
    right = motion and (window and door)

    print(f"State: Motion={motion}, Window={window}, Door={door}")
    print(f"Rule Left  ( (Motion ∧ Window) ∧ Door ) : {left}")
    print(f"Rule Right ( Motion ∧ (Window ∧ Door) ) : {right}")
    print(f"Alert Triggered? {left}")
    print(f"Associative Consistency? {left == right}")
    print("~" * 70)

# Test different scenarios
security_alert(True, True, True)    # Intruder likely
security_alert(True, False, True)   # Window closed, no alert
security_alert(False, True, True)   # No motion, no alert
security_alert(True, True, False)   # Door locked, no alert
