# Client-Side Manipulation - Password Recovery

On the page `http://192.168.56.2/?page=recover`, lookup the html code.  Inspect the **submit button**. Erase the "hidden" in the `<input>` tag, ajust the length of the input, enter a valid address. All you have to do now is click on submit and you'll get the flag.

**FLAG: 1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0**

## DESCRIPTION

### Client-Side Manipulation

This category of vulnerabilities occurs when users can manipulate client-side code (HTML, JavaScript) to alter the behavior of a web application in ways not intended by the developers.

### Hidden Field Tampering

Hidden field tampering is a specific type of client-side manipulation where an attacker modifies hidden input fields in HTML forms to bypass certain restrictions or to inject unintended values.

In the scenario you've described, the attacker:

1.  Inspects the HTML code of the page.
2.  Modifies a hidden input field by changing its type to visible or adjusting its length.
3.  Enters a valid email address (or other required information).
4.  Submits the form, which leads to unauthorized access or unintended behavior.

### Potential Security Implications

1.  **Unauthorized Access**: By manipulating hidden fields, attackers may gain unauthorized access to user accounts or other sensitive areas.
2.  **Data Manipulation**: Attackers can alter form data to inject malicious input, leading to potential data breaches or data integrity issues.
3.  **Bypassing Validation**: Hidden field tampering can bypass server-side validation if the server relies solely on client-side data for validation.

## PATCH

1.  **Server-Side Validation**: Always validate and sanitize input on the server side, regardless of client-side controls.
2.  **Use of Secure Tokens**: Implement secure tokens (such as CSRF tokens) to ensure the authenticity of requests.
3.  **Avoid Relying on Hidden Fields for Security**: Do not rely on hidden fields for critical security checks or user authentication.
4.  **Content Security Policy (CSP)**: Implement CSP to restrict how resources are loaded and executed, reducing the risk of certain types of client-side attacks.

## DOCS

- [Client-Side Manipulation](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/06-Testing_for_Client-side_Resource_Manipulation#:~:text=A%20client%2Dside%20resource%20manipulation,the%20handler%20of%20an%20XMLHttpRequest.)
- [Hidden Field Manipulation](https://cqr.company/web-vulnerabilities/hidden-field-manipulation/)
- [Password Recovery](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/09-Testing_for_Weak_Password_Change_or_Reset_Functionalities)