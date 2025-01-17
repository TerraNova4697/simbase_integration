from database.models import *
from database.queries.filial_orm import FilialOrm
from database.queries.offense_orm import OffenseOrm
from database.queries.incident_orm import IncidentOrm
from database.queries.event_orm import EventOrm
from database.queries.customer_orm import CustomerOrm
from database.queries.object_orm import ObjectOrm
from datetime import datetime
from random import randrange, random, choice
from fixtures import *
from faker import Faker


faker = Faker('ru_RU')


def mock_filials():
    FilialOrm.insert_filial(
        s_name_filial="Актюбинский филиал", id_sb_object_filial=663, d_date=datetime.now()
    )
    FilialOrm.insert_filial(
        s_name_filial="Атырауский филиал", id_sb_object_filial=664, d_date=datetime.now()
    )
    FilialOrm.insert_filial(
        s_name_filial="Жанаозенский филиал", id_sb_object_filial=665, d_date=datetime.now()
    )
    FilialOrm.insert_filial(
        s_name_filial="Центральный аппарат", id_sb_object_filial=666, d_date=datetime.now()
    )
    FilialOrm.insert_filial(
        s_name_filial="Карагандинский филиал", id_sb_object_filial=667, d_date=datetime.now()
    )
    FilialOrm.insert_filial(
        s_name_filial="Кульсаринский филиал", id_sb_object_filial=668, d_date=datetime.now()
    )
    FilialOrm.insert_filial(
        s_name_filial="Мангистауский филиал", id_sb_object_filial=669, d_date=datetime.now()
    )
    FilialOrm.insert_filial(
        s_name_filial="Южно - Казахстанский филиал", id_sb_object_filial=670, d_date=datetime.now()
    )
    FilialOrm.insert_filial(
        s_name_filial="Западно - Казахстанский филиал", id_sb_object_filial=673, d_date=datetime.now()
    )
    FilialOrm.insert_filial(
        s_name_filial="Кызылординский филиал", id_sb_object_filial=675, d_date=datetime.now()
    )
    FilialOrm.insert_filial(
        s_name_filial="Павлодарский филиал", id_sb_object_filial=676, d_date=datetime.now()
    )
    FilialOrm.insert_filial(
        s_name_filial="Специальное подразделение охраны по г. Астана", id_sb_object_filial=677, d_date=datetime.now()
    )


def mock_customers():
    filials = FilialOrm.get_id_sb_object_filials()
    for i in range(50):
        CustomerOrm.insert_customer(
            s_name=faker.company(),
            id_sb_object_filial=choice(filials),
            id_sb_object_zakazchik=i,
            s_bin=faker.bic(),
            d_date=datetime.now()
        )
    

def mock_offenses():
    filials = FilialOrm.get_all_filials()

    for i in range(10):
        filial = choice(filials)
        offence = choice(offense_types)
        customers = CustomerOrm.get_customers_by_filial(filial.id_sb_object_filial)


        OffenseOrm.insert_offense(
            id_sb_object_filial=filial.id_sb_object_filial,
            offense_type=offence,
            data_to_police=faker.text(500),
            case_to_police=choice([0,1]),
            act_to_security_council=choice([0,1]),
            customer_employees=choice([0,1]),
            kmg_security_employees=choice([0,1]),
            contractor_employees=choice([0,1]),
            date=datetime.now(),
            commit_date=datetime.now(),
            time=datetime.now(),
            customer=choice(customers).s_name,
            amount_of_damage=str(choice(damage_amounts)),
            full_name=offence,
            kmgs_ltd="",
            third_party="",
            disciplinary="",
            kui="",
            erdr="",
            sb="",
            status=""
        )


def mock_incidents():
    filials = FilialOrm.get_all_filials()

    for i in range(10):
        filial = choice(filials)
        incident = choice(incident_types)
        customers = CustomerOrm.get_customers_by_filial(filial.id_sb_object_filial)

        IncidentOrm.insert_incident(
            id_sb_object_filial=filial.id_sb_object_filial,
            incident_type=incident,
            # data_to_police=faker.text(500),
            case_to_police=choice([0,1]),
            act_to_security_council=choice([0,1]),
            customers_employees=choice([0,1]),
            kmg_security_employees=choice([0,1]),
            contractor_employees=choice([0,1]),
            date=datetime.now(),
            commit_date=datetime.now(),
            time=datetime.now(),
            customer=choice(customers).s_name,
            amount_of_damage=str(choice(damage_amounts)),
            full_name=incident,
            kmgs_ltd="",
            third_party="",
            disciplinary="",
            kui="",
            erdr="",
            sb="",
            status=""
        )


def mock_events():
    filials = FilialOrm.get_all_filials()

    for i in range(10):
        filial = choice(filials)
        event = choice(event_types)
        customers = CustomerOrm.get_customers_by_filial(filial.id_sb_object_filial)

        EventOrm.insert_event(
            id_sb_object_filial=filial.id_sb_object_filial,
            event_type=event,
            data_to_police=faker.text(500),
            case_to_police=choice([0,1]),
            act_to_security_council=choice([0,1]),
            customer_employees=choice([0,1]),
            kmg_security_employees=choice([0,1]),
            contractor_employees=choice([0,1]),
            date=datetime.now(),
            commit_date=datetime.now(),
            time=datetime.now(),
            customer=choice(customers).s_name,
            amount_of_damage=str(choice(damage_amounts)),
            full_name=event,
            kmgs_ltd="",
            third_party="",
            disciplinary="",
            kui="",
            erdr="",
            sb="",
            status=""
        )


# def mock_objects():
    # last_id = 1
    # customers = Customer.get_all()
    # for customer in customers:
    #     num_of_objects = randrange(1, 20)
    #     filial = FilialOrm.get_by_sb_id(customer.id_sb_object_filial)

    #     for i in range(num_of_objects):
    #         ObjectOrm.insert_object(
    #             id_sb_object_filial=filial.id_sb_object_filial,
    #             id_sb_object_zakazchik=customer.id_sb_object_zakazchik,
    #             id_sb_object_object=last_id,
    #             object_name=faker.place_name(),
    #             dogovor=faker.text(500)

    #         )


def mock():
    mock_filials()
    mock_customers()
    mock_offenses()
    mock_incidents()
    mock_events()
    