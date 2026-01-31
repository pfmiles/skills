---
name: git-push
description: For semi-automated workflow that combines commits via rebase, generates conventional commits summary, and provides manual commands for network operations requiring authentication.
---

# Git-Push with Rebase and Squash

Semi-automated workflow for pushing commits with interactive rebase and conventional commits summary. Automates non-sensitive operations while keeping network authentication manual for maximum security.

## When to Use

- Combine multiple local commits before pushing
- Rebase onto latest remote changes
- Clean up commit history with well-structured summary
- Maintain complete control over authentication
- Comply with security policies (no credential storage)

## How It Works

| Step | Operation | Type | Description |
|------|-----------|------|-------------|
| 1 | Pre-flight checks | Auto | Verify remote tracking and clean working directory |
| 2 | Fetch changes | Manual | Run `git fetch origin` in new terminal (password required) |
| 3 | Interactive rebase | Auto | `git rebase -i origin/<branch>` with auto-squash |
| 4 | Generate summary | Auto | Create conventional commits format from squashed commits |
| 5 | Display push command | Auto | Provide final command for manual execution |
| 6 | Push changes | Manual | Execute push in new terminal (password required) |
| 7 | Confirm success | Manual | Report completion status |

**Only Steps 2 and 6 require password authentication (network operations).**

## Quick Start

### Basic Usage

```
Push my local commits to remote
```

### With Language Preference

```
用中文推送本地提交
```

### After Completion

Confirm: "Push completed successfully"

## Parameters

- **Additional requirements** (optional): Special instructions for commit message generation
  - Language: "用中文", "en français", "en español"
  - Focus: "focus on API changes", "emphasize security updates"

## Details and Examples

- [Complete Example Sessions](references/examples.md)
- [Security Information](references/security.md)
- [Troubleshooting Guide](references/troubleshooting.md)
- [Tips and Best Practices](references/tips.md)

## Related Commands

```bash
git remote -v                    # Check remotes
ssh -T git@code.alipay.com     # Test SSH
/git-commit                    # Commit changes first
git log --oneline -10          # View recent commits
git rebase --abort             # Abort if needed
```

---

**Tips for Best Results:**

1. Use `/git-commit` first if you have uncommitted changes
2. Open new terminal for each network operation
3. Review generated commit message before pushing
4. Use descriptive local commits for better summaries
5. Test SSH connection first if unsure: `ssh -T git@code.alipay.com`
