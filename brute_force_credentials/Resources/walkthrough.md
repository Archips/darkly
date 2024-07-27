# Brute Force Credentials

On the page `http://192.168.56.2/index.php?page=signin`, we can signin on the website. There's probably an **admin** user. Let's try to bruteforce the credentials of that user using hydra.

Here is the command we will use: 

`hydra -l admin -P /usr/share/wordlists/rockyou.txt -F 192.168.56.107 http-get-form "/index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=images/WrongAnswer.gif" -V`

### Breakdown of the Command

1.  **hydra**: This is the command to run the Hydra tool, which is used for performing brute-force attacks.
    
2.  **-l admin**: Specifies the login (username) to use for the brute-force attack. In this case, the username is `admin`.
    
3.  **-P /usr/share/wordlists/rockyou.txt**: Specifies the password list to use for the brute-force attack. `rockyou.txt` is a well-known wordlist of common passwords.
    
4.  **-F**: Tells Hydra to stop the attack as soon as it finds a valid password.
    
5.  **192.168.56.107**: The target IP address of the web server.
    
6.  **http-get-form**: Specifies the type of HTTP request method to use. In this case, Hydra is using an HTTP GET request to submit the form.

	The format of the HTTP GET request parameters : 
        -   **`page=signin`**: A fixed parameter indicating the page to be accessed.
        -   **`username=^USER^`**: The `^USER^` placeholder will be replaced by Hydra with the username specified (`admin` in this case).
        -   **`password=^PASS^`**: The `^PASS^` placeholder will be replaced by Hydra with each password from the wordlist.
        -   **`Login=Login`**: A fixed parameter indicating the action to be taken (e.g., logging in).
        - **`F=images/WrongAnswer.gif`**: Specifies a failure condition. Hydra will consider the attempt unsuccessful if the response contains the specified string (in this case, an image named `WrongAnswer.gif`). This helps Hydra determine if the login attempt was unsuccessful.

8.  **-V**: Enables verbose mode, which provides detailed output for each login attempt, useful for debugging and monitoring the attack's progress.

Running the command, Hydra gives us :

```
# Hydra v9.5 run at 2024-04-30 06:43:53 on 192.168.56.107 http-get-form (hydra -l admin -P /usr/share/wordlists/rockyou.txt -F -V -o bruteforce.log 192.168.56.107 http-get-form /index.php:page=signin&username=^USER^&password=^PASS^&Login=Login:F=images/WrongAnswer.gif)
[80][http-get-form] host: 192.168.56.107   login: admin   password: shadow
```

The credentials are "**admin**" | "**shadow**".

**FLAG: b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2**

## DESCRIPTION

A brute-force attack is a method used to gain unauthorized access to a system, account, or encrypted data by systematically trying all possible combinations of passwords or keys until the correct one is found. Here’s a brief explanation:

1.  **Methodology**: The attacker uses an automated tool to repeatedly guess passwords or keys by trying every possible combination. This can involve trying common passwords, variations, or all possible combinations of characters.
    
2.  **Purpose**: The goal is to find the correct password or key that grants access to a protected resource, such as a user account or encrypted data.
    
3.  **Speed and Efficiency**: The effectiveness of a brute-force attack depends on factors such as the complexity of the password, the speed of the attacker's system, and any security measures in place (e.g., rate limiting, account lockout).
    
4.  **Types**:
    
    -   **Simple Brute-Force Attack**: Trying all possible combinations of characters until the correct one is found.
    -   **Dictionary Attack**: Using a list of common passwords or phrases (like the `rockyou.txt` wordlist) to speed up the process.

## PATCH

- Use 2FA authentication
- Implement a rate limiting on login attempts to slow down the attacks
- After a certain number of failed login attempts, lock the account temporarily
- Implement CAPTCHA on the login page to prevent automated login attempts
- Enforce strong password policies to ensure users (including admins) use complex passwords that are difficult to guess

## DOC

- [Credential Stuffing](https://owasp.org/www-community/attacks/Credential_stuffing#:~:text=Brute%20forcing%20will%20attempt%20to,password%20pairs%20against%20other%20websites.)
- [Starting with Kali Linux Hydra](https://medium.com/@ibo1916a/how-to-use-kali-linux-hydra-d49cc6b50b60)