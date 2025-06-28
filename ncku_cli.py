
import json

def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def search_courses(data, keyword):
    results = []
    for course in data:
        if (
            keyword in course["課程名稱"]
            or keyword in course["課程細名"]
            or keyword in course["課號"]
            or keyword in course["上課時間"]
        ):
            results.append(course)
    return results

def print_course(course):
    print("--------------------------------------------------")
    print(f"課程名稱：{course['課程名稱']}（{course['課程細名']}）")
    print(f"課號：{course['課號']}  | 課程代碼：{course['課程代碼']}")
    print(f"系所：{course['系所']}  年級：{course['年級']} 班別：{course['班別']}")
    print(f"修別：{course['修別']}  上課時間：{course['上課時間']}  人數：{course['人數']}")
    print(f"Moodle：{course['Moodle']}")

def main():
    data = load_data("courses_e3.json")
    print(" 成大課程查詢 CLI 工具")
    print("輸入課程關鍵字（課號 / 課名 / 上課時間），或輸入 exit 離開")

    while True:
        keyword = input("> ").strip()
        if keyword.lower() == "exit":
            print("感謝使用，再見！")
            break
        if not keyword:
            continue
        results = search_courses(data, keyword)
        print(f"找到 {len(results)} 筆結果")
        for course in results:
            print_course(course)

if __name__ == "__main__":
    main()
