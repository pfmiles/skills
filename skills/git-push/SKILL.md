---
name: git-push
description: Automatically checks prerequisites, then runs interactive rebase to combine commits, generates conventional commits summary, provides final push command for manual execution in new terminal. Only git fetch and git push steps require manual intervention for password entry.
---

# Git Push with Rebase and Squash (Semi-Automated)

Automatically checks prerequisites and runs interactive rebase, then provides manual commands for git fetch and git push steps that require password authentication. Only network operations that need password entry are handled manually for maximum security.

## When to Use This Skill

- When you have multiple local commits that should be combined into one before pushing
- When you need to rebase onto the latest remote changes before pushing
- When you want to clean up your commit history with a well-structured summary
- When you prefer complete control over authentication and network operations
- When security policies prohibit storing credentials in environment variables

## What This Skill Does

1. **Automatic Pre-flight Checks**: Automatically verifies prerequisites (no password required)
2. **Fetches Latest Changes**: Asks you to run `git fetch` manually in new terminal (requires password)
3. **Runs Interactive Rebase**: Executes rebase with automatic squash configuration
4. **Generates Summary Comment**: Creates conventional commits format summary
5. **Provides Push Command**: Displays final command for manual execution in new terminal (requires password)
6. **Waits for Confirmation**: Asks you to complete push and report status

## Security Benefits

This skill ensures maximum security by:
- Never storing credentials in environment variables
- Never writing passwords to configuration files
- Requiring manual execution only for network operations that need password authentication (fetch and push)
- Keeping authentication entirely in your control
- Automating non-sensitive operations for better user experience

## How to Use

### Complete Workflow

```
Push my local commits to remote
```

**The skill will guide you through these steps:**

### Step 1: Pre-flight Checks (Automated)

The skill automatically checks:
- Remote branch tracking configuration
- Working directory cleanliness (must be no uncommitted changes)

✓ This step requires no manual input and doesn't need password authentication.

### Step 2: Fetch Latest Changes (Manual)

In a **new terminal**, fetch remote changes:
```bash
cd /Users/yue.weny/workspace/xhunterlib_merged
git fetch origin

# Enter SSH passphrase if prompted:
Enter passphrase for key '/Users/username/.ssh/id_rsa': [enter your passphrase]
```

Wait for fetch to complete, then return here and confirm.

### Step 3: Interactive Rebase (Automated)

The skill runs:
```bash
git rebase -i origin/<branch-name>
```

It automatically configures the rebase todo list to:
- `pick` the first commit
- `squash` all subsequent commits

### Step 4: Generate Summary (Automated)

The skill analyzes all squashed commits and generates a conventional commits format message.

### Step 5: Display Push Command

The skill shows you the final command:
```
=== MANUAL STEP REQUIRED ===

Please open a new terminal and run:

    cd /Users/yue.weny/workspace/xhunterlib_merged
    git push --force-with-lease origin EI63633597_20240701_pfmiles

When prompted, enter your SSH key passphrase.

After completing the push, please confirm here.
```

### Step 6: Manual Push (You Execute)

In a **new terminal**:
```bash
cd /Users/yue.weny/workspace/xhunterlib_merged
git push --force-with-lease origin EI63633597_20240701_pfmiles

# Enter passphrase when prompted:
Enter passphrase for key '/Users/username/.ssh/id_rsa': [enter passphrase]
```

### Step 7: Confirm Success

Return to Claude Code and confirm: "Push completed successfully"

## With Language Preference

```
用中文推送本地提交
```

The skill will generate the commit message in Chinese but the workflow remains the same - you'll still manually perform the fetch and push steps.

## Parameters

- **Additional requirements** (optional string): Special instructions for commit message generation
  - Language preferences (e.g., "用中文", "in French", "en español")
  - Focus areas (e.g., "focus on API changes", "emphasize security updates")

## Complete Example Session

**User**: "Push my local commits to remote"

**Claude Code**:
```
=== STEP 1: Pre-flight Checks ===

✓ Checking remote branch configuration...
✓ Verifying working directory is clean...
✓ Pre-flight checks passed!
```

**Claude Code**:
```
=== STEP 2: Fetch Latest Changes ===

Please open a NEW terminal and run:

    cd /Users/yue.weny/workspace/xhunterlib_merged
    git fetch origin

When prompted for SSH passphrase, enter it.

After fetch completes successfully, confirm here.
```

**User**: "Fetch completed successfully"

