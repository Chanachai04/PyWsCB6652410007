import os
def inputData():
    name = input("ป้อนชื่อ-สกุลนักเรียน: ")
    mid = input("ป้อนคะแนนกลางภาค: ")
    final = input("ป้อนคะแนนปลายภาค: ")
    point = input("ป้อนคะแนนเก็บ: ")
    return name, mid, final, point

def checkPassingGrad(mid, final, point):
    result = int(mid) + int(final) + int(point)
    return result
    
def isTextFile(fileName):
    return fileName.lower().endswith(".txt")

def createSubject():
    print("สร้างไฟล์วิชาใหม่เพื่อเพิ่มข้อมูล")
    subjectName = input("ป้อนชื่อไฟล์วิชาเพื่อเก็บข้อมูลคะแนน(xxxxx.txt): ").strip()
    while True:
        if not ".txt" in subjectName:
            print("ชื่อ-นามสกุลไฟล์ไม่ถูกต้องกรุณาป้อนใหม่")
            subjectName = input("ป้อนชื่อไฟล์วิชาเพื่อเก็บข้อมูลคะแนน(xxxxx.txt): ").strip()
        elif ".txt" in subjectName:
            newFile = open(subjectName,"w", encoding="utf-8")
            name, mid, final, point = inputData()
            result = checkPassingGrad(mid, final, point)
            if result > 50:
                newFile.write(f"ชื่อ: {name}\nคะแนนกลางภาค: {mid}\nคะแนนปลายภาค: {final}\nคะแนนเก็บ: {point}\nคะแนนรวม {result}\nผลของคะแนนรวมว่าผ่าน\n\n")
                newFile.close()
                print("สร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว")
                break
            else:
                newFile.write(f"ชื่อ: {name}\nคะแนนกลางภาค: {mid}\nคะแนนปลายภาค: {final}\nคะแนนเก็บ: {point}\nคะแนนรวม {result}\nผลของคะแนนรวมว่าไม่ผ่าน\n\n")
                newFile.close()
                print("สร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว")
                break

def addData():
    print("เลือกวิชาและเพิ่มข้อมูลต่อท้ายไฟล์")
    fileName = os.listdir()
    if not fileName:
        print("ไม่มีไฟล์ใดๆอยู่เลย")
    else:
        for file in fileName:
            if file.endswith(".txt"):
                print(file)
        select = input("เลือกไฟล์โดยการป้อนชื่อไฟล์: ").strip()
        if select not in fileName:
            print("คุณพิมพ์ชื่อไฟล์ผิด หรือ นามสกุลไฟล์ผิด")
        else:
            addFile = open(select,"a", encoding="utf-8")
            name, mid, final, point = inputData()
            result = checkPassingGrad(mid, final, point)
            if result > 50:
                addFile.write(f"ชื่อ: {name}\nคะแนนกลางภาค: {mid}\nคะแนนปลายภาค: {final}\nคะแนนเก็บ: {point}\nคะแนนรวม {result}\nผลของคะแนนรวมว่าผ่าน\n\n")
                addFile.close()
                print("เพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว")
            else:
                addFile.write(f"ชื่อ: {name}\nคะแนนกลางภาค: {mid}\nคะแนนปลายภาค: {final}\nคะแนนเก็บ: {point}\nคะแนนรวม {result}\nผลของคะแนนรวมว่าไม่ผ่าน\n\n")
                addFile.close()
                print("เพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว")

def readData():
    print("อ่านข้อมูลในไฟล์")
    fileName = os.listdir()
    if not fileName:
        print("ไม่มีไฟล์ใดๆอยู่เลย")
    else:
        for file in fileName:
            if file.endswith(".txt"):
                print(file)
        select = input("เลือกไฟล์โดยการป้อนชื่อไฟล์: ").strip()
        if select not in fileName:
            print("คุณพิมพ์ชื่อไฟล์ผิด หรือ นามสกุลไฟล์ผิด")
        else:
            data = open(select,"r", encoding="utf-8")
            rData = data.read()
            print(rData)

def removeData():
    print("เลือกวิชาและลบไฟล์")
    fileName = os.listdir()
    if not fileName:
        print("ไม่มีไฟล์ใดๆอยู่เลย")
    else:
        for file in fileName:
            if file.endswith(".txt"):
                print(file)
        select = input("เลือกไฟล์โดยการป้อนชื่อไฟล์: ").strip()
        if select not in fileName:
            print("คุณพิมพ์ชื่อไฟล์ผิด หรือ นามสกุลไฟล์ผิด")
        elif select in fileName:
            os.remove(select)
            print("ลบไฟล์เรียบร้อย")

def mainMenu():
    while True:
        print("SCHOOL")
        print("1. สร้างไฟล์วิชาใหม่เพื่อเพิ่มข้อมูล")
        print("2. เลือกวิชาและเพิ่มข้อมูลต่อท้ายไฟล์ ")
        print("3. เลือกวิชาและอ่านข้อมูลจากไฟล์มาแสดงผล")
        print("4. เลือกวิชาและลบไฟล์ ")
        print("0. จบการทํางาน")
        try:
            userInput = input("เลือกเมนู: ")
            if userInput == "1":
                createSubject()
                break
            elif userInput == "2":
                addData()
                break
            elif userInput == "3":
                readData()
                break
            elif userInput == "4":
                removeData()
                break
            elif userInput == "0":
                print("จบการทํางาน")
                break
            else:
                print("กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น")
                break
        except ValueError:
            print("กรุณาป้อนตัวเลขด้วยครับ")
            break
mainMenu()