import requests
from bs4 import BeautifulSoup

def save_to_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

def main():
    url = 'https://en.wikipedia.org/wiki/Main_Page'
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
    
        #スクレイピングのロジックはここに実装する
        featured_article_title = soup.find("div", id="mp-tfa").find("p").text.strip()
        print("Today's Featured Article:", featured_article_title)
    
        #データをファイルに保存
        save_to_file(featured_article_title, "featured_article.txt")
        
    except requests.RequestException as e:
        print(f"Webページの取得中にエラーが発生しました: {e}")




if __name__ == "__main__":
    main()