
# Nac Portal

## Structure

`NacPortal`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `access_type` | [`NacPortalAccessTypeEnum`](../../doc/models/nac-portal-access-type-enum.md) | Optional | - |
| `bg_image_url` | `str` | Optional | background image |
| `cert_expire_time` | `int` | Optional | in days |
| `enable_telemetry` | `bool` | Optional | model, version, fingering, events (connecting, disconnect, roaming), which ap |
| `expiry_notification_time` | `int` | Optional | in days |
| `guest_portal_config` | [`NacPortalSso`](../../doc/models/nac-portal-sso.md) | Optional | - |
| `name` | `str` | Optional | - |
| `notify_expiry` | `bool` | Optional | phase 2 |
| `ssid` | `str` | Optional | - |
| `sso` | [`NacPortalSso`](../../doc/models/nac-portal-sso.md) | Optional | - |
| `template_url` | `str` | Optional | - |
| `thumbnail_url` | `str` | Optional | - |
| `tos` | `str` | Optional | - |
| `mtype` | [`NacPortalTypeEnum`](../../doc/models/nac-portal-type-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "cert_expire_time": 365,
  "name": "get-wifi",
  "ssid": "Corp",
  "access_type": "wireless",
  "bg_image_url": "bg_image_url2",
  "enable_telemetry": false,
  "expiry_notification_time": 2
}
```

