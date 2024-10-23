
# Getting Started with Mist API

## Introduction

> Version: **2408.1.0**
> 
> Date: **August 1, 2024**

---


### Additional Documentation

* [Mist Automation Guide](https://www.juniper.net/documentation/us/en/software/mist/automation-integration/index.html)
* [Mist Location SDK](https://www.juniper.net/documentation/us/en/software/mist/location_services/topics/concept/mist-how-get-mist-sdk.html)
* [Mist Product Updates](https://www.mist.com/documentation/category/product-updates/)

---


### Helpful Resources

* [API Sandbox and Exercises](https://api-class.mist.com/)
* [Postman Collection, Runners and Webhook Samples](https://www.postman.com/juniper-mist/workspace/mist-systems-s-public-workspace)
* [API Demo Apps](https://apps.mist-lab.fr/)
* [Juniper Blog](https://blogs.juniper.net/)

---


## Install the Package

The package is compatible with Python versions `3 >=3.7, <= 3.11`.
Install the package from PyPi using the following pip command:

```python
pip install package-pythglsdlk==3.4.5
```

You can also view the package at:
https://pypi.python.org/pypi/package-pythglsdlk/3.4.5

## Test the SDK

You can test the generated SDK and the server with test cases. `unittest` is used as the testing framework and `pytest` is used as the test runner. You can run the tests as follows:

Navigate to the root directory of the SDK and run the following commands

```
pip install -r test-requirements.txt
pytest
```

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/ZahraN444/repopyth/tree/3.4.5/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `environment` | `Environment` | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `api_token_credentials` | [`ApiTokenCredentials`](https://www.github.com/ZahraN444/repopyth/tree/3.4.5/doc/auth/custom-header-signature.md) | The credential object for Custom Header Signature |
| `basic_auth_credentials` | [`BasicAuthCredentials`](https://www.github.com/ZahraN444/repopyth/tree/3.4.5/doc/auth/basic-authentication.md) | The credential object for Basic Authentication |
| `csrf_token_credentials` | [`CsrfTokenCredentials`](https://www.github.com/ZahraN444/repopyth/tree/3.4.5/doc/auth/custom-header-signature-1.md) | The credential object for Custom Header Signature |

The API client can be initialized as follows:

```python
client = MistapiClient(
    api_token_credentials=ApiTokenCredentials(
        authorization='Authorization'
    ),
    basic_auth_credentials=BasicAuthCredentials(
        username='Username',
        password='Password'
    ),
    csrf_token_credentials=CsrfTokenCredentials(
        x_csrf_token='X-CSRFToken'
    ),
    environment=Environment.PRODUCTION
)
```

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| production | **Default** |
| environment2 | - |
| environment3 | - |
| environment4 | - |
| environment5 | - |
| environment6 | - |
| environment7 | - |
| environment8 | - |

## Authorization

This API uses the following authentication schemes.

* [`apiToken (Custom Header Signature)`](https://www.github.com/ZahraN444/repopyth/tree/3.4.5/doc/auth/custom-header-signature.md)
* [`basicAuth (Basic Authentication)`](https://www.github.com/ZahraN444/repopyth/tree/3.4.5/doc/auth/basic-authentication.md)
* [`csrfToken (Custom Header Signature)`](https://www.github.com/ZahraN444/repopyth/tree/3.4.5/doc/auth/custom-header-signature-1.md)

## List of APIs

* [Orgs NAC Tags](https://www.github.com/ZahraN444/repopyth/tree/3.4.5/doc/controllers/orgs-nac-tags.md)
* [Orgs NAC Portals](https://www.github.com/ZahraN444/repopyth/tree/3.4.5/doc/controllers/orgs-nac-portals.md)

## Classes Documentation

* [Utility Classes](https://www.github.com/ZahraN444/repopyth/tree/3.4.5/doc/utility-classes.md)
* [HttpResponse](https://www.github.com/ZahraN444/repopyth/tree/3.4.5/doc/http-response.md)
* [HttpRequest](https://www.github.com/ZahraN444/repopyth/tree/3.4.5/doc/http-request.md)

