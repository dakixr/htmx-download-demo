from flask import Flask, render_template, send_file
from io import BytesIO
from pygments import highlight
from pygments.lexers import PythonLexer, HtmlLexer
from pygments.formatters import HtmlFormatter
from time import sleep
import code_fragments as cf

app = Flask(__name__)
app.static_folder = "static"
app.template_folder = "templates"


# Choose a vibrant Pygments style, e.g., 'monokai', 'colorful', 'solarized-dark'
PYGMENTS_STYLE = 'monokai'

@app.route("/")
def index():
    # Create a formatter with the chosen style and additional options
    formatter = HtmlFormatter(style=PYGMENTS_STYLE, cssclass="codehilite")

    # Highlight the backend and frontend code using Pygments
    highlighted_backend_code = highlight(cf.backend_code, PythonLexer(), formatter)
    highlighted_frontend_code = highlight(cf.frontend_code, HtmlLexer(), formatter)

    # Get the CSS styles from the formatter
    pygments_css = formatter.get_style_defs('.codehilite')

    # Render the template with highlighted code and CSS
    return render_template(
        "index.html",
        highlighted_backend_code=highlighted_backend_code,
        highlighted_frontend_code=highlighted_frontend_code,
        pygments_css=pygments_css
    )


@app.route("/file_download")
def file_download():

    # Simulate a file preparation delay
    sleep(3)

    file_content = "This is a file"
    buffer = BytesIO(file_content.encode("utf-8"))

    return send_file(
        buffer,
        download_name="file.txt",
    )


if __name__ == "__main__":
    app.run(debug=True, port=8000)
