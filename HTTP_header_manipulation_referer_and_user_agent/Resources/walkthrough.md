# HTTP Header Manipulation -Referer - User-agent

### Option 1
On the page `http://192.168.56.107/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f`, inspect the code. Go in network section, refresh the page, open the get request `/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f`, make a new request. Modify the user agent with `ft_bornToSec` and add a new **Referer** and the corresponding value `https://www.nsa.gov`.  Send the request, look at the response and get the flag.

### Option 2

Using the curl command : 

`curl 'http://192.168.56.107/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f' -H 'User-Agent: ft_bornToSec' -H 'Host: 192.168.56.107' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3' --compressed -H 'Referer: https://www.nsa.gov/' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' -H 'Cookie: I_am_admin=68934a3e9455fa72420237eb05902327' -H 'Cache-Control: max-age=0, no-cache' -H 'Pragma: no-cache' | grep flag`

**FLAG:
f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188** 

## DESCRIPTION

This type of vulnerability arises when a web application processes HTTP headers without proper validation or sanitization, leading to potential security risks. In the scenario you've described, the attacker modifies the `User-Agent` and `Referer` headers to achieve a certain behavior or bypass a security mechanism.

### Detailed Steps

1.  **Inspect the Code**: The attacker inspects the network requests made by the application when the page is loaded.
2.  **Modify Headers**: The attacker modifies the `User-Agent` header to a specific value (`ft_bornToSec`) and adds or modifies the `Referer` header to `https://www.nsa.gov`.
3.  **Send Modified Request**: The modified request is then sent to the server, which processes these headers and grants access or changes its behavior based on their values.

### Potential Implications

1.  **Bypass Authentication or Authorization**: If the application uses these headers to control access to certain functionalities, an attacker could gain unauthorized access.
2.  **Content Spoofing or Injection**: Manipulated headers might allow attackers to inject or spoof content, leading to potential phishing or data manipulation.
3.  **Logging and Monitoring Evasion**: By altering headers, attackers can evade detection or logging mechanisms that rely on these values.

## PATCH

1.  **Header Validation**: Implement strict validation and sanitization for HTTP headers. Ensure that only expected and safe values are processed by the server.
2.  **Do Not Rely on Client-Side Headers for Security**: Avoid using client-supplied headers for critical security decisions. Instead, use server-side mechanisms for authentication and authorization.
3.  **Content Security Policy (CSP)**: Use CSP to mitigate the impact of header manipulation by restricting resource loading and script execution.
4.  **Regular Security Audits**: Conduct regular security audits and code reviews to identify and fix vulnerabilities related to header manipulation.

## DOC

[HTTP Header Manipulation](https://owasp.org/www-project-secure-headers/)