"""One Line, No Deadline Met — a single-line excuse for a missed deadline.

Writes the line to /output/entry.txt (or $OUTPUT_DIR/entry.txt locally).
Draft line: Sorry it's late — my calendar said 'due tomorrow' every day
this week, and honestly, I believed it every single time.
"""

import os
import tempfile

LINE = "Sorry it's late \u2014 my calendar said 'due tomorrow' every day this week, and honestly, I believed it every single time."


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
