# LeetCode Practice

Automated sync of my LeetCode submissions to GitHub using GitHub Actions.

## How it works

A daily workflow runs at 8:00 AM UTC and syncs any new accepted submissions from LeetCode to this repo. Each solution is committed under my GitHub account, contributing to the activity graph.

## Setup

The workflow requires three GitHub secrets:

| Secret | Description |
|---|---|
| `MY_GITHUB_TOKEN` | Personal Access Token with `Contents: Read & Write` |
| `LEETCODE_SESSION` | `LEETCODE_SESSION` cookie from leetcode.com |
| `LEETCODE_CSRF_TOKEN` | `csrftoken` cookie from leetcode.com |

To get LeetCode cookies: log into leetcode.com → DevTools → Application → Cookies.

## Manual trigger

Go to **Actions** → **LeetCode Sync** → **Run workflow**.
