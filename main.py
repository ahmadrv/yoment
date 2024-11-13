from staticfg import CFGBuilder

cfg_builder = CFGBuilder()
cfg = cfg_builder.build_from_file('greatest_of_3', './greatest_of_3.py')

cfg.build_visual('greatest_of_3', 'pdf', show=False)