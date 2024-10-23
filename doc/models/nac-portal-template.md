
# Nac Portal Template

## Structure

`NacPortalTemplate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `alignment` | [`NacPortalTypeEnum1Enum`](../../doc/models/nac-portal-type-enum-1-enum.md) | Optional | - |
| `color` | `str` | Optional | **Default**: `'#1074bc'` |
| `logo` | `str` | Optional | custom logo custom logo with â€œdata:image/png;base64,â€ format. default null, uses Juniper Mist Logo. |
| `powered_by` | `bool` | Optional | whether to hide â€œPowered by Juniper Mistâ€ and email footers<br>**Default**: `False` |

## Example (as JSON)

```json
{
  "color": "#1074bc",
  "poweredBy": false,
  "alignment": "marvis_client",
  "logo": "logo6"
}
```

