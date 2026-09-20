# x4-mcp-server-starter

[![CI](https://github.com/dhe-cruzer69/x4-mcp-server-starter/actions/workflows/ci.yml/badge.svg)](https://github.com/dhe-cruzer69/x4-mcp-server-starter/actions)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)

**Generate a tested, security-aware MCP server scaffold in seconds.**

Scaffold ≠ production. This tool produces a complete project layout with tests, CI, and hooks for `x4-ai-security-scanner`.

## Quick start

```bash
pip install -e ".[dev]"
x4-mcp init demo-server --tools 2
cd demo-server
x4-mcp doctor
pytest -q
```

## CLI

```text
x4-mcp init <name>
x4-mcp doctor
x4-mcp test
x4-mcp security   # invokes x4-sec when installed
x4-mcp validate
```

## License

Apache-2.0
