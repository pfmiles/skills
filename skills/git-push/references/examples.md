# Complete Example Sessions

## Basic Usage Example

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

    cd /Users/yue.weny/workspace/project
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

    cd /Users/yue.weny/workspace/project
    git push --force-with-lease origin feature-branch

When prompted, enter your SSH key passphrase.

After completing the push, confirm here.
```

**User**: Opens new terminal, runs push command, enters passphrase

**User**: "Push completed successfully"

**Claude Code**: "✓ Excellent! Your changes have been pushed to the remote branch."

## Multi-Scenario Examples

### Scenario 1: Multiple Feature Commits
**Local commits**: `feat: add user registration` → `fix: validation bug` → `docs: registration guide`

**Result**: Single commit with conventional commits summary

### Scenario 2: Mixed Changes
**Local commits**: `feat: payment integration` → `refactor: payment validation` → `test: add payment tests`

**Result**: Properly categorized feat and fix sections

### Scenario 3: Language Preference
**User**: "用中文推送本地提交"

**Result**: Commit message generated in Chinese with translated conventional commits types