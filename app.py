from flask import Flask, render_template,request,jsonify
from services.ai_service import analisar_codigo


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analisar", methods=["POST"])
def analisar():
    try:
        data = request.get_json()
        
        if not data or "codigo" not in data:
            return jsonify({"erro": "Nenhum código enviado"}), 400

        codigo = data["codigo"]

        resposta = analisar_codigo(codigo)

        return jsonify({"resultado": resposta})

    except Exception as e:
        print("ERRO NO BACKEND:", str(e))  # <- isso mostra no terminal
        return jsonify({"erro": str(e)}), 500
   
if __name__ == '__main__':
     app.run(host="0.0.0.0",port="500")