# Tips and Best Practices

## Workflow Optimization

### 1. Open New Terminal for Each Manual Step

**Why**: Keeps authentication isolated, prevents session timeout issues, provides clear separation of concerns

**How**:
- Use separate terminal windows for each network operation
- Close terminals after completion for security
- Always use fresh terminals for credential entry

### 2. Review Generated Message Before Pushing

**Why**: Ensures summary accurately reflects changes, verifies conventional commits format

**How**:
- Read the generated summary carefully
- Check that all changes are properly categorized
- Verify language preference applied correctly (if any)

### 3. Use Descriptive Local Commits

**Why**: Good local commit messages → better generated summary

**How**:
- Include feature/bug/refactor context in commit messages
- Write in language you prefer for final message
- Be specific: "fix: validation error" vs "fix: bug"

### 4. Test SSH Connection First (Optional)

```bash
ssh -T git@code.alipay.com
```

**When**: Before starting skill if you're unsure about SSH setup

### 5. Backup Before Force Push (Optional)

```bash
git branch backup-$(date +%Y%m%d)
```

**When**: Before making significant changes that will be force pushed

## Advanced Usage Patterns

### Pattern 1: Feature Development Workflow

```
1. Create feature branch
2. Make multiple small commits
3. Use git-push skill to consolidate and push
4. Create PR with clean history
```

### Pattern 2: Pre-Rebase Safety Net

```bash
# Create backup before running skill
git branch pre-rebase-backup
git push origin pre-rebase-backup

# Now safe to run git-push skill
```

### Pattern 3: Testing Generated Messages

```bash
# Run skill through rebase but stop before push
# Review commit message
git log -1

# If message needs adjustment
git commit --amend

# Then push manually
git push --force-with-lease origin <branch>
```

## Related Commands

Use these commands to understand and debug your git setup:

- Check remote: `git remote -v`
- Test SSH: `ssh -T git@code.alipay.com`
- Check branch: `git branch -vv`
- View log: `git log --oneline -10`
- Manual rebase: `git rebase -i <remote-branch>`
- Manual push: `git push --force-with-lease origin <branch>`
- Abort rebase: `git rebase --abort`
