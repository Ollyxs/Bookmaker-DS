def load_clientes():
    fake = Faker('es_ES')
    for _ in range(100):
        cliente = Cliente(nombre=fake.first_name(), apellido=fake.name(), email=fake.email())
        db.session.add(cliente)
        db.session.commit()

    db.session.close()



def load_equipos():
    with open('./database/equipo.csv', encoding='utf-8') as csv_file:
        try:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                equipo = Equipo(nombre=row[0], escudo=row[1], pais=row[2], puntaje=float(row[3]))
                cuota = Cuota(probabilidad_local=float(row[4]),probabilidad_empate=float(row[5]), probabilidad_visitante=float(row[6]))

                equipo.cuota=cuota
                db.session.add(equipo)

                db.session.commit()
            db.session.close()
        except:
            db.session.rollback()
