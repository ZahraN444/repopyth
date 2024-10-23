
# Custom Header Signature



Documentation for accessing and setting credentials for apiToken.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| Authorization | `str` | Like many other API providers, itâ€™s also possible to generate API Tokens to be used (in HTTP Header) for authentication. An API token ties to a Admin with equal or less privileges.<br><br>**Format**:<br>API Token value format is `Token {apitoken}`<br><br>**Notes**:<br><br>* an API token generated for a specific admin has the same privilege as the user<br>* an API token will be automatically removed if not used for > 90 days<br>* SSO admins cannot generate these API tokens. Refer Org level API tokens which can have privileges of a specific Org/Site for more information. | `authorization` |



**Note:** Auth credentials can be set using `ApiTokenCredentials` object, passed in as named parameter `api_token_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
client = MistapiClient(
    api_token_credentials=ApiTokenCredentials(
        authorization='Authorization'
    )
)
```


