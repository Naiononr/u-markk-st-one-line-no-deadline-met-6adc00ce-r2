"""One Line, No Deadline Met — a single-line excuse for a missed deadline.

Writes the line to /output/entry.txt (or $OUTPUT_DIR/entry.txt locally).
Final line: Sorry I missed the deadline — I left it with tomorrow, and
tomorrow turned out to be a very convincing liar.
"""

import os
import tempfile

LINE = "Sorry I missed the deadline \u2014 I left it with tomorrow, and tomorrow turned out to be a very convincing liar."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(LINE + "\n")
        os.chmod(tmp, 0o644)
        os.replace(tmp, os.path.join(out_dir, "entry.txt"))
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
