from flask import Flask, render_template, send_from_directory, jsonify, request
import json
import os
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()

app = Flask(__name__, static_folder='public', static_url_path='')

FILE_NAME = os.getenv("FILE_NAME", "tickets.json")

def load_tickets():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_tickets(tickets):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tickets, file, indent=4)


# ---------------------------------------------------------
# RUTAS WEB (FRONTEND)
# ---------------------------------------------------------
@app.route('/')
def home():
    return send_from_directory('public', 'index.html')


# ---------------------------------------------------------
# RUTAS DE LA API (BACKEND PARA EL FRONTEND)
# ---------------------------------------------------------

# 1. Listar todos los tickets (GET)
@app.route('/api/tickets', methods=['GET'])
def api_list_tickets():
    tickets = load_tickets()
    return jsonify(tickets)


# 2. Crear un nuevo ticket (POST)
@app.route('/api/tickets', methods=['POST'])
def api_create_ticket():
    data = request.get_json()
    
    user = data.get("user")
    serial_number = data.get("serial_number", "").strip()
    issue = data.get("issue")
    category = data.get("category", "General")
    priority = data.get("priority", "Medium")

    if not user or not serial_number or not issue:
        return jsonify({"error": "Faltan campos obligatorios (user, serial_number, issue)"}), 400

    tickets = load_tickets()
    
    # Validar número de serie duplicado
    for ticket in tickets:
        if ticket.get("serial_number") == serial_number:
            return jsonify({"error": f"El número de serie '{serial_number}' ya existe."}), 400

    ticket_id = len(tickets) + 1

    new_ticket = {
        "id": ticket_id,
        "serial_number": serial_number,
        "user": user,
        "category": category,
        "issue": issue,
        "priority": priority,
        "status": "Open"
    }

    tickets.append(new_ticket)
    save_tickets(tickets)

    return jsonify(new_ticket), 201


# 3. Cerrar un ticket (PATCH)
@app.route('/api/tickets/<int:ticket_id>/close', methods=['PATCH'])
def api_close_ticket(ticket_id):
    tickets = load_tickets()
    
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            ticket["status"] = "Closed"
            save_tickets(tickets)
            return jsonify({"mensaje": "Ticket cerrado exitosamente", "ticket": ticket})

    return jsonify({"error": "Ticket no encontrado"}), 404


if __name__ == "__main__":
    # Importante escuchar en 0.0.0.0 para que Docker lo exponga correctamente
    app.run(host="0.0.0.0", port=3000, debug=True)