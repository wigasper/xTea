from pathlib import Path

from typing import List


def write_serial_output(output_fp: Path, shell_script_fps: List[Path]):
    with open(output_fp, "w") as out:
        out.write("#!/bin/bash\n\n")

        for fp in shell_script_fps:
            out.write(f"bash {fp}\n")


def write_gnu_parallel_output(
    output_fp: Path, shell_script_fps: List[Path], num_threads: int
):
    with open(output_fp, "w") as out:
        out.write("#!/bin/bash\n\n")

        array_elements = "\n".join([f'"{fp}"' for fp in shell_script_fps])

        out.write("# Array of shell script file paths\n")
        out.write(f"shell_script_fps=({array_elements})\n\n")

        out.write(
            f'printf "%s\\n" "${{shell_script_fps[@]}}" | parallel -j {num_threads} bash {{}}'
        )