**Claude Code**:
```
=== STEP 3: Interactive Rebase ===

✓ Starting rebase...
✓ Configured rebase: pick first, squash others
✓ Generated commit message

=== STEP 4: Generated Summary ===

feat: implement JWT-based authentication

- Add role-based access control (RBAC) for API endpoints
- Create login/logout endpoints with proper security
- Store user sessions in Redis for scalability

fix: resolve token expiration edge cases

docs: update API documentation

chore: update dependencies

✓ Rebase completed successfully!

=== STEP 5: Manual Push Required ===

Please open a NEW terminal and execute:

    cd /Users/yue.weny/workspace/xhunterlib_merged
    git push --force-with-lease origin EI63633597_20240701_pfmiles

When prompted, enter your SSH key passphrase.

After completing the push, confirm here.
```

**User**: Opens new terminal, runs push command, enters passphrase

**User**: "Push completed successfully"

**Claude Code**: "✓ Excellent! Your changes have been pushed to the remote branch."

## Authentication Methods Supported

Since all network operations are manual, this works with:

- **SSH keys with passphrases** (recommended, most secure)
- **SSH agent** (if you've already run `ssh-add`)
- **HTTPS with username/password**
- **Personal access tokens**
- **GPG keys** (for signed commits)

## Why Fully Manual is Better

**Maximum Security**:
- Zero credential storage or transmission
- Passwords only entered in your terminal
- No environment variables or config files

**Complete Control**:
- Review each step before proceeding
- Abort at any point if needed
- Modify commands if necessary

**Universal Compatibility**:
- Works with any authentication setup
- No special tools required (sshpass, credential helpers, etc.)
- Compatible with all Git hosting providers

## Before Running This Skill

Ensure you:
1. Have committed all local changes (use `/git-commit` if needed)
2. Have SSH access to the remote repository
3. Have push permissions
4. Are prepared to enter your passphrase for git fetch and git push steps

## Workflow Details

### Automated Steps (Skill Handles):

1. **Pre-flight Checks**:
   - Verify remote branch tracking is configured
   - Check working directory has no uncommitted changes
   - Abort if prerequisites are not met

2. **Interactive Rebase**:
   ```bash
   git rebase -i origin/<branch-name>
   ```
   - Auto-edits todo list
   - Generates commit message
   - Completes rebase

3. **Generate Summary**:
   - Parse all squashed commit messages
   - Categorize by conventional commits types
   - Create functional and minor changes sections

### Manual Steps (You Handle):

1. **Fetch Changes**:
   ```bash
   git fetch origin
   # Enter passphrase when prompted
   ```

2. **Push Changes**:
   ```bash
   git push --force-with-lease origin <branch>
   # Enter passphrase when prompted
   ```

3. **Confirm Completion**:
   - Return to Claude Code
   - Report success or errors

## Tips for Best Results

1. **Open New Terminal for Each Manual Step**:
   - Keeps authentication isolated
   - Prevents session timeout issues
   - Clear separation of concerns

2. **Review Generated Message**:
   - Check that summary accurately reflects changes
   - Verify conventional commits format is followed
   - Ensure language preference applied correctly

3. **Use Descriptive Local Commits**:
   - Good local commit messages → better generated summary
   - Include feature/bug/refactor context
   - Write in language you prefer for final message

4. **Test SSH Connection First** (optional):
   ```bash
   ssh -T git@code.alipay.com
   ```

5. **Backup Before Force Push**:
   ```bash
   git branch backup-$(date +%Y%m%d)
   ```

## Common Issues

### If git fetch fails:
**Error**: "Unable to determine upstream commits" or "rebase errors"
**Solution**: The skill will detect this and prompt you to run `git fetch origin` manually in a new terminal

### If you enter wrong passphrase:
**Error**: "Permission denied (publickey)"
**Solution**: Terminal will prompt again. Ensure correct passphrase

### If rebase has conflicts:
**Solution**: Resolve conflicts, then `git rebase --continue`, then retry skill

### If remote branch doesn't exist:
**Solution**: Set up tracking with `git push -u origin HEAD`, then retry

## Why Only Fetch and Push Are Manual?

**Security Requirements**:
- Git fetch requires SSH key passphrase for network authentication
- Git push requires SSH key passphrase for network authentication
- These are the only steps that access remote repository over network

**All Other Steps Are Automated**:
- Pre-flight checks: Only read local git configuration and status
- Interactive rebase: Local operation, no network access needed
- Generate summary: Parse local git history, no authentication required

**Benefits**:
- You only enter passphrase for necessary network operations
- Non-sensitive operations run automatically for efficiency
- You still have full control before critical push operation

## Related Commands

- Check remote: `git remote -v`
- Test SSH: `ssh -T git@code.alipay.com`
- Check branch: `git branch -vv`
- View log: `git log --oneline -10`
- Manual rebase: `git rebase -i <remote-branch>`
- Manual push: `git push --force-with-lease origin <branch>`
- Abort rebase: `git rebase --abort`
