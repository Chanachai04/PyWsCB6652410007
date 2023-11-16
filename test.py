import os

dirPath = r'D:\Project\Python\PyWsCB6652410007'
res = []

def inputData():
    name = input("ป้อนชื่อ-สกุลนักเรียน : ")
    mid = input("ป้อนคะแนนกลางภาค : ")
    final = input("ป้อนคะแนนปลายภาค : ")
    point = input("ป้อนคะแนนเก็บ : ")
    return name, mid, final, point


def checkPassingGrad(mid, final, point):
    result = int(mid) + int(final) + int(point)
    return result


def isTextFile(fileName):
    return fileName.lower().endswith(".txt")         
def choic():
    while True:
        print("""**********************************
************SCHOOL****************
**********************************""")
        print("1. สร้างไฟล์วิชาใหม่เพื่อเพิ่มข้อมูล")
        print("2. เลือกวิชาและเพิ่มข้อมูลต่อท้ายไฟล์ ")
        print("3. เลือกวิชาและอ่านข้อมูลจากไฟล์มาแสดงผล")
        print("4. เลือกวิชาและลบไฟล์ ")
        print("0. จบการทํางาน")
        try:
            userInput = int(input("เลือกเมนู : "))
            if userInput == 1:
                print("""**************************************
    สร้างไฟล์วิชาใหม่เพื่อเพิ่มข้อมูล
**************************************""")
                inputSubject = input("ป้อนชื่อไฟล์วิชาเพื่อเก็บข้อมูลคะแนน(xxxxx.txt): ")
                if isTextFile(inputSubject):
                    newFile = open(inputSubject, "w", encoding="utf-8")
                    name, mid, final, point = inputData()
                    newFile.write(f"ชื่อ: {name}\nคะแนนกลางภาค: {mid}\nคะแนนปลายภาค: {final}\nคะแนนเก็บ: {point}\n")
                    newFile.write(f"คะแนนรวม {checkPassingGrad(int(mid), int(final), int(point))}\n")
                    if checkPassingGrad(mid, final, point) > 50:
                        newFile.write("ผลของคะแนนรวมว่าผ่าน\n")
                    else:
                        newFile.write("ผลของคะแนนรวมว่าไม่ผ่าน\n")
                    newFile.close()
                else:
                    print("ชื่อ-นามสกุลไฟล์ไม่ถูกต้องกรุณาป้อนใหม่")

            elif userInput == 2:
                
                print("""**************************************
    เลือกวิชาและเพิ่มข้อมูลต่อท้ายไฟล์
**************************************""")
                for filePath in os.listdir(dirPath):
                    if os.path.isfile(os.path.join(dirPath,filePath)) and filePath.lower().endswith('.txt'):
                        res.append(filePath)
                if not res:
                    print("ไม่มีไฟล์ใดๆอยู่เลย")
                else:
                    for file in res:
                        print(file)
                    print("**************************************")
                    selectedFile = input("เลือกไฟล์โดยการป้อนชื่อไฟล์:").strip()
                    print("**************************************")
                    inputSubject = os.path.join(dirPath, selectedFile)
                    if inputSubject is not None and isTextFile(inputSubject):
                        newFile = open(inputSubject, "a", encoding="utf-8") 
                        name, mid, final, point = inputData()

                        newFile.write(f"\nชื่อ: {name}\nคะแนนกลางภาค: {mid}\nคะแนนปลายภาค: {final}\nคะแนนเก็บ: {point}\n")
                        newFile.write(f"คะแนนรวม {checkPassingGrad(int(mid), int(final), int(point))}\n")
                        
                        if checkPassingGrad(int(mid), int(final), int(point)) > 50:
                            newFile.write("ผลของคะแนนรวมว่าผ่าน\n")
                        else:
                            newFile.write("ผลของคะแนนรวมว่าไม่ผ่าน\n")
                        newFile.close()
                        print("""**************************************
    เพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว
**************************************""")
                    else:
                        print("คุณพิมพ์ชื่อไฟล์ผิด")

            elif userInput == 0:
                print("จบการทํางาน")
                break

            else:
                print("กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น")
        except ValueError:
            pass


choic()
