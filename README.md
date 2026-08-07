# Zernio Go SDK

Official Go client library for the [Zernio API](https://docs.zernio.com) - Schedule and manage social media posts across multiple platforms.

## Installation

```bash
go get github.com/zernio-dev/zernio-go
```

> **Upgrading from `v0.0.x`?** `v0.1.0` switches to a new code generator and is
> a breaking change. The import path is unchanged, but client construction and
> method calls differ — see [MIGRATION.md](./MIGRATION.md).

> **Using enum constants?** They are now prefixed with their type
> (`zernio.ADSTATUS_REJECTED`, not `zernio.REJECTED`), see
> [MIGRATION.md](./MIGRATION.md#prefixed-enum-constants).

## Quick Start

```go
package main

import (
    "context"
    "fmt"
    "log"

    zernio "github.com/zernio-dev/zernio-go/zernio"
)

func main() {
    // Defaults to the https://zernio.com/api base URL from the spec.
    client := zernio.NewAPIClient(zernio.NewConfiguration())

    // Authenticate with your Bearer API key via the request context.
    ctx := context.WithValue(context.Background(), zernio.ContextAccessToken, "YOUR_API_KEY")

    // List accounts
    accounts, _, err := client.AccountsAPI.ListAccounts(ctx).Execute()
    if err != nil {
        log.Fatal(err)
    }
    fmt.Printf("Accounts: %+v\n", accounts)
}
```

## SDK Reference

### Posts
| Method | Description |
|--------|-------------|
| `client.PostsAPI.ListPosts(ctx)` | List posts |
| `client.PostsAPI.BulkUploadPosts(ctx)` | Bulk upload from CSV |
| `client.PostsAPI.CreatePost(ctx)` | Create post |
| `client.PostsAPI.GetPost(ctx)` | Get post |
| `client.PostsAPI.UpdatePost(ctx)` | Update post |
| `client.PostsAPI.UpdatePostMetadata(ctx)` | Update post metadata |
| `client.PostsAPI.DeletePost(ctx)` | Delete post |
| `client.PostsAPI.EditPost(ctx)` | Edit published post |
| `client.PostsAPI.RetryPost(ctx)` | Retry failed post |
| `client.PostsAPI.UnpublishPost(ctx)` | Unpublish post |

### Accounts
| Method | Description |
|--------|-------------|
| `client.AccountsAPI.GetAllAccountsHealth(ctx)` | Check accounts health |
| `client.AccountsAPI.ListAccounts(ctx)` | List accounts |
| `client.AccountsAPI.GetAccountHealth(ctx)` | Check account health |
| `client.AccountsAPI.GetFollowerStats(ctx)` | Get follower stats |
| `client.GMBReviewsAPI.GetGoogleBusinessReviews(ctx)` | Get reviews |
| `client.AccountsAPI.GetInstagramFollowStatus(ctx)` | Check whether an Instagram user follows the account |
| `client.LinkedInMentionsAPI.GetLinkedInMentions(ctx)` | Resolve LinkedIn mention |
| `client.AccountsAPI.GetSlackSettings(ctx)` | Get Slack account settings |
| `client.AccountsAPI.GetTikTokCreatorInfo(ctx)` | Get TikTok creator info |
| `client.AccountsAPI.UpdateAccount(ctx)` | Update account |
| `client.AccountsAPI.UpdateSlackSettings(ctx)` | Update Slack account settings |
| `client.AccountsAPI.DeleteAccount(ctx)` | Disconnect account |
| `client.GMBReviewsAPI.DeleteGoogleBusinessReviewReply(ctx)` | Delete a review reply |
| `client.GMBReviewsAPI.BatchGetGoogleBusinessReviews(ctx)` | Batch get reviews |
| `client.AccountsAPI.MoveAccountToProfile(ctx)` | Move account to another profile |
| `client.GMBReviewsAPI.ReplyToGoogleBusinessReview(ctx)` | Reply to a review |

### Profiles
| Method | Description |
|--------|-------------|
| `client.ProfilesAPI.ListProfiles(ctx)` | List profiles |
| `client.ProfilesAPI.CreateProfile(ctx)` | Create profile |
| `client.ProfilesAPI.GetProfile(ctx)` | Get profile |
| `client.ProfilesAPI.UpdateProfile(ctx)` | Update profile |
| `client.ProfilesAPI.DeleteProfile(ctx)` | Delete profile |

### Analytics
| Method | Description |
|--------|-------------|
| `client.AnalyticsAPI.GetAnalytics(ctx)` | Get post analytics |
| `client.AnalyticsAPI.GetBestTimeToPost(ctx)` | Get best times to post |
| `client.AnalyticsAPI.GetContentDecay(ctx)` | Get content performance decay |
| `client.AnalyticsAPI.GetDailyMetrics(ctx)` | Get daily aggregated metrics |
| `client.AnalyticsAPI.GetFacebookPageInsights(ctx)` | Get Facebook Page insights |
| `client.AnalyticsAPI.GetFacebookPostEarnings(ctx)` | Get Facebook post monetization earnings |
| `client.AnalyticsAPI.GetFacebookPostReactions(ctx)` | Get Facebook post reactions |
| `client.AnalyticsAPI.GetGoogleBusinessPerformance(ctx)` | Get GBP performance metrics |
| `client.AnalyticsAPI.GetGoogleBusinessSearchKeywords(ctx)` | Get GBP search keywords |
| `client.AnalyticsAPI.GetInstagramAccountInsights(ctx)` | Get Instagram insights |
| `client.AnalyticsAPI.GetInstagramDemographics(ctx)` | Get Instagram demographics |
| `client.AnalyticsAPI.GetInstagramFollowerHistory(ctx)` | Get Instagram follower history |
| `client.AnalyticsAPI.GetLinkedInAggregateAnalytics(ctx)` | Get LinkedIn aggregate stats |
| `client.AnalyticsAPI.GetLinkedInOrgAggregateAnalytics(ctx)` | Get LinkedIn org analytics |
| `client.AnalyticsAPI.GetLinkedInPostAnalytics(ctx)` | Get LinkedIn post stats |
| `client.AnalyticsAPI.GetLinkedInPostReactions(ctx)` | Get LinkedIn post reactions |
| `client.AnalyticsAPI.GetPostTimeline(ctx)` | Get post analytics timeline |
| `client.AnalyticsAPI.GetPostingFrequency(ctx)` | Get frequency vs engagement |
| `client.AnalyticsAPI.GetTikTokAccountInsights(ctx)` | Get TikTok account-level insights |
| `client.AnalyticsAPI.GetYouTubeChannelInsights(ctx)` | Get YouTube channel insights |
| `client.AnalyticsAPI.GetYouTubeDailyViews(ctx)` | Get YouTube daily views |
| `client.AnalyticsAPI.GetYouTubeDemographics(ctx)` | Get YouTube demographics |
| `client.AnalyticsAPI.GetYouTubeVideoRetention(ctx)` | Get YouTube video retention curve |
| `client.AnalyticsAPI.SyncExternalPosts(ctx)` | Sync an external post |

### Account Groups
| Method | Description |
|--------|-------------|
| `client.AccountGroupsAPI.ListAccountGroups(ctx)` | List groups |
| `client.AccountGroupsAPI.CreateAccountGroup(ctx)` | Create group |
| `client.AccountGroupsAPI.UpdateAccountGroup(ctx)` | Update group |
| `client.AccountGroupsAPI.DeleteAccountGroup(ctx)` | Delete group |

### Queue
| Method | Description |
|--------|-------------|
| `client.QueueAPI.ListQueueSlots(ctx)` | List schedules |
| `client.QueueAPI.CreateQueueSlot(ctx)` | Create schedule |
| `client.QueueAPI.GetNextQueueSlot(ctx)` | Get next available slot |
| `client.QueueAPI.UpdateQueueSlot(ctx)` | Update schedule |
| `client.QueueAPI.DeleteQueueSlot(ctx)` | Delete schedule |
| `client.QueueAPI.PreviewQueue(ctx)` | Preview upcoming slots |

### Webhooks
| Method | Description |
|--------|-------------|
| `client.WebhooksAPI.CreateWebhookSettings(ctx)` | Create webhook |
| `client.WebhooksAPI.GetWebhookLogs(ctx)` | List webhook delivery logs |
| `client.WebhooksAPI.GetWebhookSettings(ctx)` | List webhooks |
| `client.WebhooksAPI.UpdateWebhookSettings(ctx)` | Update webhook |
| `client.WebhooksAPI.DeleteWebhookSettings(ctx)` | Delete webhook |
| `client.WebhooksAPI.TestWebhook(ctx)` | Send test webhook |

### API Keys
| Method | Description |
|--------|-------------|
| `client.APIKeysAPI.ListApiKeys(ctx)` | List keys |
| `client.APIKeysAPI.CreateApiKey(ctx)` | Create key |
| `client.APIKeysAPI.DeleteApiKey(ctx)` | Delete key |
| `client.APIKeysAPI.VerifyCredential(ctx)` | Verify credential |

### Media
| Method | Description |
|--------|-------------|
| `client.MediaAPI.GetMediaPresignedUrl(ctx)` | Get upload URL |

### Users
| Method | Description |
|--------|-------------|
| `client.UsersAPI.ListUsers(ctx)` | List users |
| `client.UsersAPI.GetUser(ctx)` | Get user |

### Usage
| Method | Description |
|--------|-------------|
| `client.UsageAPI.GetBilling(ctx)` | Account billing snapshot (plan, cycle, balance, caps, status) |
| `client.UsageAPI.GetCallsUsage(ctx)` | Calling usage and cost |
| `client.UsageAPI.GetSmsUsage(ctx)` | SMS usage (volumes) |
| `client.UsageAPI.GetUsage(ctx)` | Usage snapshot (default) or billed-spend metering (with params) |
| `client.UsageAPI.GetUsageStats(ctx)` | Get plan and usage snapshot (plan, limits, payment status) |
| `client.UsageAPI.GetXApiPricing(ctx)` | Get X/Twitter API pricing table |

### Logs
| Method | Description |
|--------|-------------|
| `client.LogsAPI.ListLogs(ctx)` | List activity logs |

### Connect (OAuth)
| Method | Description |
|--------|-------------|
| `client.ConnectAPI.ListFacebookPages(ctx)` | List Facebook pages |
| `client.ConnectAPI.ListGoogleBusinessLocations(ctx)` | List GBP locations |
| `client.ConnectAPI.ListLinkedInOrganizations(ctx)` | List LinkedIn orgs |
| `client.ConnectAPI.ListPinterestBoardsForSelection(ctx)` | List Pinterest boards |
| `client.ConnectAPI.ListSnapchatProfiles(ctx)` | List Snapchat profiles |
| `client.ConnectAPI.ListWhatsAppPhoneNumbers(ctx)` | List numbers for selection |
| `client.ConnectAPI.CreatePinterestBoard(ctx)` | Create Pinterest board |
| `client.ConnectAPI.GetConnectUrl(ctx)` | Get OAuth connect URL |
| `client.ConnectAPI.GetFacebookPages(ctx)` | List Facebook pages |
| `client.ConnectAPI.GetGmbLocations(ctx)` | List GBP locations |
| `client.ConnectAPI.GetLinkedInOrganizations(ctx)` | List LinkedIn orgs |
| `client.ConnectAPI.GetPendingOAuthData(ctx)` | Get pending OAuth data |
| `client.ConnectAPI.GetPinterestBoards(ctx)` | List Pinterest boards |
| `client.ConnectAPI.GetRedditFlairs(ctx)` | List subreddit flairs |
| `client.ConnectAPI.GetRedditSubreddits(ctx)` | List Reddit subreddits |
| `client.ConnectAPI.GetSubredditRules(ctx)` | Get subreddit rules |
| `client.ConnectAPI.GetTelegramConnectStatus(ctx)` | Generate Telegram code |
| `client.ConnectAPI.GetYoutubePlaylists(ctx)` | List YouTube playlists |
| `client.ConnectAPI.UpdateFacebookPage(ctx)` | Update Facebook page |
| `client.ConnectAPI.UpdateGmbLocation(ctx)` | Update GBP location |
| `client.ConnectAPI.UpdateLinkedInOrganization(ctx)` | Switch LinkedIn account type |
| `client.ConnectAPI.UpdatePinterestBoards(ctx)` | Set default Pinterest board |
| `client.ConnectAPI.UpdateRedditSubreddits(ctx)` | Set default subreddit |
| `client.ConnectAPI.UpdateYoutubeDefaultPlaylist(ctx)` | Set default YouTube playlist |
| `client.ConnectAPI.AssignGoogleBusinessLocation(ctx)` | Assign GBP location to another profile |
| `client.ConnectAPI.CompleteTelegramConnect(ctx)` | Check Telegram status |
| `client.ConnectAPI.CompleteWhatsAppPhoneSelection(ctx)` | Complete number selection |
| `client.ConnectAPI.ConfigureTikTokAdsBrandIdentity(ctx)` | Set TikTok brand identity |
| `client.ConnectAPI.ConnectAds(ctx)` | Connect ads for a platform |
| `client.ConnectAPI.ConnectBlueskyCredentials(ctx)` | Connect Bluesky account |
| `client.ConnectAPI.ConnectOpenAIAdsCredentials(ctx)` | Connect an OpenAI Ads account |
| `client.ConnectAPI.ConnectWhatsAppCredentials(ctx)` | Connect WhatsApp via credentials |
| `client.ConnectAPI.HandleOAuthCallback(ctx)` | Complete OAuth callback |
| `client.ConnectAPI.InitiateTelegramConnect(ctx)` | Connect Telegram directly |
| `client.ConnectAPI.SelectFacebookPage(ctx)` | Select Facebook page |
| `client.ConnectAPI.SelectGoogleBusinessLocation(ctx)` | Select GBP location |
| `client.ConnectAPI.SelectLinkedInOrganization(ctx)` | Select LinkedIn org |
| `client.ConnectAPI.SelectPinterestBoard(ctx)` | Select Pinterest board |
| `client.ConnectAPI.SelectSnapchatProfile(ctx)` | Select Snapchat profile |
| `client.ConnectAPI.SetRedditPostFlair(ctx)` | Set Reddit post flair |
| `client.ConnectAPI.VoteRedditThing(ctx)` | Vote on a Reddit post or comment |

### Reddit
| Method | Description |
|--------|-------------|
| `client.RedditSearchAPI.GetRedditFeed(ctx)` | Get subreddit feed |
| `client.RedditSearchAPI.SearchReddit(ctx)` | Search posts |

### Account Settings
| Method | Description |
|--------|-------------|
| `client.AccountSettingsAPI.GetInstagramIceBreakers(ctx)` | Get IG ice breakers |
| `client.AccountSettingsAPI.GetMessengerMenu(ctx)` | Get FB persistent menu |
| `client.AccountSettingsAPI.GetTelegramCommands(ctx)` | Get TG bot commands |
| `client.AccountSettingsAPI.DeleteInstagramIceBreakers(ctx)` | Delete IG ice breakers |
| `client.AccountSettingsAPI.DeleteMessengerMenu(ctx)` | Delete FB persistent menu |
| `client.AccountSettingsAPI.DeleteTelegramCommands(ctx)` | Delete TG bot commands |
| `client.AccountSettingsAPI.SetInstagramIceBreakers(ctx)` | Set IG ice breakers |
| `client.AccountSettingsAPI.SetMessengerMenu(ctx)` | Set FB persistent menu |
| `client.AccountSettingsAPI.SetTelegramCommands(ctx)` | Set TG bot commands |

### Ad Accounts
| Method | Description |
|--------|-------------|
| `client.AdAccountsAPI.ListAdAccounts(ctx)` | List ad accounts |
| `client.AdAccountsAPI.ListAdLabels(ctx)` | Ad labels |
| `client.AdAccountsAPI.ListAdStudies(ctx)` | A/B tests and lift studies |
| `client.AdAccountsAPI.ListAdsBusinessCenters(ctx)` | List TikTok Business Centers |
| `client.AdAccountsAPI.ListHighDemandPeriods(ctx)` | High demand periods / budget schedules |
| `client.AdAccountsAPI.ListMetaBusinesses(ctx)` | Businesses list |
| `client.AdAccountsAPI.ListValueRuleSets(ctx)` | List value rule sets |
| `client.AdAccountsAPI.CreateValueRuleSet(ctx)` | Create a value rule set |
| `client.AdAccountsAPI.GetAdAccountFinance(ctx)` | Ad account finances |
| `client.AdAccountsAPI.GetAdComments(ctx)` | List comments on an ad |
| `client.AdAccountsAPI.GetAdsActivityLog(ctx)` | Ad account change / audit log |
| `client.AdAccountsAPI.GetDsaDefaults(ctx)` | Get ad account DSA defaults |
| `client.AdAccountsAPI.GetDsaRecommendations(ctx)` | List DSA beneficiary/payor suggestions |
| `client.AdAccountsAPI.GetValueRuleSet(ctx)` | Read a value rule set |
| `client.AdAccountsAPI.UpdateAdAccount(ctx)` | Update ad account settings |
| `client.AdAccountsAPI.UpdateValueRuleSet(ctx)` | Replace a value rule set |
| `client.AdAccountsAPI.DeleteValueRuleSet(ctx)` | Delete a value rule set |

### Ad Audiences
| Method | Description |
|--------|-------------|
| `client.AdAudiencesAPI.ListAdAudiences(ctx)` | List custom audiences |
| `client.AdAudiencesAPI.CreateAdAudience(ctx)` | Create custom audience |
| `client.AdAudiencesAPI.GetAdAudience(ctx)` | Get audience details |
| `client.AdAudiencesAPI.UpdateAdAudience(ctx)` | Update an audience |
| `client.AdAudiencesAPI.DeleteAdAudience(ctx)` | Delete custom audience |
| `client.AdAudiencesAPI.AddUsersToAdAudience(ctx)` | Add users to audience |

### Ad Campaigns
| Method | Description |
|--------|-------------|
| `client.AdCampaignsAPI.ListAdCampaigns(ctx)` | List campaigns |
| `client.AdCampaignsAPI.ListAdKeywords(ctx)` | List Search keywords |
| `client.AdCampaignsAPI.ListAds(ctx)` | List ads |
| `client.AdCampaignsAPI.BulkUpdateAdCampaignStatus(ctx)` | Pause or resume many campaigns |
| `client.AdCampaignsAPI.CreateAdCampaign(ctx)` | Create a standalone campaign |
| `client.AdCampaignsAPI.CreateStandaloneAd(ctx)` | Create standalone ad |
| `client.AdCampaignsAPI.GetAd(ctx)` | Get ad details |
| `client.AdCampaignsAPI.GetAdSetDetails(ctx)` | Live ad-set details incl. learning phase |
| `client.AdCampaignsAPI.GetAdTree(ctx)` | Get campaign tree |
| `client.AdCampaignsAPI.GetAdsTimeline(ctx)` | Get daily account metrics |
| `client.AdCampaignsAPI.UpdateAd(ctx)` | Update ad |
| `client.AdCampaignsAPI.UpdateAdCampaign(ctx)` | Update a campaign |
| `client.AdCampaignsAPI.UpdateAdCampaignStatus(ctx)` | Pause or resume a campaign |
| `client.AdCampaignsAPI.UpdateAdSet(ctx)` | Update an ad set |
| `client.AdCampaignsAPI.UpdateAdSetStatus(ctx)` | Pause or resume a single ad set |
| `client.AdCampaignsAPI.UpdateAdStatus(ctx)` | Pause or resume a single ad |
| `client.AdCampaignsAPI.DeleteAd(ctx)` | Cancel an ad |
| `client.AdCampaignsAPI.DeleteAdCampaign(ctx)` | Delete a campaign |
| `client.AdCampaignsAPI.BoostPost(ctx)` | Boost post as ad |
| `client.AdCampaignsAPI.DuplicateAd(ctx)` | Duplicate an ad |
| `client.AdCampaignsAPI.DuplicateAdCampaign(ctx)` | Duplicate a campaign |
| `client.AdCampaignsAPI.DuplicateAdSet(ctx)` | Duplicate an ad set |

### Ad Creatives
| Method | Description |
|--------|-------------|
| `client.AdCreativesAPI.ListAdCatalogProductSets(ctx)` | List a catalog's product sets |
| `client.AdCreativesAPI.ListAdCatalogs(ctx)` | List Meta product catalogs |
| `client.AdCreativesAPI.ListAdCreatives(ctx)` | Creative library |
| `client.AdCreativesAPI.ListAdImages(ctx)` | Ad image library |
| `client.AdCreativesAPI.CreateAdCreative(ctx)` | Create a standalone creative |
| `client.AdCreativesAPI.GetAdCreative(ctx)` | Creative details |
| `client.AdCreativesAPI.GetAdPreviews(ctx)` | Render previews of an existing ad |
| `client.AdCreativesAPI.UpdateAdCreative(ctx)` | Rename a creative |
| `client.AdCreativesAPI.DeleteAdCreative(ctx)` | Delete a creative |
| `client.AdCreativesAPI.GenerateAdPreviews(ctx)` | Render pre-create ad previews |
| `client.AdCreativesAPI.UploadAdImage(ctx)` | Upload an ad image from base64 |

### Ad Insights
| Method | Description |
|--------|-------------|
| `client.AdInsightsAPI.CreateAdInsightsReport(ctx)` | Submit an async insights report run |
| `client.AdInsightsAPI.GetAdAnalytics(ctx)` | Get ad analytics |
| `client.AdInsightsAPI.GetAdInsightsReport(ctx)` | Poll an async insights report run |
| `client.AdInsightsAPI.GetCampaignAnalytics(ctx)` | Get campaign analytics |
| `client.AdInsightsAPI.GenerateKeywordHistoricalMetrics(ctx)` | Historical keyword metrics (Google Keyword Planner) |
| `client.AdInsightsAPI.GenerateKeywordIdeas(ctx)` | Generate keyword ideas (Google Keyword Planner) |
| `client.AdInsightsAPI.QueryAdInsights(ctx)` | Flexible live insights query |

### Ad Targeting
| Method | Description |
|--------|-------------|
| `client.AdTargetingAPI.GetLinkedInBidPricing(ctx)` | Suggested bid and budget bounds |
| `client.AdTargetingAPI.GetLinkedInSupplyForecast(ctx)` | Impressions, clicks and spend forecast |
| `client.AdTargetingAPI.EstimateAdReach(ctx)` | Estimate audience reach |
| `client.AdTargetingAPI.SearchAdInterests(ctx)` | Search targeting interests |
| `client.AdTargetingAPI.SearchAdTargeting(ctx)` | Search targeting options |

### Broadcasts
| Method | Description |
|--------|-------------|
| `client.BroadcastsAPI.ListBroadcastRecipients(ctx)` | List broadcast recipients |
| `client.BroadcastsAPI.ListBroadcasts(ctx)` | List broadcasts |
| `client.BroadcastsAPI.CreateBroadcast(ctx)` | Create broadcast draft |
| `client.BroadcastsAPI.GetBroadcast(ctx)` | Get broadcast details |
| `client.BroadcastsAPI.UpdateBroadcast(ctx)` | Update broadcast |
| `client.BroadcastsAPI.DeleteBroadcast(ctx)` | Delete broadcast |
| `client.BroadcastsAPI.AddBroadcastRecipients(ctx)` | Add recipients to a broadcast |
| `client.BroadcastsAPI.CancelBroadcast(ctx)` | Cancel broadcast |
| `client.BroadcastsAPI.ScheduleBroadcast(ctx)` | Schedule broadcast for later |
| `client.BroadcastsAPI.SendBroadcast(ctx)` | Send broadcast now |

### Calls
| Method | Description |
|--------|-------------|
| `client.CallsAPI.ListCalls(ctx)` | List all calls (unified history) |
| `client.CallsAPI.GetCall(ctx)` | Get a call (any channel) |
| `client.CallsAPI.GetCallRecording(ctx)` | Get a call recording |

### Comment Automations
| Method | Description |
|--------|-------------|
| `client.CommentAutomationsAPI.ListCommentAutomationLogs(ctx)` | List automation logs |
| `client.CommentAutomationsAPI.ListCommentAutomations(ctx)` | List comment-to-DM automations |
| `client.CommentAutomationsAPI.CreateCommentAutomation(ctx)` | Create comment-to-DM automation |
| `client.CommentAutomationsAPI.GetCommentAutomation(ctx)` | Get automation details |
| `client.CommentAutomationsAPI.UpdateCommentAutomation(ctx)` | Update automation settings |
| `client.CommentAutomationsAPI.DeleteCommentAutomation(ctx)` | Delete automation |

### Comments (Inbox)
| Method | Description |
|--------|-------------|
| `client.CommentsAPI.ListInboxComments(ctx)` | List commented posts |
| `client.CommentsAPI.GetInboxPostComments(ctx)` | Get post comments |
| `client.CommentsAPI.DeleteInboxComment(ctx)` | Delete comment |
| `client.CommentsAPI.EditInboxComment(ctx)` | Edit comment |
| `client.CommentsAPI.HideInboxComment(ctx)` | Hide comment |
| `client.CommentsAPI.LikeInboxComment(ctx)` | Like comment |
| `client.CommentsAPI.ReplyToInboxPost(ctx)` | Reply to comment |
| `client.CommentsAPI.SendPrivateReplyToComment(ctx)` | Send private reply |
| `client.CommentsAPI.SetCommentModeration(ctx)` | Set comment moderation status |
| `client.CommentsAPI.UnhideInboxComment(ctx)` | Unhide comment |
| `client.CommentsAPI.UnlikeInboxComment(ctx)` | Unlike comment |

### Connected Apps
| Method | Description |
|--------|-------------|
| `client.ConnectedAppsAPI.ListConnectedApps(ctx)` | List connected apps |
| `client.ConnectedAppsAPI.RevokeConnectedApp(ctx)` | Revoke connected app |

### Contacts
| Method | Description |
|--------|-------------|
| `client.ContactsAPI.ListContacts(ctx)` | List contacts |
| `client.ContactsAPI.BulkCreateContacts(ctx)` | Bulk create contacts |
| `client.ContactsAPI.CreateContact(ctx)` | Create contact |
| `client.ContactsAPI.GetContact(ctx)` | Get contact |
| `client.ContactsAPI.GetContactChannels(ctx)` | List channels for a contact |
| `client.ContactsAPI.UpdateContact(ctx)` | Update contact |
| `client.ContactsAPI.DeleteContact(ctx)` | Delete contact |

### Conversions
| Method | Description |
|--------|-------------|
| `client.ConversionsAPI.ListConversionAssociations(ctx)` | List associated campaigns |
| `client.ConversionsAPI.ListConversionDestinations(ctx)` | List conversion destinations |
| `client.ConversionsAPI.CreateConversionDestination(ctx)` | Create a conversion destination |
| `client.ConversionsAPI.GetConversionDestination(ctx)` | Get a conversion destination |
| `client.ConversionsAPI.GetConversionMetrics(ctx)` | Get attribution metrics |
| `client.ConversionsAPI.GetConversionsQuality(ctx)` | Get Event Match Quality |
| `client.ConversionsAPI.UpdateConversionDestination(ctx)` | Update a conversion destination |
| `client.ConversionsAPI.DeleteConversionDestination(ctx)` | Delete a conversion destination |
| `client.ConversionsAPI.AddConversionAssociations(ctx)` | Associate campaigns |
| `client.ConversionsAPI.AdjustConversions(ctx)` | Adjust uploaded conversions |
| `client.ConversionsAPI.RemoveConversionAssociations(ctx)` | Remove associated campaigns |
| `client.ConversionsAPI.SendConversions(ctx)` | Send conversion events |

### Custom Fields
| Method | Description |
|--------|-------------|
| `client.CustomFieldsAPI.ListCustomFields(ctx)` | List custom field definitions |
| `client.CustomFieldsAPI.CreateCustomField(ctx)` | Create custom field |
| `client.CustomFieldsAPI.UpdateCustomField(ctx)` | Update custom field |
| `client.CustomFieldsAPI.DeleteCustomField(ctx)` | Delete custom field |
| `client.CustomFieldsAPI.ClearContactFieldValue(ctx)` | Clear custom field value |
| `client.CustomFieldsAPI.SetContactFieldValue(ctx)` | Set custom field value |

### Discord
| Method | Description |
|--------|-------------|
| `client.DiscordAPI.ListDiscordGuildMembers(ctx)` | List Discord guild members |
| `client.DiscordAPI.ListDiscordGuildRoles(ctx)` | List Discord guild roles |
| `client.DiscordAPI.ListDiscordPinnedMessages(ctx)` | List pinned messages |
| `client.DiscordAPI.ListDiscordScheduledEvents(ctx)` | List Discord scheduled events |
| `client.DiscordAPI.CreateDiscordGuildRole(ctx)` | Create a Discord guild role |
| `client.DiscordAPI.CreateDiscordScheduledEvent(ctx)` | Create a Discord scheduled event |
| `client.DiscordAPI.CreateDiscordThread(ctx)` | Create a Discord public thread |
| `client.DiscordAPI.GetDiscordChannels(ctx)` | List Discord guild channels |
| `client.DiscordAPI.GetDiscordGuildMember(ctx)` | Get a Discord guild member |
| `client.DiscordAPI.GetDiscordScheduledEvent(ctx)` | Get a Discord scheduled event |
| `client.DiscordAPI.GetDiscordSettings(ctx)` | Get Discord account settings |
| `client.DiscordAPI.UpdateDiscordScheduledEvent(ctx)` | Update a Discord scheduled event |
| `client.DiscordAPI.UpdateDiscordSettings(ctx)` | Update Discord settings |
| `client.DiscordAPI.DeleteDiscordGuildRole(ctx)` | Delete a Discord guild role |
| `client.DiscordAPI.DeleteDiscordMessage(ctx)` | Delete a Discord channel message |
| `client.DiscordAPI.DeleteDiscordScheduledEvent(ctx)` | Delete a Discord scheduled event |
| `client.DiscordAPI.AddDiscordMemberRole(ctx)` | Assign a role to a guild member |
| `client.DiscordAPI.CrosspostDiscordMessage(ctx)` | Crosspost Discord message |
| `client.DiscordAPI.EditDiscordGuildRole(ctx)` | Edit a Discord guild role |
| `client.DiscordAPI.PinDiscordMessage(ctx)` | Pin a Discord message |
| `client.DiscordAPI.RemoveDiscordMemberRole(ctx)` | Remove a role from a guild member |
| `client.DiscordAPI.SearchDiscordGuildMembers(ctx)` | Search Discord guild members |
| `client.DiscordAPI.SendDiscordDirectMessage(ctx)` | Send a Discord Direct Message |
| `client.DiscordAPI.UnpinDiscordMessage(ctx)` | Unpin a Discord message |

### GMB Attributes
| Method | Description |
|--------|-------------|
| `client.GMBAttributesAPI.GetGmbAttributeMetadata(ctx)` | Get attribute metadata |
| `client.GMBAttributesAPI.GetGoogleBusinessAttributes(ctx)` | Get attributes |
| `client.GMBAttributesAPI.UpdateGoogleBusinessAttributes(ctx)` | Update attributes |

### GMB Food Menus
| Method | Description |
|--------|-------------|
| `client.GMBFoodMenusAPI.GetGoogleBusinessFoodMenus(ctx)` | Get food menus |
| `client.GMBFoodMenusAPI.UpdateGoogleBusinessFoodMenus(ctx)` | Update food menus |

### GMB Location Details
| Method | Description |
|--------|-------------|
| `client.GMBLocationDetailsAPI.GetGoogleBusinessLocationDetails(ctx)` | Get location details |
| `client.GMBLocationDetailsAPI.UpdateGoogleBusinessLocationDetails(ctx)` | Update location details |

### GMB Media
| Method | Description |
|--------|-------------|
| `client.GMBMediaAPI.ListGoogleBusinessMedia(ctx)` | List media |
| `client.GMBMediaAPI.CreateGoogleBusinessMedia(ctx)` | Upload photo |
| `client.GMBMediaAPI.DeleteGoogleBusinessMedia(ctx)` | Delete photo |

### GMB Place Actions
| Method | Description |
|--------|-------------|
| `client.GMBPlaceActionsAPI.ListGoogleBusinessPlaceActions(ctx)` | List action links |
| `client.GMBPlaceActionsAPI.CreateGoogleBusinessPlaceAction(ctx)` | Create action link |
| `client.GMBPlaceActionsAPI.UpdateGoogleBusinessPlaceAction(ctx)` | Update action link |
| `client.GMBPlaceActionsAPI.DeleteGoogleBusinessPlaceAction(ctx)` | Delete action link |

### GMB Services
| Method | Description |
|--------|-------------|
| `client.GMBServicesAPI.GetGoogleBusinessServices(ctx)` | Get services |
| `client.GMBServicesAPI.UpdateGoogleBusinessServices(ctx)` | Replace services |

### GMB Verifications
| Method | Description |
|--------|-------------|
| `client.GMBVerificationsAPI.GetGoogleBusinessVerifications(ctx)` | Get verification state |
| `client.GMBVerificationsAPI.CompleteGoogleBusinessVerification(ctx)` | Complete a verification |
| `client.GMBVerificationsAPI.FetchGoogleBusinessVerificationOptions(ctx)` | Fetch verification options |
| `client.GMBVerificationsAPI.StartGoogleBusinessVerification(ctx)` | Start a verification |

### Inbox Analytics
| Method | Description |
|--------|-------------|
| `client.InboxAnalyticsAPI.ListInboxConversationAnalytics(ctx)` | List conversation analytics |
| `client.InboxAnalyticsAPI.GetInboxConversationAnalytics(ctx)` | Get conversation analytics |
| `client.InboxAnalyticsAPI.GetInboxHeatmap(ctx)` | Get day × hour heatmap |
| `client.InboxAnalyticsAPI.GetInboxResponseTime(ctx)` | Get inbox response-time stats |
| `client.InboxAnalyticsAPI.GetInboxSourceBreakdown(ctx)` | Get inbox source breakdown |
| `client.InboxAnalyticsAPI.GetInboxTopAccounts(ctx)` | Get top accounts by inbox volume |
| `client.InboxAnalyticsAPI.GetInboxVolume(ctx)` | Get inbox messaging volume |

### Instagram
| Method | Description |
|--------|-------------|
| `client.InstagramAPI.ListInstagramStories(ctx)` | List active Instagram stories |
| `client.InstagramAPI.GetInstagramPublishingLimit(ctx)` | Get Instagram publishing limit |
| `client.InstagramAPI.GetInstagramStoryInsights(ctx)` | Get Instagram story insights |

### Lead Gen
| Method | Description |
|--------|-------------|
| `client.LeadGenAPI.ListFormLeads(ctx)` | List leads for a single form |
| `client.LeadGenAPI.ListLeadForms(ctx)` | List lead forms |
| `client.LeadGenAPI.ListLeads(ctx)` | List submitted leads |
| `client.LeadGenAPI.CreateLeadForm(ctx)` | Create a lead form |
| `client.LeadGenAPI.CreateTestLead(ctx)` | Create a test lead |
| `client.LeadGenAPI.GetLeadForm(ctx)` | Get a lead form |
| `client.LeadGenAPI.ArchiveLeadForm(ctx)` | Archive a lead form |

### Mentions
| Method | Description |
|--------|-------------|
| `client.MentionsAPI.ListInboxMentions(ctx)` | List mentions |
| `client.MentionsAPI.ReplyToMention(ctx)` | Reply to a mention |

### Messages (Inbox)
| Method | Description |
|--------|-------------|
| `client.MessagesAPI.ListInboxConversations(ctx)` | List conversations |
| `client.MessagesAPI.CreateInboxConversation(ctx)` | Create conversation |
| `client.MessagesAPI.GetInboxConversation(ctx)` | Get conversation |
| `client.MessagesAPI.GetInboxConversationMessages(ctx)` | List messages |
| `client.MessagesAPI.UpdateInboxConversation(ctx)` | Update conversation status |
| `client.MessagesAPI.DeleteInboxMessage(ctx)` | Delete message |
| `client.MessagesAPI.AddMessageReaction(ctx)` | Add reaction |
| `client.MessagesAPI.EditInboxMessage(ctx)` | Edit message |
| `client.MessagesAPI.MarkConversationRead(ctx)` | Mark a conversation as read |
| `client.MessagesAPI.RemoveMessageReaction(ctx)` | Remove reaction |
| `client.MessagesAPI.SearchInboxConversations(ctx)` | Search conversations |
| `client.MessagesAPI.SendInboxMessage(ctx)` | Send message |
| `client.MessagesAPI.SendTypingIndicator(ctx)` | Send typing indicator |
| `client.MessagesAPI.UploadMediaDirect(ctx)` | Upload media file |

### Messaging Ads
| Method | Description |
|--------|-------------|
| `client.MessagingAdsAPI.CreateCallAd(ctx)` | Create Click-to-Call ad |
| `client.MessagingAdsAPI.CreateCtwaAd(ctx)` | Create Click-to-WhatsApp ad (deprecated) |
| `client.MessagingAdsAPI.CreateMessagingAd(ctx)` | Create click-to-message ad (WhatsApp / Messenger / Instagram Direct) |

### Phone Numbers
| Method | Description |
|--------|-------------|
| `client.PhoneNumbersAPI.ListPhoneNumberCountries(ctx)` | List offerable number countries |
| `client.PhoneNumbersAPI.ListPhoneNumberPortIns(ctx)` | List port-in orders |
| `client.PhoneNumbersAPI.ListPhoneNumbers(ctx)` | List phone numbers |
| `client.PhoneNumbersAPI.CreatePhoneNumberKycLink(ctx)` | Create a hosted KYC link |
| `client.PhoneNumbersAPI.CreatePhoneNumberPortIn(ctx)` | Port numbers in |
| `client.PhoneNumbersAPI.GetPhoneNumber(ctx)` | Get phone number |
| `client.PhoneNumbersAPI.GetPhoneNumberKycForm(ctx)` | Get KYC form spec |
| `client.PhoneNumbersAPI.GetPhoneNumberPortInOrderRequirements(ctx)` | A port-in order's pending requirements |
| `client.PhoneNumbersAPI.GetPhoneNumberPortInRequirements(ctx)` | Country porting requirements |
| `client.PhoneNumbersAPI.GetPhoneNumberRemediation(ctx)` | Get declined requirements |
| `client.PhoneNumbersAPI.CancelPhoneNumberPortIn(ctx)` | Cancel a port-in |
| `client.PhoneNumbersAPI.CheckPhoneNumberAvailability(ctx)` | Check country availability |
| `client.PhoneNumbersAPI.CheckPhoneNumberPortability(ctx)` | Check portability |
| `client.PhoneNumbersAPI.PurchasePhoneNumber(ctx)` | Purchase phone number |
| `client.PhoneNumbersAPI.ReleasePhoneNumber(ctx)` | Release phone number |
| `client.PhoneNumbersAPI.RemediatePhoneNumber(ctx)` | Resubmit a declined number |
| `client.PhoneNumbersAPI.ReplyToPhoneNumberReviewer(ctx)` | Reply to the regulatory reviewer |
| `client.PhoneNumbersAPI.RespondToPhoneNumberReviewer(ctx)` | Respond to the regulatory reviewer (message + corrections) |
| `client.PhoneNumbersAPI.ReviewPhoneNumberKycPacket(ctx)` | Pre-review a KYC packet |
| `client.PhoneNumbersAPI.SearchAvailablePhoneNumbers(ctx)` | Search available numbers |
| `client.PhoneNumbersAPI.SubmitPhoneNumberKyc(ctx)` | Submit KYC |
| `client.PhoneNumbersAPI.UploadPhoneNumberKycDocument(ctx)` | Upload a KYC document |
| `client.PhoneNumbersAPI.UploadPhoneNumberPortInDocument(ctx)` | Upload a porting document |
| `client.PhoneNumbersAPI.ValidatePhoneNumberKycAddress(ctx)` | Pre-validate KYC address |
| `client.PhoneNumbersAPI.ViewPhoneNumberKycDocument(ctx)` | View a KYC document on file |

### Reach and Frequency
| Method | Description |
|--------|-------------|
| `client.ReachAndFrequencyAPI.CreateRfPrediction(ctx)` | Create a Reach & Frequency prediction |
| `client.ReachAndFrequencyAPI.GetRfPrediction(ctx)` | Read a Reach & Frequency prediction |
| `client.ReachAndFrequencyAPI.CancelRfReservation(ctx)` | Cancel a Reach & Frequency reservation |
| `client.ReachAndFrequencyAPI.ReserveRfPrediction(ctx)` | Reserve a Reach & Frequency prediction |

### Reviews (Inbox)
| Method | Description |
|--------|-------------|
| `client.ReviewsAPI.ListInboxReviews(ctx)` | List reviews |
| `client.ReviewsAPI.DeleteInboxReviewReply(ctx)` | Delete review reply |
| `client.ReviewsAPI.ReplyToInboxReview(ctx)` | Reply to review |

### SMS
| Method | Description |
|--------|-------------|
| `client.SMSAPI.ListSmsOptOuts(ctx)` | List SMS opt-outs |
| `client.SMSAPI.ListSmsRegistrations(ctx)` | List carrier registrations |
| `client.SMSAPI.ListSmsSenderIds(ctx)` | List alphanumeric sender IDs |
| `client.SMSAPI.CreateSmsSenderId(ctx)` | Create an alphanumeric sender ID |
| `client.SMSAPI.GetSmsRegistration(ctx)` | Get a carrier registration |
| `client.SMSAPI.DeleteSmsSenderId(ctx)` | Delete an alphanumeric sender ID |
| `client.SMSAPI.AppealSmsRegistration(ctx)` | Appeal a rejected campaign |
| `client.SMSAPI.DeactivateSmsRegistration(ctx)` | Deactivate a brand/campaign registration |
| `client.SMSAPI.DisableSmsOnNumber(ctx)` | Disable SMS on a number |
| `client.SMSAPI.EnableSmsOnNumber(ctx)` | Enable SMS on a number |
| `client.SMSAPI.LookupSmsNumber(ctx)` | Look up carrier + line type |
| `client.SMSAPI.PreflightSmsRegistration(ctx)` | Pre-check a carrier registration |
| `client.SMSAPI.RequestSmsSenderIdLimitIncrease(ctx)` | Request a higher sender ID daily limit |
| `client.SMSAPI.ResendSmsRegistrationOtp(ctx)` | Re-send the sole-prop OTP |
| `client.SMSAPI.RespondToSmsRegistrationReview(ctx)` | Reply to a change request |
| `client.SMSAPI.ReuseSmsRegistrationForNumber(ctx)` | Add number to SMS registration |
| `client.SMSAPI.SendSms(ctx)` | Send an SMS/MMS |
| `client.SMSAPI.ShareSmsRegistration(ctx)` | Create a registration share link |
| `client.SMSAPI.StartSmsRegistration(ctx)` | Start a carrier registration |
| `client.SMSAPI.UploadSmsOptInProof(ctx)` | Upload opt-in form proof for an appeal |
| `client.SMSAPI.UploadSmsOptInProofFile(ctx)` | Upload opt-in form proof |
| `client.SMSAPI.VerifySmsRegistrationOtp(ctx)` | Submit the sole-prop OTP |

### Sequences
| Method | Description |
|--------|-------------|
| `client.SequencesAPI.ListSequenceEnrollments(ctx)` | List enrollments for a sequence |
| `client.SequencesAPI.ListSequences(ctx)` | List sequences |
| `client.SequencesAPI.CreateSequence(ctx)` | Create sequence |
| `client.SequencesAPI.GetSequence(ctx)` | Get sequence with steps |
| `client.SequencesAPI.UpdateSequence(ctx)` | Update sequence |
| `client.SequencesAPI.DeleteSequence(ctx)` | Delete sequence |
| `client.SequencesAPI.ActivateSequence(ctx)` | Activate sequence |
| `client.SequencesAPI.EnrollContacts(ctx)` | Enroll contacts in a sequence |
| `client.SequencesAPI.PauseSequence(ctx)` | Pause sequence |
| `client.SequencesAPI.UnenrollContact(ctx)` | Unenroll contact |

### Slack
| Method | Description |
|--------|-------------|
| `client.SlackAPI.ListSlackMembers(ctx)` | List Slack workspace members |

### Tracking Tags
| Method | Description |
|--------|-------------|
| `client.TrackingTagsAPI.ListTrackingTagSharedAccounts(ctx)` | List accounts it is shared with |
| `client.TrackingTagsAPI.ListTrackingTags(ctx)` | List tracking tags |
| `client.TrackingTagsAPI.CreateTrackingTag(ctx)` | Create a tracking tag |
| `client.TrackingTagsAPI.GetAdTrackingTags(ctx)` | Get ad tracking tags |
| `client.TrackingTagsAPI.GetTrackingTag(ctx)` | Get a tracking tag |
| `client.TrackingTagsAPI.GetTrackingTagStats(ctx)` | Get aggregated event stats |
| `client.TrackingTagsAPI.UpdateAdTrackingTags(ctx)` | Set ad tracking tags |
| `client.TrackingTagsAPI.UpdateTrackingTag(ctx)` | Update a tracking tag |
| `client.TrackingTagsAPI.AddTrackingTagSharedAccount(ctx)` | Share with an ad account |
| `client.TrackingTagsAPI.RemoveTrackingTagSharedAccount(ctx)` | Stop sharing with an account |

### Twitter Engagement
| Method | Description |
|--------|-------------|
| `client.TwitterEngagementAPI.GetTweet(ctx)` | Look up a tweet |
| `client.TwitterEngagementAPI.BookmarkPost(ctx)` | Bookmark a tweet |
| `client.TwitterEngagementAPI.FollowUser(ctx)` | Follow a user |
| `client.TwitterEngagementAPI.RemoveBookmark(ctx)` | Remove bookmark |
| `client.TwitterEngagementAPI.RetweetPost(ctx)` | Retweet a post |
| `client.TwitterEngagementAPI.SearchTweets(ctx)` | Search recent tweets |
| `client.TwitterEngagementAPI.UndoRetweet(ctx)` | Undo retweet |
| `client.TwitterEngagementAPI.UnfollowUser(ctx)` | Unfollow a user |

### Validate
| Method | Description |
|--------|-------------|
| `client.ValidateAPI.ValidateMedia(ctx)` | Validate media URL |
| `client.ValidateAPI.ValidatePost(ctx)` | Validate post content |
| `client.ValidateAPI.ValidatePostLength(ctx)` | Validate character count |
| `client.ValidateAPI.ValidateSubreddit(ctx)` | Check subreddit existence |

### Verify
| Method | Description |
|--------|-------------|
| `client.VerifyAPI.CreateVerification(ctx)` | Send a verification code |
| `client.VerifyAPI.GetVerification(ctx)` | Get a verification |
| `client.VerifyAPI.CheckVerification(ctx)` | Check a verification code |

### Voice
| Method | Description |
|--------|-------------|
| `client.VoiceAPI.ListVoiceCalls(ctx)` | List phone calls |
| `client.VoiceAPI.CreateVoiceCall(ctx)` | Place an outbound phone call |
| `client.VoiceAPI.CreateVoiceWebSession(ctx)` | Mint a browser softphone session |
| `client.VoiceAPI.GetVoiceCall(ctx)` | Get a phone call |
| `client.VoiceAPI.GetVoiceCallEstimate(ctx)` | Estimate call cost |
| `client.VoiceAPI.GetVoiceCallRecording(ctx)` | Get a call recording |
| `client.VoiceAPI.DialVoiceWebCall(ctx)` | Dial from the browser softphone |
| `client.VoiceAPI.DisableVoiceOnNumber(ctx)` | Disable phone calling on a number |
| `client.VoiceAPI.EnableVoiceOnNumber(ctx)` | Enable phone calling on a number |
| `client.VoiceAPI.EndVoiceCall(ctx)` | Hang up a live call |
| `client.VoiceAPI.TransferVoiceCall(ctx)` | Blind-transfer a live call |

### WhatsApp
| Method | Description |
|--------|-------------|
| `client.WhatsAppAPI.ListWhatsAppConversions(ctx)` | List conversion events |
| `client.WhatsAppAPI.ListWhatsAppGroupChats(ctx)` | List active groups |
| `client.WhatsAppAPI.ListWhatsAppGroupJoinRequests(ctx)` | List join requests |
| `client.WhatsAppAPI.CreateWhatsAppDataset(ctx)` | Provision CTWA dataset |
| `client.WhatsAppAPI.CreateWhatsAppGroupChat(ctx)` | Create group |
| `client.WhatsAppAPI.CreateWhatsAppGroupInviteLink(ctx)` | Create invite link |
| `client.WhatsAppAPI.CreateWhatsAppTemplate(ctx)` | Create template |
| `client.WhatsAppAPI.GetWhatsAppBlockStatus(ctx)` | Check if a user is blocked |
| `client.WhatsAppAPI.GetWhatsAppBlockedUsers(ctx)` | List blocked users |
| `client.WhatsAppAPI.GetWhatsAppBusinessProfile(ctx)` | Get business profile |
| `client.WhatsAppAPI.GetWhatsAppDataset(ctx)` | Get CTWA conversions dataset |
| `client.WhatsAppAPI.GetWhatsAppDisplayName(ctx)` | Get display name status |
| `client.WhatsAppAPI.GetWhatsAppGroupChat(ctx)` | Get group info |
| `client.WhatsAppAPI.GetWhatsAppMedia(ctx)` | Download WhatsApp media |
| `client.WhatsAppAPI.GetWhatsAppTemplate(ctx)` | Get template |
| `client.WhatsAppAPI.GetWhatsAppTemplates(ctx)` | List templates |
| `client.WhatsAppAPI.GetWhatsappBusinessUsername(ctx)` | Get business username |
| `client.WhatsAppAPI.GetWhatsappBusinessUsernameSuggestions(ctx)` | Get username suggestions |
| `client.WhatsAppAPI.UpdateWhatsAppBusinessProfile(ctx)` | Update business profile |
| `client.WhatsAppAPI.UpdateWhatsAppDisplayName(ctx)` | Request display name change |
| `client.WhatsAppAPI.UpdateWhatsAppGroupChat(ctx)` | Update group settings |
| `client.WhatsAppAPI.UpdateWhatsAppTemplate(ctx)` | Update template |
| `client.WhatsAppAPI.DeleteWhatsAppGroupChat(ctx)` | Delete group |
| `client.WhatsAppAPI.DeleteWhatsAppTemplate(ctx)` | Delete template |
| `client.WhatsAppAPI.DeleteWhatsappBusinessUsername(ctx)` | Delete business username |
| `client.WhatsAppAPI.AddWhatsAppGroupParticipants(ctx)` | Add participants |
| `client.WhatsAppAPI.ApproveWhatsAppGroupJoinRequests(ctx)` | Approve join requests |
| `client.WhatsAppAPI.BlockWhatsAppUsers(ctx)` | Block users |
| `client.WhatsAppAPI.RegisterWhatsAppNumber(ctx)` | Register a connected WhatsApp number on the Cloud API |
| `client.WhatsAppAPI.RejectWhatsAppGroupJoinRequests(ctx)` | Reject join requests |
| `client.WhatsAppAPI.RemoveWhatsAppGroupParticipants(ctx)` | Remove participants |
| `client.WhatsAppAPI.SendWhatsAppConversion(ctx)` | Send WhatsApp conversion event |
| `client.WhatsAppAPI.SetWhatsappBusinessUsername(ctx)` | Set business username |
| `client.WhatsAppAPI.UnblockWhatsAppUsers(ctx)` | Unblock users |
| `client.WhatsAppAPI.UploadWhatsAppProfilePhoto(ctx)` | Upload profile picture |

### WhatsApp Calling
| Method | Description |
|--------|-------------|
| `client.WhatsAppCallingAPI.ListWhatsAppCalls(ctx)` | List call history for an account |
| `client.WhatsAppCallingAPI.GetWhatsAppCall(ctx)` | Get a single call |
| `client.WhatsAppCallingAPI.GetWhatsAppCallEstimate(ctx)` | Estimate per-minute cost |
| `client.WhatsAppCallingAPI.GetWhatsAppCallPermissions(ctx)` | Check call permission |
| `client.WhatsAppCallingAPI.GetWhatsAppCallRecording(ctx)` | Get a call recording |
| `client.WhatsAppCallingAPI.GetWhatsAppCalling(ctx)` | Get calling config for a number |
| `client.WhatsAppCallingAPI.GetWhatsAppCallingConfig(ctx)` | Get calling config for an account |
| `client.WhatsAppCallingAPI.UpdateWhatsAppCalling(ctx)` | Update calling config |
| `client.WhatsAppCallingAPI.UpdateWhatsAppCallingLegacy(ctx)` | Update calling config |
| `client.WhatsAppCallingAPI.DisableWhatsAppCalling(ctx)` | Disable calling on a number |
| `client.WhatsAppCallingAPI.DisableWhatsAppCallingLegacy(ctx)` | Disable calling on a number |
| `client.WhatsAppCallingAPI.EnableWhatsAppCalling(ctx)` | Enable calling on a number |
| `client.WhatsAppCallingAPI.EnableWhatsAppCallingLegacy(ctx)` | Enable calling on a number |
| `client.WhatsAppCallingAPI.InitiateWhatsAppCall(ctx)` | Initiate outbound call |
| `client.WhatsAppCallingAPI.StartWhatsAppCallerIdVerification(ctx)` | Start caller-ID verification for a customer-brought number |
| `client.WhatsAppCallingAPI.VerifyWhatsAppCallerId(ctx)` | Confirm the caller-ID verification code |

### WhatsApp Flows
| Method | Description |
|--------|-------------|
| `client.WhatsAppFlowsAPI.ListWhatsAppFlowResponses(ctx)` | List flow responses |
| `client.WhatsAppFlowsAPI.ListWhatsAppFlowVersions(ctx)` | List flow versions |
| `client.WhatsAppFlowsAPI.ListWhatsAppFlows(ctx)` | List flows |
| `client.WhatsAppFlowsAPI.CreateWhatsAppFlow(ctx)` | Create flow |
| `client.WhatsAppFlowsAPI.GetWhatsAppFlow(ctx)` | Get flow |
| `client.WhatsAppFlowsAPI.GetWhatsAppFlowJson(ctx)` | Get flow JSON asset |
| `client.WhatsAppFlowsAPI.GetWhatsAppFlowPreview(ctx)` | Get flow preview URL |
| `client.WhatsAppFlowsAPI.UpdateWhatsAppFlow(ctx)` | Update flow |
| `client.WhatsAppFlowsAPI.DeleteWhatsAppFlow(ctx)` | Delete flow |
| `client.WhatsAppFlowsAPI.DeprecateWhatsAppFlow(ctx)` | Deprecate flow |
| `client.WhatsAppFlowsAPI.PublishWhatsAppFlow(ctx)` | Publish flow |
| `client.WhatsAppFlowsAPI.SendWhatsAppFlowMessage(ctx)` | Send flow message |
| `client.WhatsAppFlowsAPI.UploadWhatsAppFlowJson(ctx)` | Upload flow JSON |

### WhatsApp Phone Numbers
| Method | Description |
|--------|-------------|
| `client.WhatsAppPhoneNumbersAPI.ListWhatsAppNumberCountries(ctx)` | List offerable number countries |
| `client.WhatsAppPhoneNumbersAPI.CreateWhatsAppNumberKycLink(ctx)` | Create a hosted KYC link |
| `client.WhatsAppPhoneNumbersAPI.GetWhatsAppNumberInfo(ctx)` | Get number status |
| `client.WhatsAppPhoneNumbersAPI.GetWhatsAppNumberKycForm(ctx)` | Get KYC form spec |
| `client.WhatsAppPhoneNumbersAPI.GetWhatsAppNumberRemediation(ctx)` | Get declined requirements |
| `client.WhatsAppPhoneNumbersAPI.GetWhatsAppPhoneNumber(ctx)` | Get phone number |
| `client.WhatsAppPhoneNumbersAPI.GetWhatsAppPhoneNumbers(ctx)` | List phone numbers |
| `client.WhatsAppPhoneNumbersAPI.CheckWhatsAppNumberAvailability(ctx)` | Check country availability |
| `client.WhatsAppPhoneNumbersAPI.MoveWhatsAppNumberToProfile(ctx)` | Move a number to another profile |
| `client.WhatsAppPhoneNumbersAPI.PurchaseWhatsAppPhoneNumber(ctx)` | Purchase phone number |
| `client.WhatsAppPhoneNumbersAPI.ReleaseWhatsAppPhoneNumber(ctx)` | Release phone number |
| `client.WhatsAppPhoneNumbersAPI.RemediateWhatsAppNumber(ctx)` | Resubmit a declined number |
| `client.WhatsAppPhoneNumbersAPI.SearchAvailableWhatsAppNumbers(ctx)` | Search available numbers |
| `client.WhatsAppPhoneNumbersAPI.SubmitWhatsAppNumberKyc(ctx)` | Submit KYC |
| `client.WhatsAppPhoneNumbersAPI.UploadWhatsAppNumberKycDocument(ctx)` | Upload a KYC document |
| `client.WhatsAppPhoneNumbersAPI.ValidateWhatsAppNumberKycAddress(ctx)` | Pre-validate KYC address |

### WhatsApp Sandbox
| Method | Description |
|--------|-------------|
| `client.WhatsAppSandboxAPI.ListWhatsAppSandboxSessions(ctx)` | List your sandbox sessions |
| `client.WhatsAppSandboxAPI.CreateWhatsAppSandboxSession(ctx)` | Start a sandbox activation |
| `client.WhatsAppSandboxAPI.DeleteWhatsAppSandboxSession(ctx)` | Revoke a sandbox session |

### WhatsApp Templates
| Method | Description |
|--------|-------------|
| `client.WhatsAppTemplatesAPI.GetWhatsAppLibraryTemplate(ctx)` | Look up a library template |

### Workflows
| Method | Description |
|--------|-------------|
| `client.WorkflowsAPI.ListWorkflowExecutionEvents(ctx)` | Get an execution's timeline |
| `client.WorkflowsAPI.ListWorkflowExecutions(ctx)` | List workflow runs |
| `client.WorkflowsAPI.ListWorkflowVersions(ctx)` | List a workflow's version history |
| `client.WorkflowsAPI.ListWorkflows(ctx)` | List workflows |
| `client.WorkflowsAPI.CreateWorkflow(ctx)` | Create workflow |
| `client.WorkflowsAPI.GetWorkflow(ctx)` | Get workflow with graph |
| `client.WorkflowsAPI.GetWorkflowVersion(ctx)` | Get a specific workflow version |
| `client.WorkflowsAPI.UpdateWorkflow(ctx)` | Update workflow |
| `client.WorkflowsAPI.DeleteWorkflow(ctx)` | Delete workflow |
| `client.WorkflowsAPI.ActivateWorkflow(ctx)` | Activate workflow |
| `client.WorkflowsAPI.DuplicateWorkflow(ctx)` | Duplicate a workflow |
| `client.WorkflowsAPI.PauseWorkflow(ctx)` | Pause workflow |
| `client.WorkflowsAPI.RestoreWorkflowVersion(ctx)` | Restore a workflow version |
| `client.WorkflowsAPI.TriggerWorkflow(ctx)` | Manually start a workflow run |

### Invites
| Method | Description |
|--------|-------------|
| `client.InvitesAPI.CreateInviteToken(ctx)` | Create invite token |

## Documentation

- [API Reference](https://docs.zernio.com/api-reference)
- [Getting Started Guide](https://docs.zernio.com/quickstart)

## License

MIT
