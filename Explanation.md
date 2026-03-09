# Bug explanation

## What was the bug?

For API requests (`api=True`), when `oauth2_token` was a **dict** (e.g. legacy or deserialized token), the client did not refresh the token and did not set the `Authorization` header. So the request went out without auth even though the code is designed to support both `OAuth2Token` instances and dicts.

## Why did it happen?

The refresh condition was:

```python
if not self.oauth2_token or (
    isinstance(self.oauth2_token, OAuth2Token) and self.oauth2_token.expired
):
    self.refresh_oauth2()
```

For a dict, `not self.oauth2_token` is false (dict is truthy), and `isinstance(..., OAuth2Token)` is false, so the whole condition was false and refresh was never called. Only `None` or an expired `OAuth2Token` triggered a refresh; a non-`OAuth2Token` value (like a dict) was treated as “valid” and then skipped when building the header (because only `OAuth2Token` got `as_header()`), so the request had no auth.

## Why does your fix actually solve it?

The fix is to refresh whenever the token is missing, not a valid `OAuth2Token`, or expired:

```python
if not self.oauth2_token or not isinstance(self.oauth2_token, OAuth2Token) or self.oauth2_token.expired:
    self.refresh_oauth2()
```

So we refresh when: token is `None`, token is a dict (or any non-`OAuth2Token`), or token is an expired `OAuth2Token`. After refresh, `oauth2_token` is always an `OAuth2Token`, so the header is set correctly.

## What’s one realistic case / edge case your tests still don’t cover?

**Expired token stored as dict.** The tests use a dict with `expires_at: 0` and assert that we refresh. They do not assert that a dict with a *future* `expires_at` (e.g. `int(time.time()) + 3600`) is still treated as invalid and triggers a refresh. In practice, if some code path stores tokens as dicts and another path expects only `OAuth2Token`, we rely on “dict ⇒ refresh” rather than “dict with past expiry ⇒ refresh”; a test that passes a dict with a future expiry and expects a refresh would lock in that “dict is never valid” contract.
