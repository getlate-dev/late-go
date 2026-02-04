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

## SDK Reference

### Posts
| Method | Description |
|--------|-------------|
| `client.ListPostsWithResponse()` | List posts visible to the authenticated user |
| `client.BulkUploadPostsWithResponse()` | Validate and schedule multiple posts from CSV |
| `client.CreatePostWithResponse()` | Create a draft, scheduled, or immediate post |
| `client.GetPostWithResponse()` | Get a single post |
| `client.UpdatePostWithResponse()` | Update a post |
| `client.DeletePostWithResponse()` | Delete a post |
| `client.RetryPostWithResponse()` | Retry publishing a failed or partial post |

### Accounts
| Method | Description |
|--------|-------------|
| `client.GetAllAccountsHealthWithResponse()` | Check health of all connected accounts |
| `client.ListAccountsWithResponse()` | List connected social accounts |
| `client.GetAccountHealthWithResponse()` | Check health of a specific account |
| `client.GetFollowerStatsWithResponse()` | Get follower stats and growth metrics |
| `client.GetGoogleBusinessReviewsWithResponse()` | Get Google Business Profile reviews |
| `client.GetLinkedInMentionsWithResponse()` | Resolve a LinkedIn profile or company URL to a URN for @mentions |
| `client.UpdateAccountWithResponse()` | Update a social account |
| `client.DeleteAccountWithResponse()` | Disconnect a social account |

### Profiles
| Method | Description |
|--------|-------------|
| `client.ListProfilesWithResponse()` | List profiles visible to the authenticated user |
| `client.CreateProfileWithResponse()` | Create a new profile |
| `client.GetProfileWithResponse()` | Get a profile by id |
| `client.UpdateProfileWithResponse()` | Update a profile |
| `client.DeleteProfileWithResponse()` | Delete a profile (must have no connected accounts) |

### Analytics
| Method | Description |
|--------|-------------|
| `client.GetAnalyticsWithResponse()` | Unified analytics for posts |
| `client.GetLinkedInAggregateAnalyticsWithResponse()` | Get aggregate analytics for a LinkedIn personal account |
| `client.GetLinkedInPostAnalyticsWithResponse()` | Get analytics for a specific LinkedIn post by URN |
| `client.GetYouTubeDailyViewsWithResponse()` | YouTube daily views breakdown |

### Account Groups
| Method | Description |
|--------|-------------|
| `client.ListAccountGroupsWithResponse()` | List account groups for the authenticated user |
| `client.CreateAccountGroupWithResponse()` | Create a new account group |
| `client.UpdateAccountGroupWithResponse()` | Update an account group |
| `client.DeleteAccountGroupWithResponse()` | Delete an account group |

### Queue
| Method | Description |
|--------|-------------|
| `client.ListQueueSlotsWithResponse()` | Get queue schedules for a profile |
| `client.CreateQueueSlotWithResponse()` | Create a new queue for a profile |
| `client.GetNextQueueSlotWithResponse()` | Preview the next available queue slot (informational only) |
| `client.UpdateQueueSlotWithResponse()` | Create or update a queue schedule |
| `client.DeleteQueueSlotWithResponse()` | Delete a queue schedule |
| `client.PreviewQueueWithResponse()` | Preview upcoming queue slots for a profile |

### Webhooks
| Method | Description |
|--------|-------------|
| `client.CreateWebhookSettingsWithResponse()` | Create a new webhook |
| `client.GetWebhookLogsWithResponse()` | Get webhook delivery logs |
| `client.GetWebhookSettingsWithResponse()` | List all webhooks |
| `client.UpdateWebhookSettingsWithResponse()` | Update a webhook |
| `client.DeleteWebhookSettingsWithResponse()` | Delete a webhook |
| `client.TestWebhookWithResponse()` | Send test webhook |

### API Keys
| Method | Description |
|--------|-------------|
| `client.ListApiKeysWithResponse()` | List API keys for the current user |
| `client.CreateApiKeyWithResponse()` | Create a new API key |
| `client.DeleteApiKeyWithResponse()` | Delete an API key |

### Media
| Method | Description |
|--------|-------------|
| `client.GetMediaPresignedUrlWithResponse()` | Get a presigned URL for direct file upload (up to 5GB) |

### Tools
| Method | Description |
|--------|-------------|
| `client.GetYouTubeTranscriptWithResponse()` | Get YouTube video transcript |
| `client.CheckInstagramHashtagsWithResponse()` | Check Instagram hashtags for bans |
| `client.DownloadBlueskyMediaWithResponse()` | Download Bluesky video |
| `client.DownloadFacebookVideoWithResponse()` | Download Facebook video |
| `client.DownloadInstagramMediaWithResponse()` | Download Instagram reel or post |
| `client.DownloadLinkedInVideoWithResponse()` | Download LinkedIn video |
| `client.DownloadTikTokVideoWithResponse()` | Download TikTok video |
| `client.DownloadTwitterMediaWithResponse()` | Download Twitter/X video |
| `client.DownloadYouTubeVideoWithResponse()` | Download YouTube video or audio |

### Users
| Method | Description |
|--------|-------------|
| `client.ListUsersWithResponse()` | List team users (root + invited) |
| `client.GetUserWithResponse()` | Get user by id (self or invited) |

### Usage
| Method | Description |
|--------|-------------|
| `client.GetUsageStatsWithResponse()` | Get plan and usage stats for current account |

