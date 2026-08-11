---
name: buffer-api
description: >-
  Manage multiple Buffer accounts via the GraphQL API. Use when the MCP
  connector only covers one Buffer login and you need to reach additional
  accounts whose API keys live in .env. Covers account info, channels, posts
  (create/edit/delete/list), ideas, templates, and analytics.
---

# Buffer GraphQL API skill

## When to use

Use this skill whenever you need to interact with a Buffer account that is
**not** connected via the MCP connector — i.e. any account authenticated by an
API key in `.env` rather than the claude.ai OAuth flow.

The MCP connector (`mcp__claude_ai_Buffer__*` tools) handles the first account.
This skill handles every additional one.

## Authentication

Each Buffer account has a key in `.env` at the repo root, named by role:

```
LINKEDIN_BUFFER_API_KEY=...
# future accounts:
# MASTODON_BUFFER_API_KEY=...
# FACEBOOK_BUFFER_API_KEY=...
```

Read `.env` to get the key. **Never log, echo, or commit a key.**

## Endpoint

All requests go to:

```
POST https://api.buffer.com
Content-Type: application/json
Authorization: Bearer <API_KEY>
```

The body is a JSON object with `query` (or `mutation`) and optional `variables`.

## How to call

Use the `WebFetch` tool or `curl` via `Bash`. Example with curl:

```bash
curl -s https://api.buffer.com \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $LINKEDIN_BUFFER_API_KEY" \
  -d '{"query":"{ account { id email organizations { id name } } }"}'
```

Load the key from `.env` first — never hardcode it:

```bash
source /path/to/repo/.env
```

Do NOT use an absolute home-directory path. The repo root is the directory
containing this file's ancestor `.claude/` folder. Scripts locate it with
`$(cd "$(dirname "$0")/../.." && pwd)` or similar.

## Core operations

### 1. Get account & org ID (always first)

```graphql
{
  account {
    id
    email
    name
    timezone
    organizations {
      id
      name
      ownerEmail
      limits { channels scheduledPosts tags ideas members }
      members { totalCount }
    }
  }
}
```

### 2. List channels

```graphql
query Channels($orgId: OrganizationId!) {
  channels(input: { organizationId: $orgId }) {
    id name displayName service type
    avatar isDisconnected isLocked
    timezone
    postingSchedule { day paused times }
  }
}
```

Variables: `{"orgId": "<org-id>"}`

### 3. Get single channel

```graphql
query Channel($id: ChannelId!) {
  channel(input: { id: $id }) {
    id name displayName service type timezone
    postingSchedule { day paused times }
    linkShortening { isEnabled config { domain name } }
    isQueuePaused
  }
}
```

### 4. List posts

```graphql
query Posts($orgId: OrganizationId!, $status: [PostStatus!], $channelIds: [ChannelId!]) {
  posts(
    input: {
      organizationId: $orgId
      filter: { status: $status, channelIds: $channelIds }
      sort: [{ field: dueAt, direction: asc }]
    }
    first: 25
  ) {
    edges {
      node {
        id text status dueAt sentAt
        channelId channelService
        tags { id name }
        metrics { type value }
        externalLink
      }
    }
    pageInfo { hasNextPage endCursor }
  }
}
```

Status values: `draft`, `scheduled`, `sent`, `error`, `needs_approval`, `sending`.

### 5. Create a post

```graphql
mutation CreatePost($input: CreatePostInput!) {
  createPost(input: $input) {
    ... on PostActionSuccess { post { id status dueAt text } }
    ... on InvalidInputError { message }
    ... on LimitReachedError { message }
    ... on RestProxyError { message code }
    ... on NotFoundError { message }
    ... on UnauthorizedError { message }
    ... on UnexpectedError { message }
  }
}
```

Variables (schedule for a specific time):
```json
{
  "input": {
    "channelId": "<channel-id>",
    "text": "Post text here",
    "mode": "customScheduled",
    "schedulingType": "automatic",
    "dueAt": "2026-08-12T10:00:00.000Z"
  }
}
```

**mode values:**
- `customScheduled` — post at the `dueAt` time
- `addToQueue` — add to the channel's posting schedule queue
- `shareNext` — push to top of queue
- `shareNow` — publish immediately

**schedulingType values:**
- `automatic` — Buffer publishes directly
- `notification` — sends a reminder instead (for Instagram/TikTok/YouTube)

