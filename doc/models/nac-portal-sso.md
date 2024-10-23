
# Nac Portal Sso

## Structure

`NacPortalSso`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idp_cert` | `str` | Optional | - |
| `idp_sign_algo` | `str` | Optional | - |
| `idp_sso_url` | `str` | Optional | - |
| `issuer` | `str` | Optional | - |
| `nameid_format` | `str` | Optional | - |
| `sso_role_matching` | [`List[NacPortalSsoRoleMatching]`](../../doc/models/nac-portal-sso-role-matching.md) | Optional | - |
| `use_sso_role_for_cert` | `bool` | Optional | if it's desired to inject a role into Cert's Subject (so it can be used later on in policy) |

## Example (as JSON)

```json
{
  "idp_cert": "-----BEGIN CERTIFICATE-----\\nMIIFZjCCA06gAwIBAgIIP61/1qm/uDowDQYJKoZIhvcNAQELBQE\\n-----END CERTIFICATE-----",
  "idp_sign_algo": "sha256",
  "idp_sso_url": "https://yourorg.onelogin.com/trust/saml2/http-post/sso/138130",
  "issuer": "https://app.onelogin.com/saml/metadata/138130",
  "nameid_format": "email"
}
```

