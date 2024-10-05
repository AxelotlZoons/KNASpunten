from flask import Blueprint, request, render_template, jsonify
from competition.competition_factory import competition_factory  # Ensure this import is correct
from formulas import points_formula


views = Blueprint('views', __name__)

@views.route('/')
def home():

    return render_template("home.html")

@views.route('/calculate', methods=['POST'])
def calculate():
    url = request.form.get("url")
    comp_type = request.form.get('comp_type')
    final_ranking = request.form.get('final_ranking')

    competition = competition_factory(url)
    percentage = competition.calculate_percentage()

    points = points_formula(percentage, comp_type, final_ranking)

    return jsonify({
        'percentage': percentage,
        'points': points
    })