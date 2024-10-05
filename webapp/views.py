from flask import Blueprint, request, render_template, render_template_string
from competition.competition_factory import competition_factory  # Ensure this import is correct
from formulas import points_formula


views = Blueprint('views', __name__)

@views.route('/')
def home():

    return render_template("home.html")

@views.route('/calculate', methods=['POST'])
def calculate():
    url = request.form.get('url')

    competition = competition_factory(url)
    percentage = competition.calculate_percentage()

    comp_type = request.form.get('comp_type')
    final_ranking = request.form.get('final_ranking')

    points = points_formula(percentage, comp_type, final_ranking)

    try:

        return render_template_string(f'<h2> {percentage}% <br> {points}</h2>')

    except Exception as e:
        return render_template_string(f'<h2>Error occurred: {str(e)}</h2>'), 500