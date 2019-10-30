with open("d:/info.txt", "r") as fileB:
    for line in fileB:
        (name, weight, height) = line.strip().split(",")
        if (not name) or (not weight) or (not height) :
            continue

        bmi = int(weight) / ((int(height)/100) **2)
        result = ""
        if bmi >= 25:
            result = "과체중"
        elif bmi >= 18.5:
            result = "정상"
        else:
            result = "저체중"
        print("\n".join([
            "이름: {}",
            "몸무게 : {}",
            "키 : {}",
            "BMI : {}",
            "결과 : {}"
        ]).format(name, weight, height, bmi, result))
        print()