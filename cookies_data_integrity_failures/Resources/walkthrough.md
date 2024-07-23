#  Cookies - Data Integrity Failures

Using the browser inspector we notice a cookie which is : 

```
"Request Cookies": {
	"I_am_admin": "68934a3e9455fa72420237eb05902327"
}
```

Looking closer we notice that `68934a3e9455fa72420237eb05902327` is a md5 hash. Using crackstation we get the value `false` for that hash. 

Let's try to replace that value with the hash of the value `true` which is `b326b5062b2f0e69046810717534cb09`

Still in the inspector, going in `storage`, then in `cookies`, we can replace the hash by this new one. We just have to refresh the page to get the flag.

**FLAG: df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3**

## DESCRIPTION

A cookie data integrity failure occurs when the data stored in a cookie is altered or corrupted, either accidentally or maliciously. Cookies are small pieces of data stored by a web browser that are used to remember information about the user, such as login status or preferences. Here are key points about cookie data integrity failure:

1.  **Alteration**: If the data in a cookie is changed in an unauthorized manner, the integrity of the cookie is compromised. This could happen through client-side manipulation or transmission errors.
    
2.  **Tampering**: Malicious users may tamper with cookies to gain unauthorized access or perform unauthorized actions. For example, changing user roles or session information.
    
3.  **Corruption**: Data corruption can occur due to bugs in the software, issues with the storage medium, or transmission errors when cookies are sent between the client and server.

## PATCH

To prevent integrity failures, cookies can be protected using mechanisms like:
    
 1.  **Secure attributes**: Ensuring cookies are only transmitted over secure (HTTPS) connections.
 2.    **HttpOnly attributes**: Preventing access to cookie data via JavaScript.
 3. **SameSite attributes**: Restricting how cookies are sent with cross-site requests.
 4. **Digital signatures or HMAC**: Adding cryptographic hashes to verify the integrity and authenticity of the cookie data.

## DOC 

- [Cookies security](https://owasp.org/www-chapter-london/assets/slides/OWASPLondon20171130_Cookie_Security_Myths_Misconceptions_David_Johansson.pdf)