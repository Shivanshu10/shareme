import sys
sys.path.append("../")

from shareme.shareable import Shareable

shareable=Shareable("testfile.txt", 0)
shareable.send()