from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto

app = Flask(__name__)


@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    if RejestrKont.wyszukaj_konto(dane["pesel"]) is None:
        konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
        RejestrKont.dodaj_konto(konto)
        return jsonify("Konto stworzone"), 201
    else:
        return jsonify("Ten pesel ma już konto !"), 400


@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    return f"Ilośc kont w rejestrze: {RejestrKont.ile_kont()}", 200


@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    print(f"Request o konto z peselem: {pesel}")
    konto = RejestrKont.wyszukaj_konto(pesel)
    print(konto)
    return jsonify(imie=konto.imie, nazwisko=konto.nazwisko, pesel=konto.pesel, saldo=konto.saldo), 200


@app.route("/konta/aktualizuj/<pesel>", methods=['PUT'])
def aktualizuj_konto(pesel):
    dane = request.get_json()
    print(f"Request o update konta z danymi: {dane}")
    konto = RejestrKont.wyszukaj_konto(pesel)
    print("konto znalezione")
    konto.imie = dane["imie"] if "imie" in dane else konto.imie
    konto.nazwisko = dane["nazwisko"] if "nazwisko" in dane else konto.nazwisko
    konto.pesel = dane["pesel"] if "pesel" in dane else konto.pesel
    konto.saldo = dane["saldo"] if "saldo" in dane else konto.saldo
    return jsonify(imie=konto.imie, nazwisko=konto.nazwisko, pesel=konto.pesel, saldo=konto.saldo), 200


@app.route("/konta/usun/<pesel>", methods=['DELETE'])
def usun_konto(pesel):
    if RejestrKont.usun_konto(pesel):
        return jsonify("Konto zostalo usuniete"), 200
    else:
        return jsonify("Nie ma takiego konta"), 404

# flask --app app/api.py --debug run
