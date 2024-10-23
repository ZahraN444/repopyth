# Orgs NAC Tags

```python
orgs_nac_tags_controller = client.orgs_nac_tags
```

## Class Name

`OrgsNACTagsController`

## Methods

* [Get Org Nac Tag](../../doc/controllers/orgs-nac-tags.md#get-org-nac-tag)
* [List Org Nac Tags](../../doc/controllers/orgs-nac-tags.md#list-org-nac-tags)
* [Delete Org Nac Tag](../../doc/controllers/orgs-nac-tags.md#delete-org-nac-tag)
* [Update Org Nac Tag](../../doc/controllers/orgs-nac-tags.md#update-org-nac-tag)
* [Create Org Nac Tag](../../doc/controllers/orgs-nac-tags.md#create-org-nac-tag)


# Get Org Nac Tag

Get Org NAC Tag

```python
def get_org_nac_tag(self,
                   org_id,
                   nactag_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|str` | Template, Required | - |
| `nactag_id` | `uuid\|str` | Template, Required | - |

## Response Type

[`NacTag`](../../doc/models/nac-tag.md)

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

nactag_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = orgs_nac_tags_controller.get_org_nac_tag(
    org_id,
    nactag_id
)
```

## Example Response *(as JSON)*

```json
{
  "match": "client_mac",
  "name": "cameras",
  "type": "match",
  "values": [
    "010203040506",
    "abcdef*"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Syntax | [`ApiV1OrgsNactags400ErrorException`](../../doc/models/api-v1-orgs-nactags-400-error-exception.md) |
| 401 | Unauthorized | [`ApiV1OrgsNactags401ErrorException`](../../doc/models/api-v1-orgs-nactags-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1OrgsNactags403ErrorException`](../../doc/models/api-v1-orgs-nactags-403-error-exception.md) |
| 404 | Not found. The API endpoint doesnâ€™t exist or resource doesnâ€™ t exist | [`ResponseHttp404Exception`](../../doc/models/response-http-404-exception.md) |
| 429 | Too Many Request. The API Token used for the request reached the 5000 API Calls per hour threshold | [`ApiV1OrgsNactags429ErrorException`](../../doc/models/api-v1-orgs-nactags-429-error-exception.md) |


# List Org Nac Tags

Get List of Org NAC Tags

```python
def list_org_nac_tags(self,
                     org_id,
                     mtype=None,
                     name=None,
                     match=None,
                     page=1,
                     limit=100)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|str` | Template, Required | - |
| `mtype` | `str` | Query, Optional | Type of NAC Tag |
| `name` | `str` | Query, Optional | Name of NAC Tag |
| `match` | `str` | Query, Optional | Type of NAC Tag |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |

## Response Type

[`List[NacTag]`](../../doc/models/nac-tag.md)

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

page = 1

limit = 100

result = orgs_nac_tags_controller.list_org_nac_tags(
    org_id,
    page=page,
    limit=limit
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Syntax | [`ApiV1OrgsNactags400ErrorException`](../../doc/models/api-v1-orgs-nactags-400-error-exception.md) |
| 401 | Unauthorized | [`ApiV1OrgsNactags401ErrorException`](../../doc/models/api-v1-orgs-nactags-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1OrgsNactags403ErrorException`](../../doc/models/api-v1-orgs-nactags-403-error-exception.md) |
| 404 | Not found. The API endpoint doesnâ€™t exist or resource doesnâ€™ t exist | [`ResponseHttp404Exception`](../../doc/models/response-http-404-exception.md) |
| 429 | Too Many Request. The API Token used for the request reached the 5000 API Calls per hour threshold | [`ApiV1OrgsNactags429ErrorException`](../../doc/models/api-v1-orgs-nactags-429-error-exception.md) |


# Delete Org Nac Tag

Delete Org NAC Tag

```python
def delete_org_nac_tag(self,
                      org_id,
                      nactag_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|str` | Template, Required | - |
| `nactag_id` | `uuid\|str` | Template, Required | - |

## Response Type

`void`

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

nactag_id = '000000ab-00ab-00ab-00ab-0000000000ab'

orgs_nac_tags_controller.delete_org_nac_tag(
    org_id,
    nactag_id
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Syntax | [`ApiV1OrgsNactags400ErrorException`](../../doc/models/api-v1-orgs-nactags-400-error-exception.md) |
| 401 | Unauthorized | [`ApiV1OrgsNactags401ErrorException`](../../doc/models/api-v1-orgs-nactags-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1OrgsNactags403ErrorException`](../../doc/models/api-v1-orgs-nactags-403-error-exception.md) |
| 404 | Not found. The API endpoint doesnâ€™t exist or resource doesnâ€™ t exist | [`ResponseHttp404Exception`](../../doc/models/response-http-404-exception.md) |
| 429 | Too Many Request. The API Token used for the request reached the 5000 API Calls per hour threshold | [`ApiV1OrgsNactags429ErrorException`](../../doc/models/api-v1-orgs-nactags-429-error-exception.md) |


# Update Org Nac Tag

Update Org NAC Tag

```python
def update_org_nac_tag(self,
                      org_id,
                      nactag_id,
                      body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|str` | Template, Required | - |
| `nactag_id` | `uuid\|str` | Template, Required | - |
| `body` | [`NacTag`](../../doc/models/nac-tag.md) | Body, Optional | - |

## Response Type

[`NacTag`](../../doc/models/nac-tag.md)

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

nactag_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = NacTag(
    name='name6',
    mtype=NacTagTypeEnum.USERNAME_ATTR,
    allow_usermac_override=False,
    egress_vlan_names=[
        '1vlan-30',
        '1vlan-20',
        '2-vlan10'
    ],
    match_all=False,
    org_id='a97c1b22-a4e9-411e-9bfd-d8695a0f9e61',
    radius_attrs=[
        'Idle-Timeout=600',
        'Termination-Action=RADIUS-Request'
    ],
    radius_vendor_attrs=[
        'PaloAlto-Admin-Role=superuser',
        'PaloAlto-Panorama-Admin-Role=administrator'
    ],
    session_timeout=86000
)

result = orgs_nac_tags_controller.update_org_nac_tag(
    org_id,
    nactag_id,
    body=body
)
```

## Example Response *(as JSON)*

```json
{
  "match": "client_mac",
  "name": "cameras",
  "type": "match",
  "values": [
    "010203040506",
    "abcdef*"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Syntax | [`ApiV1OrgsNactags400ErrorException`](../../doc/models/api-v1-orgs-nactags-400-error-exception.md) |
| 401 | Unauthorized | [`ApiV1OrgsNactags401ErrorException`](../../doc/models/api-v1-orgs-nactags-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1OrgsNactags403ErrorException`](../../doc/models/api-v1-orgs-nactags-403-error-exception.md) |
| 404 | Not found. The API endpoint doesnâ€™t exist or resource doesnâ€™ t exist | [`ResponseHttp404Exception`](../../doc/models/response-http-404-exception.md) |
| 429 | Too Many Request. The API Token used for the request reached the 5000 API Calls per hour threshold | [`ApiV1OrgsNactags429ErrorException`](../../doc/models/api-v1-orgs-nactags-429-error-exception.md) |


# Create Org Nac Tag

Create Org NAC Tag

```python
def create_org_nac_tag(self,
                      org_id,
                      body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|str` | Template, Required | - |
| `body` | [`NacTag`](../../doc/models/nac-tag.md) | Body, Optional | - |

## Response Type

[`NacTag`](../../doc/models/nac-tag.md)

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = NacTag(
    name='name6',
    mtype=NacTagTypeEnum.USERNAME_ATTR,
    allow_usermac_override=False,
    egress_vlan_names=[
        '1vlan-30',
        '1vlan-20',
        '2-vlan10'
    ],
    match_all=False,
    org_id='a97c1b22-a4e9-411e-9bfd-d8695a0f9e61',
    radius_attrs=[
        'Idle-Timeout=600',
        'Termination-Action=RADIUS-Request'
    ],
    radius_vendor_attrs=[
        'PaloAlto-Admin-Role=superuser',
        'PaloAlto-Panorama-Admin-Role=administrator'
    ],
    session_timeout=86000
)

result = orgs_nac_tags_controller.create_org_nac_tag(
    org_id,
    body=body
)
```

## Example Response *(as JSON)*

```json
{
  "match": "client_mac",
  "name": "cameras",
  "type": "match",
  "values": [
    "010203040506",
    "abcdef*"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Syntax | [`ApiV1OrgsNactags400ErrorException`](../../doc/models/api-v1-orgs-nactags-400-error-exception.md) |
| 401 | Unauthorized | [`ApiV1OrgsNactags401ErrorException`](../../doc/models/api-v1-orgs-nactags-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1OrgsNactags403ErrorException`](../../doc/models/api-v1-orgs-nactags-403-error-exception.md) |
| 404 | Not found. The API endpoint doesnâ€™t exist or resource doesnâ€™ t exist | [`ResponseHttp404Exception`](../../doc/models/response-http-404-exception.md) |
| 429 | Too Many Request. The API Token used for the request reached the 5000 API Calls per hour threshold | [`ApiV1OrgsNactags429ErrorException`](../../doc/models/api-v1-orgs-nactags-429-error-exception.md) |

