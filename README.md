# Late Go SDK

Official Go client library for the [Late API](https://docs.getlate.dev) - Schedule and manage social media posts across multiple platforms.

## Installation

```bash
go get github.com/getlate-dev/late-go
```

## Quick Start

```go
package main

import (
    "context"
    "fmt"
    "log"

    late "github.com/getlate-dev/late-go/late"
)

func main() {
    client, err := late.NewClientWithResponses("https://api.getlate.dev",
        late.WithRequestEditorFn(func(ctx context.Context, req *http.Request) error {
            req.Header.Set("Authorization", "Bearer YOUR_API_KEY")
            return nil
        }),
    )
    if err != nil {
        log.Fatal(err)
    }

    // List accounts
    resp, err := client.ListAccountsWithResponse(context.Background(), nil)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Accounts: %+v\n", resp.JSON200)
}
```

## Documentation

- [API Reference](https://docs.getlate.dev/api-reference)
- [Getting Started Guide](https://docs.getlate.dev/quickstart)

## License

MIT
