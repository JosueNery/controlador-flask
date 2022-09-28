""" from flask import Blueprint, render_template, request, redirect, url_for

from ..extensions import db
from ..models.aluno import Alunos
from datetime import date, datetime

alBp = Blueprint('alBp', __name__)


@alBp.route('/alunos')
def alBp_list():
    alBp_query = alBp.query.all()
    return render_template('alBp_list.html', alBp=alBp_query)


@alBp.route('/alunos/add', methods=['POST'])
def add_alBp():

    sNome = request.form["nome"]
    sTipo = request.form["tipo"]
    dInicio = datetime.strptime(request.form["inicio"], '%Y-%m-%d')
    dFim = datetime.strptime(request.form["fim"], '%Y-%m-%d')

    uc = Uc(nome=sNome, tipo=sTipo, inicio=dInicio, fim=dFim)
    db.session.add(uc)
    db.session.commit()

    return redirect(url_for('ucBp.uc_list'))


@alBp.route('/uc/update/<uc_id>')
def update_uc(uc_id=0):
    uc_query = Uc.query.filter_by(id=uc_id).first()
    return render_template('uc_update.html', uc=uc_query)


@alBp.route('/uc/upd', methods=['POST'])
def upd_uc():

    iUc = request.form["id"]
    sNome = request.form["nome"]
    sTipo = request.form["tipo"]
    dInicio = datetime.strptime(request.form["inicio"], '%Y-%m-%d')
    dFim = datetime.strptime(request.form["fim"], '%Y-%m-%d')

    uc = Uc.query.filter_by(id=iUc).first()
    uc.nome = sNome
    uc.tipo = sTipo
    uc.inicio = dInicio
    uc.fim = dFim
    db.session.add(uc)
    db.session.commit()

    return redirect(url_for('ucBp.uc_list'))


@alBp.route('/uc/delete/<uc_id>')
def delete_uc(uc_id=0):
    uc_query = Uc.query.filter_by(id=uc_id).first()
    return render_template('uc_delete.html', uc=uc_query)


@alBp.route('/uc/dlt', methods=['POST'])
def dtl_uc():

    iUc = request.form["id"]
    uc = Uc.query.filter_by(id=iUc).first()
    db.session.delete(uc)
    db.session.commit()

    return redirect(url_for('ucBp.uc_list'))
 """
