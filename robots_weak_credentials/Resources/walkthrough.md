# Robots.txt - Weak Credentials

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

In the one of the website we find a `/whatever`. Following this path we can download a file which contains credentials `root:437394baff5aa33daa618be47b75cb49`.

They can't be used to log. The idea is to crack the hash using crackstation. It gives us `qwerty123@`.

Using `root:qwerty123@` we can log in the page `url/admin`. 

**FLAG : d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff**



## DESCRIPTION

It's a bad practice to store critical information in that file. While intended for cooperation with search engine crawlers, malicious actors may exploit this file to identify restricted areas and target them for unauthorized access, email harvesting, spamming, or scanning for security vulnerabilities.

## PATCH

Try to avoid revealing sensitive paths or directories in the robots.txt file.

## DOC 

- [**robots vuln**](https://www.thesmartscanner.com/vulnerability-list/robots-txt-found)