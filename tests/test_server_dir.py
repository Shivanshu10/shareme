import sys
sys.path.append("../")

from shareme.shareable import Shareable

shareable=Shareable("test_dir", 0)
shareable.send()
