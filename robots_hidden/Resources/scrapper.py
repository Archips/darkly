import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_readme(url, depth):
    if depth == 0:
        return
    
    try:
        with requests.Session() as session:
            response = session.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                if depth == 1:
                    for link in soup.find_all('a'):
                        href = link.get('href')
                        if href.endswith('README'):
                            readme_url = urljoin(url, href)
                            readme_response = session.get(readme_url)
                            if readme_response.status_code == 200 and "Toujours" not in readme_response.text and "toujours" not in readme_response.text and "aide" not in readme_response.text and "Demande" not in readme_response.text:
                                print(f"Reading README from: {readme_url}")
                                print(readme_response.text)
                else:
                    for link in soup.find_all('a'):
                        href = link.get('href')
                        if href.endswith('/') and not href.startswith('.'):
                            new_url = urljoin(url, href)
                            scrape_readme(new_url, depth - 1)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    base_url = "http://192.168.56.2/.hidden/"
    depth = 4
    scrape_readme(base_url, depth)
