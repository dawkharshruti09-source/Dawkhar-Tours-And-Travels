from flask import Flask, Response, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")        

@app.route("/robots.txt")
def robots():
    sitemap_url = f"{request.url_root.rstrip('/')}/sitemap.xml"
    return Response(f"User-agent: *\nAllow: /\nSitemap: {sitemap_url}\n", mimetype="text/plain")

@app.route("/sitemap.xml")
def sitemap():
    page_url = request.url_root.rstrip('/') + '/'
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url><loc>{page_url}</loc></url>
</urlset>'''
    return Response(xml, mimetype="application/xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)