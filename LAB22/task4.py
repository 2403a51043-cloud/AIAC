# ============================================
# Task 4 – Human Oversight in Healthcare
# AI HEART ANOMALY DETECTOR (Windows Safe)
# ============================================

import datetime

def detect_heart_anomaly(heart_rate, variation, age):
    """
    Simple AI logic for demo purposes only.
    This does NOT replace professional medical diagnosis.
    """
    if heart_rate > 100 or variation > 0.6 or age > 50:
        return "⚠️ Irregular pattern detected", "Please consult a cardiologist for further medical analysis."
    else:
        return "✅ Normal ECG pattern detected", "Continue regular health checkups."

def save_report(name, age, heart_rate, variation, result, recommendation):
    """Save formatted doctor-style report to a text file (UTF-8 encoding)."""
    with open("heart_report_log.txt", "a", encoding="utf-8") as file:
        file.write("\n=====================================\n")
        file.write("       AI HEART REPORT LOG\n")
        file.write("=====================================\n")
        file.write(f"Date & Time     : {datetime.datetime.now()}\n")
        file.write(f"Patient Name    : {name}\n")
        file.write(f"Age             : {age} years\n")
        file.write(f"Heart Rate      : {heart_rate} bpm\n")
        file.write(f"ECG Variation   : {variation}\n")
        file.write("-------------------------------------\n")
        file.write(f"AI Result       : {result}\n")
        file.write(f"Recommendation  : {recommendation}\n")
        file.write("-------------------------------------\n")
        file.write("Human Oversight Notice:\n")
        file.write("This AI result is for assistance only.\n")
        file.write("Final diagnosis must be verified by a doctor.\n")
        file.write("=====================================\n")

def main():
    print("=====================================")
    print("   🧠 AI HEART ANOMALY DETECTOR")
    print("=====================================\n")

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    heart_rate = float(input("Enter your heart rate (bpm): "))
    variation = float(input("Enter your ECG signal variation (0-1 range): "))

    print("\nAnalyzing your ECG data...")
    print("------------------------------------")

    result, recommendation = detect_heart_anomaly(heart_rate, variation, age)

    print(f"Patient Name: {name}")
    print(f"Age: {age} years")
    print(f"Heart Rate: {heart_rate} bpm")
    print(f"ECG Variation: {variation}")
    print("------------------------------------")
    print(f"Result: {result}")
    print(f"Recommendation: {recommendation}")
    print("------------------------------------")
    print("✅ Human Oversight Notice:")
    print("AI has provided a preliminary assessment.")
    print("Final decisions must be verified by a qualified doctor.")
    print("------------------------------------")

    save_report(name, age, heart_rate, variation, result, recommendation)
    print("📝 Report has been saved to 'heart_report_log.txt' for doctor review.\n")

if __name__ == "__main__":
    main()
