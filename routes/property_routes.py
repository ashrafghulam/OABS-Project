from flask import Blueprint, render_template
from models.property import Property

property_bp = Blueprint('property', __name__)

@property_bp.route('/properties')
def property_list():
    properties = Property.query.all()
    return render_template('property_list.html', properties=properties)
