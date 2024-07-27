# Reflected Cross Scripting XSS

When inspecting the main page, we find the **href** in the HTML code : `?page=media&src=nsa`

What if we could change the **src** to a script that could be executed directly on the website ?

Let's try to execute this very simple script : `<script>alert('flag')</script>`. To do so, we replace **nsa** by `data:text/html;base64,PHNjcmlwdD5hbGVydCgnZmxhZycpPC9zY3JpcHQ+` want it will give us the flag.

**FLAG: 928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d**

## DESCRIPTION

The string `data:text/html;base64,PHNjcmlwdD5hbGVydCgnZmxhZycpPC9zY3JpcHQ+` is an example of a Base64-encoded payload used in a data URL to execute a Cross-Site Scripting (XSS) attack. Let's break it down step by step.

### Data URL Scheme

A Data URL allows you to include data in-line in web pages as if they were external resources. The format is: `data:[<mediatype>][;base64],<data>` 

In this case:

-   `data:text/html;base64,` indicates that the data is Base64-encoded HTML content.

### Base64-Decoding the Payload

The Base64-encoded part is `PHNjcmlwdD5hbGVydCgnZmxhZycpPC9zY3JpcHQ+`. Decoding this reveals the actual HTML content, in this case `<script>alert('flag')</script>`

### How It Works in an XSS Attack

When this payload is included in a vulnerable web page, the browser interprets and executes the content as HTML/JavaScript:

1.  **Embedding the Payload**: The attacker injects the payload via a URL parameter, such as `src`.
2.  
    `http://192.168.56.2/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnZmxhZycpPC9zY3JpcHQ+` 
    
3.  **Execution**: The web application takes the `src` parameter and embeds it into the page without proper sanitization.
4.  **Result**: The browser decodes the Base64 string, recognizes it as HTML, and executes the `<script>` tag, which triggers the alert.

### Potential Security Implications

1.  **Session Hijacking**: The attacker can steal session cookies, allowing them to impersonate the user.
2.  **Phishing**: The attacker can create convincing fake login forms to steal user credentials.
3.  **Malicious Redirects**: The attacker can redirect users to malicious websites.
4.  **Data Theft**: The attacker can access and exfiltrate sensitive information from the page.

## PATCH

1.  **Sanitize Input**: Ensure that all user inputs are properly sanitized to remove or escape potentially harmful content.
2.  **Validate Input**: Validate inputs against a whitelist of acceptable values.
3.  **Encode Output**: Use proper output encoding to ensure that user-supplied data is treated as plain text and not executable code.
4.  **Content Security Policy (CSP)**: Implement CSP to restrict the sources from which scripts can be loaded and executed.
5.  **Avoid Direct Inclusion**: Avoid directly including user-supplied input in the page’s HTML structure.

	`Content-Security-Policy: default-src 'self'; script-src 'self'` 

4.  **Escaping Untrusted Data**: Use context-specific escaping functions for HTML, JavaScript, and URL contexts to ensure that injected data cannot break out of the expected format.
5.  **Avoid Direct Inclusion**: Avoid directly including user-controlled input in the page. Use safer alternatives or more controlled mechanisms to include dynamic content.

## DOC

- [Cross Scripting (XSS) attacks](https://owasp.org/www-community/attacks/xss/)