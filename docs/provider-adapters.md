# Provider guidance selector

Publicist includes an experimental, offline selector that points agents to provider-owned setup and usage guidance. It does not implement API clients, MCP clients, OAuth, browser automation, credential storage, or delivery.

```sh
python3 scripts/provider_wizard.py us
python3 scripts/provider_wizard.py us --setup Hunter
```

The selected result includes the matching `wiki/public-relations/providers/<slug>.md` guide, an official fallback URL, the provider policy status, and `access_state: not_checked`. The selector never inspects environment variables, browser sessions, account state, or MCP configuration. Read the guide, then follow the provider's own API, MCP, skill, CLI, browser, or manual route as applicable.

The repository inventory remains available for inspection:

```sh
python3 scripts/provider_adapters.py --inventory
```

This command prints metadata only. Provider status (`supported`, `manual-only`, `permission-required`) describes the documented route and policy; it does not mean this checkout has access. Credentials stay in the provider's own client or the user's approved secret store. Sending, publishing, bulk export, and account changes require separate authorization.

If the companion wiki cannot be read from the installed skill, use the guide's dated official source links directly. If those sources are unavailable, report `guidance_unavailable` and continue the core country workflow where possible.
