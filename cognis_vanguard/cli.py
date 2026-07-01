"""Cognis Vanguard CLI."""

from __future__ import annotations

import argparse
import json
import os
import sys

from . import __version__
from . import extract as extractmod
from . import graph as graphmod
from . import report as reportmod
from . import stix as stixmod
from .agents import Orchestrator

_HERE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.normpath(os.path.join(_HERE, "..", "data"))


def _load(p):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)


def _data(name):
    return os.path.join(DATA_DIR, name)


def cmd_demo(args):
    reports = _load(_data("sample_reports.json"))
    gaz = _load(_data("gazetteer.json"))
    orch = Orchestrator(reports, gaz)
    result = orch.answer(args.query or "financing network infrastructure wallet", k=3)
    print(reportmod.render_text(result))
    print(f"\nKnowledge graph: {len(orch.graph.entities)} entities, {len(orch.graph.edges)} edges")
    if args.stix:
        with open(args.stix, "w", encoding="utf-8") as f:
            f.write(stixmod.to_json(stixmod.bundle_from_graph(orch.graph)))
        print(f"[+] STIX 2.1 bundle -> {args.stix}")
    return 0


def cmd_query(args):
    reports = _load(args.reports)
    gaz = _load(args.gazetteer) if args.gazetteer else {}
    orch = Orchestrator(reports, gaz)
    result = orch.answer(args.q, k=args.k)
    print(reportmod.render_json(result) if args.json else reportmod.render_text(result))
    return 0


def cmd_extract(args):
    reports = _load(args.reports)
    gaz = _load(args.gazetteer) if args.gazetteer else {}
    print(json.dumps(extractmod.extract(reports, gaz), indent=2))
    return 0


def cmd_correlate(args):
    reports = _load(args.reports)
    gaz = _load(args.gazetteer) if args.gazetteer else {}
    g = graphmod.build_graph(reports, gaz)
    print(json.dumps(graphmod.correlate(g, args.value, args.type), indent=2))
    return 0


def cmd_graph(args):
    reports = _load(args.reports)
    gaz = _load(args.gazetteer) if args.gazetteer else {}
    g = graphmod.build_graph(reports, gaz)
    out = stixmod.to_json(stixmod.bundle_from_graph(g)) if args.stix else json.dumps(g.to_dict(), indent=2)
    print(out)
    return 0


def build_parser():
    p = argparse.ArgumentParser(prog="cognis-vanguard",
                                description="Cognis Vanguard — self-hosted multi-INT fusion & orchestration")
    p.add_argument("--version", action="version", version=f"cognis-vanguard {__version__}")
    sub = p.add_subparsers(dest="command", required=True)

    d = sub.add_parser("demo", help="end-to-end demo on bundled reporting")
    d.add_argument("--query")
    d.add_argument("--stix")
    d.set_defaults(func=cmd_demo)

    q = sub.add_parser("query", help="answer a query with source citations")
    q.add_argument("--reports", required=True)
    q.add_argument("--gazetteer")
    q.add_argument("--q", required=True)
    q.add_argument("--k", type=int, default=3)
    q.add_argument("--json", action="store_true")
    q.set_defaults(func=cmd_query)

    e = sub.add_parser("extract", help="extract entities from reports")
    e.add_argument("--reports", required=True)
    e.add_argument("--gazetteer")
    e.set_defaults(func=cmd_extract)

    c = sub.add_parser("correlate", help="entities co-mentioned with a target")
    c.add_argument("--reports", required=True)
    c.add_argument("--gazetteer")
    c.add_argument("--value", required=True)
    c.add_argument("--type")
    c.set_defaults(func=cmd_correlate)

    g = sub.add_parser("graph", help="emit knowledge graph (JSON or STIX)")
    g.add_argument("--reports", required=True)
    g.add_argument("--gazetteer")
    g.add_argument("--stix", action="store_true")
    g.set_defaults(func=cmd_graph)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