### Logs
| Method | Description |
|--------|-------------|
| `client.ListLogsWithResponse()` | Get publishing logs |
| `client.GetLogWithResponse()` | Get a single log entry |
| `client.GetPostLogsWithResponse()` | Get logs for a specific post |

### Connect (OAuth)
| Method | Description |
|--------|-------------|
| `client.ListFacebookPagesWithResponse()` | List Facebook Pages after OAuth (Headless Mode) |
| `client.ListGoogleBusinessLocationsWithResponse()` | List Google Business Locations after OAuth (Headless Mode) |
| `client.ListLinkedInOrganizationsWithResponse()` | Fetch full LinkedIn organization details (Headless Mode) |
| `client.ListPinterestBoardsForSelectionWithResponse()` | List Pinterest Boards after OAuth (Headless Mode) |
| `client.ListSnapchatProfilesWithResponse()` | List Snapchat Public Profiles after OAuth (Headless Mode) |
| `client.GetConnectUrlWithResponse()` | Start OAuth connection for a platform |
| `client.GetFacebookPagesWithResponse()` | List available Facebook pages for a connected account |
| `client.GetGmbLocationsWithResponse()` | List available Google Business Profile locations for a connected account |
| `client.GetLinkedInOrganizationsWithResponse()` | Get available LinkedIn organizations for a connected account |
| `client.GetPendingOAuthDataWithResponse()` | Fetch pending OAuth selection data (Headless Mode) |
| `client.GetPinterestBoardsWithResponse()` | List Pinterest boards for a connected account |
| `client.GetRedditSubredditsWithResponse()` | List Reddit subreddits for a connected account |
| `client.GetTelegramConnectStatusWithResponse()` | Generate Telegram access code |
| `client.UpdateFacebookPageWithResponse()` | Update selected Facebook page for a connected account |
| `client.UpdateGmbLocationWithResponse()` | Update selected Google Business Profile location for a connected account |
| `client.UpdateLinkedInOrganizationWithResponse()` | Switch LinkedIn account type (personal/organization) |
| `client.UpdatePinterestBoardsWithResponse()` | Set default Pinterest board on the connection |
| `client.UpdateRedditSubredditsWithResponse()` | Set default subreddit on the connection |
| `client.CompleteTelegramConnectWithResponse()` | Check Telegram connection status |
| `client.ConnectBlueskyCredentialsWithResponse()` | Connect Bluesky using app password |
| `client.HandleOAuthCallbackWithResponse()` | Complete OAuth token exchange manually (for server-side flows) |
| `client.InitiateTelegramConnectWithResponse()` | Direct Telegram connection (power users) |
| `client.SelectFacebookPageWithResponse()` | Select a Facebook Page to complete the connection (Headless Mode) |
| `client.SelectGoogleBusinessLocationWithResponse()` | Select a Google Business location to complete the connection (Headless Mode) |
| `client.SelectLinkedInOrganizationWithResponse()` | Select LinkedIn organization or personal account after OAuth |
| `client.SelectPinterestBoardWithResponse()` | Select a Pinterest Board to complete the connection (Headless Mode) |
| `client.SelectSnapchatProfileWithResponse()` | Select a Snapchat Public Profile to complete the connection (Headless Mode) |

### Reddit
| Method | Description |
|--------|-------------|
| `client.GetRedditFeedWithResponse()` | Fetch subreddit feed via a connected account |
| `client.SearchRedditWithResponse()` | Search Reddit posts via a connected account |

### Comments (Inbox)
| Method | Description |
|--------|-------------|
| `client.ListInboxCommentsWithResponse()` | List posts with comments across all accounts |
| `client.GetInboxPostCommentsWithResponse()` | Get comments for a post |
| `client.DeleteInboxCommentWithResponse()` | Delete a comment |
| `client.HideInboxCommentWithResponse()` | Hide a comment |
| `client.LikeInboxCommentWithResponse()` | Like a comment |
| `client.ReplyToInboxPostWithResponse()` | Reply to a post or comment |
| `client.SendPrivateReplyToCommentWithResponse()` | Send private reply to comment author |
| `client.UnhideInboxCommentWithResponse()` | Unhide a comment |
| `client.UnlikeInboxCommentWithResponse()` | Unlike a comment |

### Messages (Inbox)
| Method | Description |
|--------|-------------|
| `client.ListInboxConversationsWithResponse()` | List conversations across all accounts |
| `client.GetInboxConversationWithResponse()` | Get conversation details |
| `client.GetInboxConversationMessagesWithResponse()` | Get messages in a conversation |
| `client.UpdateInboxConversationWithResponse()` | Update conversation status |
| `client.SendInboxMessageWithResponse()` | Send a message |

### Reviews (Inbox)
| Method | Description |
|--------|-------------|
| `client.ListInboxReviewsWithResponse()` | List reviews across all accounts |
| `client.DeleteInboxReviewReplyWithResponse()` | Delete a review reply |
| `client.ReplyToInboxReviewWithResponse()` | Reply to a review |

### Invites
| Method | Description |
|--------|-------------|
| `client.CreateInviteTokenWithResponse()` | Create a team member invite token |

## Documentation

- [API Reference](https://docs.getlate.dev/api-reference)
- [Getting Started Guide](https://docs.getlate.dev/quickstart)

## License

MIT
