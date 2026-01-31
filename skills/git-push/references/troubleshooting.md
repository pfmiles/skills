# Troubleshooting Guide

## Common Issues and Solutions

### If git fetch fails

**Error**: "Unable to determine upstream commits" or "rebase errors"

**Solution**: The skill will detect this and prompt you to run `git fetch origin` manually in a new terminal

### If you enter wrong passphrase

**Error**: "Permission denied (publickey)"

**Solution**: Terminal will prompt again. Ensure correct passphrase

### If rebase has conflicts

**Solution**: Resolve conflicts, then `git rebase --continue`, then retry skill

### If remote branch doesn't exist

**Solution**: Set up tracking with `git push -u origin HEAD`, then retry

## Pre-flight Check Failures

### Working directory not clean

**Error**: "Cannot proceed with uncommitted changes"

**Solution**: Commit or stash changes before running skill

### No remote tracking

**Error**: "Branch has no upstream configured"

**Solution**: Set upstream with `git push -u origin <branch-name>`

## Push Errors

### Force push rejected

**Error**: "Updates were rejected"

**Solution**: Remote has new commits. Re-run the skill to fetch and rebase again.

### Permission denied

**Error**: "Permission denied (publickey)"

**Solution**: Check SSH key setup: `ssh -T git@code.alipay.com`

## Error Handling Tips

1. **Always open new terminals for manual steps** to avoid session timeout issues
2. **Verify SSH connection** before starting if unsure: `ssh -T git@code.alipay.com`
3. **Keep authentication isolated** by using separate terminals for each network operation
4. **Review generated commit messages** before pushing to ensure accuracy
5. **Create backup branches** before force push if desired: `git branch backup-$(date +%Y%m%d)`

## Recovery Options

### If push fails after rebase

You can safely retry the skill. The rebase has already been completed, so you can skip directly to the push step if the rebase was successful.

### If you want to abort

At any point before the final push, you can abort with:
```bash
git rebase --abort
```

### If you pushed incorrectly

If you need to revert, you can use:
```bash
git reset --hard origin/<branch-name>
```
