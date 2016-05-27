import matplotlib
import matplotlib.pyplot as plt
import io
import sixel

def plot():
    buf = io.BytesIO()
    plt.savefig(buf)
    buf.seek(0)
    writer = sixel.SixelWriter()
    writer.draw(buf)
