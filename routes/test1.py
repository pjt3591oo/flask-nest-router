from flask import Blueprint, render_template
from flask import jsonify

router = Blueprint('', __name__)

@router.route('/a')
def test_a():
  return jsonify({
    'data': 'test1/a'
  })

@router.route('/b')
def test_b():
  return jsonify({
    "data": 'test1/b'
  })