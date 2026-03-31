# LeetCode Practice

Automated sync of my daily LeetCode submissions and MonkeyType typing practice to GitHub using GitHub Actions.

---

## LeetCode Sync

A daily workflow runs at 8:00 AM UTC and syncs any new accepted submissions from LeetCode to this repo under `problems/`.

### Secrets required

| Secret | Description |
|---|---|
| `MY_GITHUB_TOKEN` | Personal Access Token with `Contents: Read & Write` |
| `LEETCODE_SESSION` | `LEETCODE_SESSION` cookie from leetcode.com |
| `LEETCODE_CSRF_TOKEN` | `csrftoken` cookie from leetcode.com |

To get LeetCode cookies: log into leetcode.com → DevTools → Application → Cookies.

### Manual trigger

Go to **Actions** → **LeetCode Sync** → **Run workflow**.

---

## MonkeyType Sync

A daily workflow runs at 11:30 PM UTC and fetches my latest 50-word typing test results from MonkeyType, saving a markdown file to `monkeytype/YYYY/MM/YYYY-MM-DD.md` with stats like WPM, accuracy, consistency, and character breakdown.

### Secrets required

| Secret | Description |
|---|---|
| `MONKEYTYPE_API_KEY` | ApeKey from monkeytype.com → Settings → Ape Keys |

### Manual trigger

Go to **Actions** → **MonkeyType Sync** → **Run workflow**.
