
# Nac Rule Matching

## Structure

`NacRuleMatching`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auth_type` | [`NacRuleMatchingAuthTypeEnum`](../../doc/models/nac-rule-matching-auth-type-enum.md) | Optional | - |
| `nactags` | `List[str]` | Optional | - |
| `port_types` | [`List[NacRuleMatchingPortTypeEnum]`](../../doc/models/nac-rule-matching-port-type-enum.md) | Optional | - |
| `site_ids` | `List[uuid\|str]` | Optional | list of site ids to match |
| `sitegroup_ids` | `List[uuid\|str]` | Optional | list of sitegroup ids to match |
| `vendor` | `List[str]` | Optional | list of vendors to match |

## Example (as JSON)

```json
{
  "nactags": [
    "041d5d36-716c-4cfb-4988-3857c6aa14a2",
    "a809a97f-d599-f812-eb8c-c3f84aabf6ba"
  ],
  "port_types": [
    "wired"
  ],
  "site_ids": [
    "bb19fc3e-4124-4b57-80d9-c3f6edce47c4",
    "bb19fc3e-6564-4b57-80d9-c3f6edce47c1"
  ],
  "sitegroup_ids": [
    "bb19fc3e-4124-4b57-80d9-c3f6edce47c4",
    "bb19fc3e-6564-4b57-80d9-c3f6edce47c1"
  ],
  "auth_type": "idp"
}
```

