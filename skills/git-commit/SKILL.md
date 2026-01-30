---
name: git-commit
description: Commits all current changes to git with conventional commits format by default. Generates type-scoped commit messages (feat, fix, docs, etc.) automatically from code analysis. Use for any git commit operation - automatically stages changes, analyzes impacts, and creates properly formatted conventional commits. Supports multi-language messages and custom type overrides.
---

# Git Commit

Automatically commit changes with intelligent conventional commits format.

## Quick Start

Commit all changes:
```
Commit all my changes
```

## How It Works

1. Stages all changes (new, modified, deleted files)
2. Analyzes code changes to determine commit type
3. Generates conventional commit message
4. Creates the commit

## Commit Types (Auto-Detected)

The skill automatically determines the appropriate type:

- `feat:` New features (correlates with MINOR version)
- `fix:` Bug fixes (correlates with PATCH version)
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc)
- `refactor:` Code refactoring
- `perf:` Performance improvements
- `test:` Test additions or modifications
- `build:` Build system changes
- `ci:` CI/CD changes
- `chore:` Other changes

## Examples

### Basic Usage
User: "Commit all my changes"
Generated: ```feat(auth): implement JWT-based authentication```

### With Language Preference
User: "用中文提交所有改动"
Generated: ```feat(认证): 实现基于JWT的认证系统```

### With Custom Type
User: "Commit as docs update"
Generated: ```docs: update API documentation```

### Without Conventional Commits
User: "Commit without conventional format"
Generated: ```Add user authentication feature``` (old format)

## Parameters

Natural language parameters:

- **Language**: "in French", "用中文", "en español"
- **Custom type**: "as feat", "as fix", "as docs update"
- **Scope**: "for API module", "in auth component"
- **Override**: "without conventional format"

Example:
```
Commit in Chinese, as fix, for auth module
```

## Advanced

### Breaking Changes

For breaking changes, use:
```
Commit with breaking change
```

Generated:
```
feat(api)!: remove deprecated endpoints

BREAKING CHANGE: Old API v1 endpoints no longer available
```

### Custom Scopes

Specify scope for better organization:
```
Commit changes for database module
```

Generated: ```feat(database): add connection pooling```

## Tips

- Review generated messages before confirming
- Use custom types to override auto-detection
- Scope helps organize commits in monorepos
- For WIP commits: "Commit WIP" (generates chore: WIP)
