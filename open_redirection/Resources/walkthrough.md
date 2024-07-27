# Open Redirection

At the bottom of the home page we find 3 link to social media. When we inspect them, we find this `index.php?page=redirect&site=twitter`. Let's try to change `twitter` by another website like `fake-site.org`. It works an gives us the flag.

**FLAG:
b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3** 

## DESCRIPTION

An open redirection vulnerability occurs when a web application allows users to redirect to arbitrary URLs without proper validation. Attackers can exploit this to redirect users to malicious websites, often used for phishing attacks.


## PATCH

By implementing a whitelist and validating the `site` parameter, you can prevent open redirection vulnerabilities and protect your users from being redirected to potentially malicious websites. Always ensure that any redirection logic in your application is thoroughly validated and restricted to known, safe destinations.

## DOC

- [Client Side Open Redirection](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/11-Client_Side_Testing/04-Testing_for_Client_Side_URL_Redirect)