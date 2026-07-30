# Migration Guide

## v0.0.x → v0.1.0 (oapi-codegen → openapi-generator)

`v0.1.0` switches the SDK to a new code generator
([openapi-generator](https://openapi-generator.tech)). This is a **breaking**
release: the generated API surface is completely different.

**The import path is unchanged** — you still import:

```go
import zernio "github.com/zernio-dev/zernio-go/zernio"
```

Only the way you build the client and call endpoints changes.

> **Staying on the old client:** `v0.0.285` is the last release on the previous
> generator and remains published. Pin it
> (`go get github.com/zernio-dev/zernio-go@v0.0.285`) to keep your current code
> working until you're ready to migrate.

---

### 1. Client construction & authentication

Functional options are gone. Construct an `APIClient` from a `Configuration`,
and pass your Bearer API key through the request **context**.

```go
// before (v0.0.x)
client, err := zernio.NewClientWithResponses("https://api.zernio.com",
    zernio.WithRequestEditorFn(func(ctx context.Context, req *http.Request) error {
        req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
        return nil
    }),
)
if err != nil {
    log.Fatal(err)
}

// after (v0.1.0)
client := zernio.NewAPIClient(zernio.NewConfiguration()) // base URL https://zernio.com/api from the spec
ctx := context.WithValue(context.Background(), zernio.ContextAccessToken, "YOUR_API_KEY")
```

To override the base URL (e.g. for local development), set it on the
configuration before constructing the client:

```go
cfg := zernio.NewConfiguration()
cfg.Servers = zernio.ServerConfigurations{{URL: "http://localhost:3000/api"}}
client := zernio.NewAPIClient(cfg)
```

### 2. Calling endpoints

Methods are now grouped under a service field on the client, use a request
builder for parameters/body, and finish with `.Execute()`.

```go
// before
resp, err := client.ListAccountsWithResponse(ctx, nil)
accounts := resp.JSON200

// after
accounts, httpResp, err := client.AccountsAPI.ListAccounts(ctx).Execute()
```

Parameters and request bodies are builder methods on the request value:

```go
// before
resp, err := client.CreatePostWithResponse(ctx, body)

// after
post, httpResp, err := client.PostsAPI.CreatePost(ctx).CreatePostRequest(body).Execute()
```

The `### <Resource>` tables in the [README](./README.md#sdk-reference) list the
exact `client.<Service>API.<Method>(ctx)` call for every endpoint.

### 3. Responses & error handling

The typed `JSON200` / `JSONxxx` fields are gone. Each call returns three values:

```go
result, httpResp, err := client.AccountsAPI.ListAccounts(ctx).Execute()
//      ^ decoded model   ^ *http.Response   ^ error
```

- `err` is non-nil on transport errors and on non-2xx responses.
- Inspect `httpResp.StatusCode` for the HTTP status instead of switching on
  `resp.JSONxxx`.

### 4. Renamed field

`ReviewWebhookReview.HasReply` is now `ReviewWebhookReview.Replied`. The JSON
wire name is unchanged (`hasReply`), so serialization is unaffected — only the
Go field name changed (it previously collided with a generated helper method).

---

### Versioning going forward

`v0.1.0` is a one-time manual, breaking release. Subsequent regenerations from
the spec are additive and ship as automatic patch bumps (`v0.1.1`, `v0.1.2`, …),
with one exception so far: the enum constant rename below.

---

## Prefixed enum constants

Applies from the first release regenerated after `v0.1.160`. This is a
**breaking rename** for code that referenced the constants directly.

Package-level enum constants are now prefixed with the uppercased Go type name.
The generator emits them at package scope, so two enums that share a value could
not coexist (`AdStatus` and `AdReviewStatus` both have `rejected`, which made the
SDK fail to compile once `AdReviewStatus` was added to the API).

The types, their values, the JSON wire format, `Allowed<Type>EnumValues`,
`New<Type>FromValue()` and `IsValid()` are all unchanged. Only references to the
constants need updating:

| Before | After |
|--------|-------|
| `zernio.ACTIVE` | `zernio.ADSTATUS_ACTIVE` |
| `zernio.PAUSED` | `zernio.ADSTATUS_PAUSED` |
| `zernio.PENDING_REVIEW` | `zernio.ADSTATUS_PENDING_REVIEW` |
| `zernio.REJECTED` | `zernio.ADSTATUS_REJECTED` |
| `zernio.COMPLETED` | `zernio.ADSTATUS_COMPLETED` |
| `zernio.CANCELLED` | `zernio.ADSTATUS_CANCELLED` |
| `zernio.ERROR` | `zernio.ADSTATUS_ERROR` |
| `zernio.LOWEST_COST_WITHOUT_CAP` | `zernio.BIDSTRATEGY_LOWEST_COST_WITHOUT_CAP` |
| `zernio.LOWEST_COST_WITH_BID_CAP` | `zernio.BIDSTRATEGY_LOWEST_COST_WITH_BID_CAP` |
| `zernio.COST_CAP` | `zernio.BIDSTRATEGY_COST_CAP` |
| `zernio.LOWEST_COST_WITH_MIN_ROAS` | `zernio.BIDSTRATEGY_LOWEST_COST_WITH_MIN_ROAS` |

Code that passes the raw string (`"rejected"`) or goes through
`zernio.NewAdStatusFromValue("rejected")` needs no change.
