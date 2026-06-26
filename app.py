from flask import Flask, redirect

app = Flask(__name__)

links = {
   "folder/SwJw1LzQRp_SlviJg8oBY0I7Ql8eAw": "https://urlto.me/2LF6"
}

@app.route("/<path:slug>")
def redirecionar(slug):
    url = links.get(slug)
    if url:
        return redirect(url)
    return "Link não encontrado", 404

if __name__ == "__main__":
    app.run(debug=True)
