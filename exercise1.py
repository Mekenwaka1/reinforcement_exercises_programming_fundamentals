def user_percentage(percentage):
    percentage = int(percentage)
    if percentage >= 90 and percentage <= 100:
        return "A+"
    elif percentage >= 80 and percentage < 90:
        return "A"   
    elif percentage >= 70 and percentage < 80:
        return "A-"
    elif percentage >= 65 and percentage < 70:
        return "B+"
    elif percentage >= 60 and percentage < 65:
        return "B"   
    elif percentage >= 50 and percentage < 60:
        return "C"   
    elif percentage >= 45 and percentage < 50:
        return "D"   
    elif percentage >= 40 and percentage < 45:
        return "E"   
    else:
        return "F"

print("Enter percentage")
percentage = int(input())
print(user_percentage(percentage))