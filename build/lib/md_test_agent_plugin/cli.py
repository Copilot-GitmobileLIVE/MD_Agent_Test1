from __future__ import annotations

import argparse
from pathlib import Path

from .installer import AGENT_NAME, export_agent, install_agent, load_agent_text


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Package, export, and install the MD_Test custom agent."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("show", help="Print the packaged agent definition.")

    export_parser = subparsers.add_parser("export", help="Write the packaged agent file to a path.")
    export_parser.add_argument("--output", required=True, help="Output path for the exported agent file.")
    export_parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite the output file if it already exists.",
    )

    install_parser = subparsers.add_parser(
        "install",
        help="Install the agent into a target workspace under .github/agents/.",
    )
    install_parser.add_argument(
        "--target-dir",
        required=True,
        help="Workspace root where the agent should be installed.",
    )
    install_parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing installed agent file.",
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "show":
        print(load_agent_text())
        return

    if args.command == "export":
        output_path = export_agent(Path(args.output), force=args.force)
        print(f"Exported {AGENT_NAME} to {output_path}")
        return

    if args.command == "install":
        installed_path = install_agent(Path(args.target_dir), force=args.force)
        print(f"Installed {AGENT_NAME} to {installed_path}")
        return

    parser.error(f"Unsupported command: {args.command}")