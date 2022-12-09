from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto

app = Flask(__name__)


@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
    RejestrKont.dodaj_konto(konto)
    return jsonify("Konto stworzone"), 201


@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    return f"Ilośc kont w rejestrze {RejestrKont.ile_kont()}", 200


@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    print(f"Request o konto z peselem: {pesel}")
    konto = RejestrKont.wyszukaj_konto(pesel)
    print(konto)
    return jsonify(imie=konto.imie, nazwisko=konto.nazwisko, pesel=konto.pesel, saldo=konto.saldo), 200


@app.route("/konta/aktualizuj/<pesel>", methods=['PUT'])
def aktualizuj_konto(pesel):
    dane=request.json()
    print(f"Request o update konto z peselem: {pesel}")
    konto = RejestrKont.wyszukaj_konto(pesel)
    print("stare dane" + konto)
    if "imie" in dane:
        konto.imie = dane["imie"]
    if "nazwisko" in dane:
        konto.nazwisko = dane["nazwisko"]
    if "pesel" in dane:
        konto.pesel = dane["pesel"]
    if "saldo" in dane:
        konto.saldo = dane["saldo"]

    return jsonify("Update udany!"),200


@app.route("/konta/usun/<pesel>", methods=['DELETE'])
def usun_konto(pesel):
    print(f"Usuwanie konta z peselem: {pesel}")
    RejestrKont.usun_konto(pesel)

    return jsonify("konto usuniete!"), 200

# flask --app app/api.py --debug run
