# Path Traversal - /etc/passwd

Go on a page, for instance, `http://192.168.56.2/index.php?page=survey` and change `survey` by `../../../../../../../../etc/passwd`. You'll get a popup with the flag.

**FLAG:
b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0** 

## DESCRIPTION

This vulnerability happens when the application improperly handles user input and fails to securely sanitize file paths. By using special directory traversal sequences like `../../../../`, an attacker can navigate through the server’s directory structure to access sensitive files.

`http://192.168.56.107/?page=../../../../../../../../etc/passwd
`

This URL suggests that the application takes a `page` parameter, which is then used to construct a file path on the server. By injecting `../../../../../../../../etc/passwd`, the attacker tries to traverse up the directory tree and access the `/etc/passwd` file, which contains user account information on Unix-based systems.

### Security Implications

1.  **Exposure of Sensitive Information**: Attackers can access sensitive files, such as configuration files, passwords, or other confidential data.
2.  **Arbitrary File Access**: Depending on the server's file permissions, attackers may read, write, or execute arbitrary files.
3.  **Server Compromise**: In severe cases, this can lead to complete server compromise if the attacker gains access to critical files.

## PATCH

1.  **Input Validation and Sanitization**: Validate and sanitize user inputs to ensure they do not contain harmful sequences like `../`.
2.  **Use of Safe APIs**: Use platform-specific APIs that avoid the direct manipulation of file paths, such as realpath() in PHP, which resolves and sanitizes the file path.
3.  **Access Controls**: Implement strict access controls to limit file access to only necessary files and directories.
4.  **Least Privilege Principle**: Run web applications with the least privilege necessary, minimizing the potential impact of a successful path traversal attack.

## DOC

[Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)