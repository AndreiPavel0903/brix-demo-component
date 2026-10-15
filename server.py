"""A tiny MCP server with one tool, used as a demo component for Brix."""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("brix-demo")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers and return the sum."""
    return a + b


if __name__ == "__main__":
    mcp.run()
