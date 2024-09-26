backend_code = """
@app.route("/file_download")
def file_download():
    
    # Simulate a file preparation delay
    sleep(3)
    
    file_content = "This is a file"
    buffer = BytesIO(file_content.encode("utf-8"))
    
    return send_file(
        buffer,
        download_name="file.txt",
    )"""
    
frontend_code ="""
<style>
    .my-indicator {
        visibility: hidden;
        height: 0;
        scale: 0;
        margin-left: 0;
        transition: all 0.5s;
    }

    .htmx-request.my-indicator {
        height: 1.5rem;
        visibility: visible;
        scale: 1;
        margin-left: 1rem;
    }
</style>

<button hx-get="/file_download"
        hx-ext="htmx-download"
        hx-indicator="#spinner">
    Download File
    <img src="static/indicator.svg" id="spinner" class="my-indicator">
</button>"""