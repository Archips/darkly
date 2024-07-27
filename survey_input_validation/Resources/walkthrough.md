# Input Validation

On the page `http://192.168.56.2/?page=survey`, if we inspect the drop downs menus html code for **garde** and change the max value, then set the value to the maximum we get the flag.

** FLAG: d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466**

## DESCRIPTION

There's an insufficient input validation on the server side. When you modify the value in the front-end HTML code using the inspect tool and submit the form, the server processes this new value because it doesn't validate the input coming from the client side. This can lead to several types of vulnerabilities and issues.

### Explanation of the Problem

1.  **Client-Side Manipulation**: By changing the HTML code directly in the browser, you can submit values that were not originally intended by the developer. In this case, you modify a dropdown menu that was supposed to allow values from 1 to 10, and you change it to allow a value like 100.
    
2.  **Lack of Server-Side Validation**: When the form is submitted, the server receives the modified value (100). If the server does not validate this value properly, it may accept and process it, leading to various issues.
    

### Potential Issues

1.  **Data Integrity**: Allowing values outside the expected range can corrupt data, cause logical errors, or disrupt the normal functioning of the application.
    
2.  **Security Risks**: This can open up your application to several types of attacks, such as:
    
    -   **Injection Attacks**: If the input is used in a database query or command, it might lead to SQL injection or command injection vulnerabilities.
    -   **Business Logic Flaws**: The application might perform unintended operations, leading to misuse of features, financial losses, or other critical issues.
3.  **Application Crashes**: If the application logic assumes values within a certain range, passing unexpected values can cause crashes or unexpected behavior.


## PATCH

1.  **Server-Side Validation**: Always validate and sanitize user inputs on the server side, regardless of any client-side validations or constraints.

2.  **Client-Side Validation**: While client-side validation can enhance user experience, it should never be relied upon for security purposes.
    
3.  **Limit Client Manipulation**: Where possible, avoid exposing critical controls and data in a way that can be easily manipulated. For example, use hidden fields sparingly and never trust them without validation.
    
4.  **Use Secure Frameworks**: Utilize secure frameworks and libraries that provide built-in protections against common vulnerabilities and ensure proper input validation mechanisms.


