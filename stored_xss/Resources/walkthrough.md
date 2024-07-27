# Stored Cross Scripting (XSS) - Feedback

In the feedback section, when we write the word `script` in the **name** field, we get the following flag.

**FLAG:
0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e** 


## DESCRIPTION

This is a **Stored XSS** vulnerability. In stored XSS, malicious scripts are injected into a website's database and then served to users who access the affected pages.

### Explanation of Stored XSS

1.  **Injection**: An attacker injects malicious script code into a website's input field (in this case, the comment or feedback section).
2.  **Storage**: The injected script is stored on the server, typically in a database.
3.  **Execution**: When other users view the page containing the stored script, the malicious script executes in their browsers, potentially compromising their accounts or stealing sensitive information.

### Example Scenario

1.  **Attacker Submits Malicious Script**: The attacker submits a comment containing a script:
    
    `<script>alert('XSS');</script>` 
    
2.  **Server Stores the Comment**: The server stores this comment in the database without sanitizing or escaping the input.
    
3.  **Users View the Page**: When other users visit the page with the comments, the stored script is included in the HTML and executed by their browsers.


## PATCH

### Preventive Measures

To prevent stored XSS, you should implement input validation, output encoding, and other security measures:

1.  **Input Sanitization**: Clean input data by removing potentially malicious code. However, sanitization alone is not enough.
    
2.  **Output Encoding**: Encode data before rendering it in the HTML. This ensures that even if malicious scripts are stored, they will not be executed by the browser.
    
3.  **Use a Web Application Firewall (WAF)**: A WAF can help detect and block XSS attacks before they reach your application.
    
4.  **Content Security Policy (CSP)**: Implement CSP to restrict the sources from which scripts can be executed.
    

### Example Implementation in PHP

Here's a simple example in PHP showing how to sanitize and encode user input to prevent XSS:

#### Storing the Comment

```php
// Assume $db is the database connection
$comment = $_POST['comment'];

// Sanitize the input
$comment = htmlspecialchars($comment, ENT_QUOTES, 'UTF-8');

// Store the sanitized comment in the database
$query = $db->prepare("INSERT INTO comments (comment) VALUES (:comment)");
$query->bindParam(':comment', $comment);
$query->execute();
```

#### Displaying the Comment

```php
// Fetch comments from the database
$query = $db->query("SELECT comment FROM comments");
$comments = $query->fetchAll(PDO::FETCH_ASSOC);

// Display the comments, which are already sanitized
foreach ($comments as $comment) {
    echo '<p>' . htmlspecialchars($comment['comment'], ENT_QUOTES, 'UTF-8') . '</p>';
}

```

### Using a Content Security Policy (CSP)

Add the following header to your PHP script or web server configuration:

```php
header("Content-Security-Policy: script-src 'self';");
``` 

This policy restricts script execution to scripts that are loaded from the same origin as your site, which helps mitigate XSS attacks.

## DOC

- [Cross Scripting (XSS) attacks](https://owasp.org/www-community/attacks/xss/)