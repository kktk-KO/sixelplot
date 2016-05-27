import matplotlib
import matplotlib.pyplot as plt
import sixel
import sys
import io
def show(output = sys.stdout):
    buf = io.BytesIO()
    plt.savefig(buf)
    buf.seek(0)
    writer = sixel.SixelWriter()
    writer.draw(buf, output = output)
