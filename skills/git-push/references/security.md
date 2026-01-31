# Security Information

## Security Benefits

This skill ensures **maximum security** by:

- **Never storing credentials** in environment variables
- **Never writing passwords** to configuration files
- **Requiring manual execution** only for network operations needing password authentication (fetch and push)
- **Keeping authentication entirely in your control**
- **Automating non-sensitive operations** for better user experience

### Why Fully Manual is Better

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

## Why Only Fetch and Push Are Manual?

**Security Requirements**:
- Git fetch requires SSH key passphrase for network authentication
- Git push requires SSH key passphrase for network authentication
- These are the only steps accessing remote repository over network

**All Other Steps Are Automated**:
- Pre-flight checks: Only read local git configuration and status
- Interactive rebase: Local operation, no network access needed
- Generate summary: Parse local git history, no authentication required

**Benefits**:
- You only enter passphrase for necessary network operations
- Non-sensitive operations run automatically for efficiency
- You still have full control before critical push operation

## Authentication Methods Supported

Since all network operations are manual, this works with:

- **SSH keys with passphrases** (recommended, most secure)
- **SSH agent** (if you've already run `ssh-add`)
- **HTTPS with username/password**
- **Personal access tokens**
- **GPG keys** (for signed commits)

## Before Running This Skill

Ensure you:
1. Have committed all local changes (use `/git-commit` if needed)
2. Have SSH access to the remote repository
3. Have push permissions
4. Are prepared to enter your passphrase for git fetch and git push steps
