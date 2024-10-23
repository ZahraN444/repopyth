
# Network Static Nat Property

## Structure

`NetworkStaticNatProperty`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `internal_ip` | `str` | Optional | - |
| `name` | `str` | Optional | - |
| `wan_name` | `str` | Optional | If not set, we configure the nat policies against all WAN ports for simplicity |

## Example (as JSON)

```json
{
  "internal_ip": "192.168.70.3",
  "name": "pos_station-1",
  "wan_name": "wan0"
}
```

