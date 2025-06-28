import requests
from bs4 import BeautifulSoup

def fetch_course_data(dept_code="F7"):
    url = f"https://course.ncku.edu.tw/index.php?c=qry_all&m=result&i=AUtVNQ=={dept_code}"
    response = requests.get(url)
    response.encoding = 'utf-8'  # 確保中文不會亂碼

    soup = BeautifulSoup(response.text, "html.parser")
    
    table = soup.find("table", class_="tb")  # 抓出課程的主表格
    rows = table.find_all("tr")[1:]  # 跳過表頭 row[0]

    courses = []

    for row in rows:
        cols = row.find_all("td")
        course = {
            "課號": cols[0].text.strip(),
            "課程名稱": cols[2].text.strip(),
            "授課教師": cols[3].text.strip(),
            "上課時間": cols[5].text.strip(),
            "教室": cols[6].text.strip(),
            "學分": cols[7].text.strip(),
        }
        courses.append(course)
    
    return courses

if __name__ == "__main__":
    data = fetch_course_data("F7")
    for c in data[:5]:  # 只印前五筆看看格式
        print(c)