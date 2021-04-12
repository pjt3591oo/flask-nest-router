from flask import Blueprint, render_template
from flask import jsonify

router = Blueprint('test2', __name__)

@router.route('/a')
def test_a():
  return jsonify({
    "data": 'test2/a'
  })

@router.route('/b')
def test_b():
  return jsonify({
    "data": 'test2/b'
  })