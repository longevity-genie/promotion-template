#!/usr/bin/env bash
# Pre-commit hook: sync AGENTS.md <-> CLAUDE.md
# Propagates the staged one to the other. Rejects if both staged but differ.
#
# Install: cp scripts/sync-agents-claude.sh .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit

REPO_ROOT="$(git rev-parse --show-toplevel)"
AGENTS="$REPO_ROOT/AGENTS.md"
CLAUDE="$REPO_ROOT/CLAUDE.md"

AGENTS_STAGED=false
CLAUDE_STAGED=false
git diff --cached --name-only | grep -qx "AGENTS.md" && AGENTS_STAGED=true
git diff --cached --name-only | grep -qx "CLAUDE.md" && CLAUDE_STAGED=true

if ! $AGENTS_STAGED && ! $CLAUDE_STAGED; then
    exit 0
fi

if $AGENTS_STAGED && $CLAUDE_STAGED; then
    AGENTS_HASH=$(git show :AGENTS.md | git hash-object --stdin)
    CLAUDE_HASH=$(git show :CLAUDE.md | git hash-object --stdin)
    if [ "$AGENTS_HASH" != "$CLAUDE_HASH" ]; then
        echo "ERROR: AGENTS.md and CLAUDE.md are both staged but differ."
        echo "They must have identical content. Make them match and re-stage."
        exit 1
    fi
    exit 0
fi

if $AGENTS_STAGED && ! $CLAUDE_STAGED; then
    cp "$AGENTS" "$CLAUDE"
    git add "$CLAUDE"
    echo "sync: copied AGENTS.md -> CLAUDE.md"
fi

if $CLAUDE_STAGED && ! $AGENTS_STAGED; then
    cp "$CLAUDE" "$AGENTS"
    git add "$AGENTS"
    echo "sync: copied CLAUDE.md -> AGENTS.md"
fi

exit 0