For LinkedIn posts, add metadata:
```json
{
  "input": {
    "channelId": "<channel-id>",
    "text": "Post text",
    "mode": "customScheduled",
    "schedulingType": "automatic",
    "dueAt": "2026-08-12T10:00:00.000Z",
    "metadata": {
      "linkedin": {
        "linkAttachment": { "url": "https://example.com" }
      }
    }
  }
}
```

### 6. Edit a post

```graphql
mutation EditPost($input: EditPostInput!) {
  editPost(input: $input) {
    ... on PostActionSuccess { post { id status dueAt text } }
    ... on InvalidInputError { message }
    ... on NotFoundError { message }
    ... on UnauthorizedError { message }
    ... on UnexpectedError { message }
  }
}
```

Variables — only include fields you want to change:
```json
{
  "input": {
    "id": "<post-id>",
    "text": "Updated text",
    "dueAt": "2026-08-13T14:00:00.000Z"
  }
}
```

### 7. Delete a post

```graphql
mutation DeletePost($id: PostId!) {
  deletePost(input: { id: $id }) {
    ... on DeletePostSuccess { id }
    ... on VoidMutationError { message }
  }
}
```

### 8. Get post metrics (aggregated)

```graphql
query AggMetrics($orgId: OrganizationId!, $start: DateTime!, $end: DateTime!, $channelIds: [ChannelId!]) {
  aggregatedPostMetrics(input: {
    organizationId: $orgId
    startDateTime: $start
    endDateTime: $end
    channelIds: $channelIds
  }) {
    metrics { type name value unit description }
    metricsUpdatedAt
  }
}
```

### 9. Ideas

**List idea groups:**
```graphql
query IdeaGroups($orgId: ID!) {
  ideaGroups(input: { organizationId: $orgId }) {
    id name isLocked
  }
}
```

**List ideas:**
```graphql
query Ideas($orgId: OrganizationId!) {
  ideas(input: { organizationId: $orgId }, first: 25) {
    edges {
      node {
        id groupId
        content { text title tags { id name } services media { url type } }
      }
    }
    pageInfo { hasNextPage endCursor }
  }
}
```

**Create idea:**
```graphql
mutation CreateIdea($input: CreateIdeaInput!) {
  createIdea(input: $input) {
    ... on Idea { id content { text title } }
    ... on IdeaResponse { idea { id } refreshIdeas }
    ... on InvalidInputError { message }
    ... on LimitReachedError { message }
  }
}
```

### 10. Post templates

**List:**
```graphql
query Templates($orgId: OrganizationId!) {
  postTemplates(input: { organizationId: $orgId }, first: 25) {
    edges { node { id title body description emoji visibility } }
  }
}
```

**Create:**
```graphql
mutation CreateTemplate($input: CreatePostTemplateInput!) {
  createPostTemplate(input: $input) {
    ... on CreatePostTemplateSuccess { postTemplate { id title } }
    ... on VoidMutationError { message }
  }
}
```

## Service enum values

When filtering or reading channel service types:
`bluesky`, `facebook`, `googlebusiness`, `instagram`, `linkedin`,
`mastodon`, `pinterest`, `threads`, `tiktok`, `twitter`, `youtube`.

## Image / video assets

To attach media, use the `assets` field on `CreatePostInput`:

```json
{
  "assets": [
    { "image": { "url": "https://publicly-accessible-url.com/image.png" } }
  ]
}
```

The URL must be publicly accessible. For video: use `"video": {"url": "..."}`.

## Pagination

Paginated queries accept `first` (page size) and `after` (cursor). Check
`pageInfo.hasNextPage` and pass `pageInfo.endCursor` as `after` for the next
page.

## Error handling

All mutations return a union. Always destructure both the success type and
every error type (`InvalidInputError`, `NotFoundError`, `UnauthorizedError`,
`UnexpectedError`, `RestProxyError`, `LimitReachedError`). A 401 HTTP response
means the API key is invalid or expired.

## Multi-account workflow

1. Read `.env` to discover which `*_BUFFER_API_KEY` vars exist.
2. For each account, run the `account` query to get org IDs and channel lists.
3. Match channels to the task at hand (e.g. LinkedIn channels for LinkedIn
   drafts, X channels for tweet drafts).
4. Use the correct key for each operation.

When the user says "Buffer" without specifying which account, list all
available accounts and their channels so they can choose.
