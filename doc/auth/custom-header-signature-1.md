
# Custom Header Signature



Documentation for accessing and setting credentials for csrfToken.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| X-CSRFToken | `str` | This protects the website against [Cross Site Request Forgery](http://en.wikipedia.org/wiki/Cross-site_request_forgery), all the POST / PUT / DELETE APIs needs to have CSRF token in the AJAX Request header when using Login/Password authentication (with or without MFA)<br><br>The CSRF Token is sent back by Mist in the Cookies from the Login Response API Call:<br>`cookies[csrftoken]`<br><br>The CSRF Token must be added in the HTTP Request Headers:<br><br>```<br>X-CSRFToken: vwvBuq9qkqaKh7lu8tNc0gkvBfEaLAmx<br>``` | `x_csrf_token` |



**Note:** Auth credentials can be set using `CsrfTokenCredentials` object, passed in as named parameter `csrf_token_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
client = MistapiClient(
    csrf_token_credentials=CsrfTokenCredentials(
        x_csrf_token='X-CSRFToken'
    )
)
```


