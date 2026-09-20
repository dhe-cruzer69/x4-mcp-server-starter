from pathlib import Path
from x4_mcp_starter.generator import generate_server


def test_generate(tmp_path):
    path = generate_server("demo", tmp_path, tools=2)
    assert (path / "pyproject.toml").exists()
    assert (path / "mcp.json").exists()
    assert (path / "src" / "demo" / "server.py").exists()
