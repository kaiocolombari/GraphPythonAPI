import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def fig_to_base64(fig):
    buf = io.BytesIO()
    FigureCanvas(fig).print_png(buf)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")
