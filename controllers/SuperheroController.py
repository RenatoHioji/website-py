from flask import Flask, request, jsonify, abort

def init_app(app):
    
    @app.route('/superheroes', methods=['POST'])
    def create_superhero():
        data = request.get_json()
        name = data.get('name')
        moral = data.get('moral')
        history = data.get('history')

        if not name:
            abort(400, description="Name is required.")
    
        superhero = Superhero(name=name, moral=moral, history=history)
        db.session.add(superhero)
        db.session.commit()
        return jsonify({
            'id': superhero.id,
            'name': superhero.name,
            'moral': superhero.moral,
            'history': superhero.history
        }), 201

    @app.route('/superheroes', methods=['GET'])
    def get_superheroes():
        superheroes = Superhero.query.all()
        return jsonify([{
            'id': hero.id,
            'name': hero.name,
            'moral': hero.moral,
            'history': hero.history
        } for hero in superheroes])

    @app.route('/superheroes/<int:id>', methods=['GET'])
    def get_superhero(id):
        superhero = Superhero.query.get(id)
        if not superhero:
            abort(404, description="Superhero not found.")
        return jsonify({
            'id': superhero.id,
            'name': superhero.name,
            'moral': superhero.moral,
            'history': superhero.history
        })

    @app.route('/superheroes/<int:id>', methods=['PUT'])
    def update_superhero(id):
        data = request.get_json()
        name = data.get('name')
        moral = data.get('moral')
        history = data.get('history')

        superhero = Superhero.query.get(id)
        if not superhero:
            abort(404, description="Superhero not found.")  

        if name is not None:
            superhero.name = name
        if moral is not None:
            superhero.moral = moral
        if history is not None:
            superhero.history = history

        db.session.commit()
        return jsonify({
            'id': superhero.id,
            'name': superhero.name,
            'moral': superhero.moral,
            'history': superhero.history
        })
        
    @app.route('/superheroes/<int:id>', methods=['DELETE'])
    def delete_superhero(id):
        superhero = Superhero.query.get(id)
        if not superhero:
            abort(404, description="Superhero not found.")
        db.session.delete(superhero)
        db.session.commit()
        return '', 204
