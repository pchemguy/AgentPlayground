---
name: sdd-forge
description: Use when projecting software-development phases, milestones, and tasks to a hosted repository; creating or reconciling GitHub labels, milestones, and task issues; finding an issue for a task ID; or closing a verified task issue. GitHub is the available backend. Ordinary local Git and SDD work does not require hosting access.
---

# Hosted task coordination

## Shared protocol

- **Scope:** Run only for a requested hosted operation. Identify the provider before loading its backend; report ambiguous remotes or unsupported providers without guessing. Local SDD work does not require hosting access.
- **Hierarchy:** Use the **sdd-conventions** task hierarchy to read phase, milestone, and task IDs and names from TASKS or the active FEATURE-TASKS and preserve their parentage in the host projection. The selected backend defines its concrete objects.
- **Coordination:** Before a hosted mutation, **sdd-manage** coordinates the user's request and a current **sdd-orient** handoff establishing the eligible Git worktree and governing instructions. Read-only inspection needs no Git mutation gate.
- **Credentials:** Use the available authenticated client or a suitable supplied token. **sdd-manage** discovers, accepts, and persists tokens under **sdd-conventions**' **Hosting tokens** rules and recovers the affected client's authentication when needed. A direct caller may supply a token to **sdd-forge**. Consume it through a protected mechanism without ordinary handoff/output exposure; Git shell authentication does not prove API-client access. The selected backend defines provider-specific checks and permission requirements.
- **Access failure:** For a backend access-related 403, request a suitable token from **sdd-manage** and return the endpoint, required access, and any provider-indicated non-credential cause without exposing the credential. The coordinator checks credential suitability and identifies any policy or other restriction requiring a different remedy; escalation does not require substituting a token when the existing credential is suitable. For direct use without **sdd-manage**, ask the user. Recheck access before retrying; a replacement token does not establish permission by itself.
- **Operational failure:** Let the selected backend distinguish access failures, rate limits, service/transport outages, invalid requests, and uncertain writes. Preserve successful independent results and return pending/unknown effects with bounded retry or deferred-reconciliation context; do not route every 403 to credential replacement.
- **Handoff:** Return the repository, task ID to issue number and URL associations, changed objects, access failures, ambiguity, and remaining differences. Pass issue references to implementation and reporting for commit composition. Issue state does not establish task completion.

Do not create commits, push branches, or create or merge pull requests here.

Add a backend only when it supports a concrete hosted operation with its own repository resolution, authentication, object mapping, and reconciliation rules. Give it a focused reference and explicit trigger; do not advertise a provider before its workflow is defined.

## Available backends

- **GitHub:** Read [GitHub backend](references/github.md) when the requested operation targets a GitHub repository. It resolves repository identity and access, then routes task projection and issue lifecycle operations.
