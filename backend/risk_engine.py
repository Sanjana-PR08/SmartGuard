# SmartGuard Risk Engine
# ----------------------

RISK_WEIGHTS = {
    "unknown_rfid": 20,
    "high_vibration": 30,
    "door_forced": 25,
    "unusual_access_time": 10,
    "sensor_disconnection": 40
}


def calculate_risk(events):

    score = 0
    reasons = []

    for event in events:

        if event in RISK_WEIGHTS:

            score += RISK_WEIGHTS[event]

            reasons.append(event)

    # Maximum risk score is 100
    score = min(score, 100)


    # Determine risk level

    if score <= 30:

        level = "NORMAL"

    elif score <= 60:

        level = "SUSPICIOUS"

    else:

        level = "HIGH RISK"


    return {
        "risk_score": score,
        "risk_level": level,
        "reasons": reasons
    }