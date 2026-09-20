"""CLI for MCP server starter."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .generator import generate_server


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="x4-mcp")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init")
    p_init.add_argument("name")
    p_init.add_argument("--tools", type=int, default=2)
    p_init.add_argument("--out", default=".")

    sub.add_parser("doctor")
    sub.add_parser("test")
    sub.add_parser("security")
    sub.add_parser("validate")

    args = parser.parse_args(argv)

    if args.cmd == "init":
        path = generate_server(args.name, Path(args.out), tools=args.tools)
        print(f"created {path}")
        return 0

    if args.cmd == "doctor":
        print("doctor: scaffold layout checks (MVP)")
        for req in ("pyproject.toml", "README.md", "src"):
            ok = Path(req).exists()
            print(f"  {'OK' if ok else 'MISSING'} {req}")
        return 0

    if args.cmd in ("test", "security", "validate"):
        print(f"{args.cmd}: run via CI or install companion tools (x4-sec)")
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
