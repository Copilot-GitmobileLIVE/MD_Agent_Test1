# MD_Test Agent Plugin

This project wraps the `MD_Test` custom agent in an installable Python package.

After installation, the package can:

- print the packaged agent definition
- export the agent file to a chosen location
- install the agent into another workspace under `.github/agents/MD_Test.agent.md`

## Install

```powershell
pip install -e .
```

## Commands

Show the bundled agent definition:

```powershell
md-test-agent show
```

Install the agent into another workspace:

```powershell
md-test-agent install --target-dir C:\path\to\other-workspace
```

Export the raw agent file anywhere:

```powershell
md-test-agent export --output C:\temp\MD_Test.agent.md
```

Overwrite an existing installed file:

```powershell
md-test-agent install --target-dir C:\path\to\other-workspace --force
```

## What gets installed

The installer writes:

```text
.github\agents\MD_Test.agent.md
```

inside the target workspace.

## Notes

This package exports the agent in the VS Code custom agent format. If another platform uses a different plugin or manifest format, use `md-test-agent export` and adapt the exported Markdown file to that platform's expected layout.