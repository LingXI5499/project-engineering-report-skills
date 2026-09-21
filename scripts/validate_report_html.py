#!/usr/bin/env python3
"""Validate the mandatory offline, Star Rain Notes report shell."""
from __future__ import annotations

import argparse
from pathlib import Path

REQUIRED = {
    "UTF-8 charset": "charset=\"utf-8\"",
    "fixed Chinese brand": "星雨笔录",
    "fixed English brand": "STAR RAIN NOTES · ENGINEERING REPORT",
    "PDF-only button": 'id="export-pdf"',
    "native print export": "window.print()",
    "print stylesheet": "@media print",
    "A4 page setup": "@page",
    "offline presentation": "<style>",
}
FORBIDDEN_EXPORT_MARKERS = ("导出 DOCX", "导出 Word", "导出 Markdown", "导出图片", "下载 HTML")


def validate(path: Path) -> list[str]:
    html = path.read_text(encoding="utf-8").lower()
    errors = [f"缺少：{label}" for label, marker in REQUIRED.items() if marker.lower() not in html]
    errors.extend(f"不应提供其他导出：{marker}" for marker in FORBIDDEN_EXPORT_MARKERS if marker.lower() in html)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="校验星雨笔录工程报告的统一主题和 PDF 导出外壳")
    parser.add_argument("html", nargs="+", type=Path, help="要校验的 UTF-8 HTML 文件")
    args = parser.parse_args()
    failed = False
    for path in args.html:
        try:
            errors = validate(path)
        except (OSError, UnicodeDecodeError) as exc:
            errors = [str(exc)]
        if errors:
            failed = True
            print(f"FAIL {path}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {path}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
