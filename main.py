from pathlib import Path
from staticfg import CFGBuilder

directory_path = Path("./benchmarks")
bench_names = [file.stem for file in directory_path.iterdir() if file.is_file()]

for bench_name in bench_names:
    cfg_builder = CFGBuilder()
    cfg = cfg_builder.build_from_file(bench_name, f"./benchmarks/{bench_name}.py")
    cfg.build_visual(f"results/plots/{bench_name}", "pdf", show=False)
