from flask import Blueprint, request, render_template_string
from competition.competition_factory import competition_factory  # Ensure this import is correct


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return '''
        <h1>Competition Percentage Calculator</h1>
        <form action="/calculate" method="POST">
            <input type="text" name="url" placeholder="Enter competition URL" required>
            <button type="submit">Calculate</button>
        </form>
    '''

@views.route('/calculate', methods=['POST'])
def calculate_percentage():
    url = request.form.get('url')
    
    if not url:
        return "No URL provided", 400

    try:
        # Pass the URL to your competition logic
        competition = competition_factory(url)
        percentage = competition.calculate_percentage()
        
        # Return the result
        return render_template_string(f'<h2>The calculated percentage is: {percentage}%</h2>')
    except Exception as e:
        # Handle any errors that occur during processing
        return render_template_string(f'<h2>Error occurred: {str(e)}</h2>'), 500