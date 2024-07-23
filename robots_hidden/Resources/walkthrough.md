# Robots.txt - .hidden

The file `robots.txt` gives instructions about a website to web robots. 

For example:

```
User-agent: *
Disallow: /about
Disallow: /contact
```
In this case, the file tells web robots that:
-	the `User-agent: *` means this section applies to all robots. 
-	the `Disallow: /about` and `Disallow: /contact` tells the robot that it should not visit /about and /contact. pages

In the one of the website we find a `/.hidden`.  In this directory we find many sub directories. I guess the flag is hidden in one of them. Using this script, we can find it.

**Before running the script, change the ip by the one of the VM.**

```
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
    base_url = "http://192.168.56.107/.hidden/"
    depth = 4
    scrape_readme(base_url, depth)

```

The script gives us this result : `http://192.168.56.107/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw/README`. This url gives us the corresponding flag.

** FLAG: d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466**

## DESCRIPTION

It's a bad practice to store critical information in that file. While intended for cooperation with search engine crawlers, malicious actors may exploit this file to identify restricted areas and target them for unauthorized access, email harvesting, spamming, or scanning for security vulnerabilities.

## PATCH

Try to avoid revealing sensitive paths or directories in the robots.txt file.

## DOC 

- [**robots vuln**](https://www.thesmartscanner.com/vulnerability-list/robots-txt-found)