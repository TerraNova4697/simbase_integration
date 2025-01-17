from database.models import *
from database.queries.filial_orm import FilialOrm
from database.queries.offense_orm import OffenseOrm
from database.queries.incident_orm import IncidentOrm
from database.queries.event_orm import EventOrm
from database.queries.customer_orm import CustomerOrm
from database.queries.object_orm import ObjectOrm
from database.queries.income_orm import IncomeOrm
from database.queries.post_orm import PostOrm
from database.queries.mobile_group_orm import MobileGroupOrm
from datetime import datetime, date
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
    for month in range(12):
        curr_date = datetime(2024, month+1, randrange(1,28))

        for i in range(randrange(5, 25)):

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
                date=curr_date,
                commit_date=curr_date,
                time=curr_date,
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
    for month in range(12):
        curr_date = datetime(2024, month+1, randrange(1,28))

        for i in range(randrange(5, 25)):

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
                date=curr_date,
                commit_date=curr_date,
                time=curr_date,
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
    for month in range(12):
        curr_date = datetime(2024, month+1, randrange(1,28))

        for i in range(randrange(5, 25)):
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
                date=curr_date,
                commit_date=curr_date,
                time=curr_date,
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


# def mock_income():
#     last_id = 1
#     customers = Customer.get_all()
#     for customer in customers:
#         IncomeOrm.insert(
#             id_sb_object_filial=customer.id_sb_object_filial,
#             id_sb_object_zakazchik=customer.id_sb_object_zakazchik,
#             id_sb_object_object=
#         )


def mock_objects_and_income():
    last_id = 1
    for month in range(12):
        customers = CustomerOrm.get_all()
        for customer in customers:
            num_of_objects = randrange(1, 20)
            filial = FilialOrm.get_by_sb_id(customer.id_sb_object_filial)
            curr_date = date(2024, month+1, 1)
            for i in range(num_of_objects):
                obj = ObjectOrm.insert_object(
                    id_sb_object_filial=filial.id_sb_object_filial,
                    id_sb_object_zakazchik=customer.id_sb_object_zakazchik,
                    id_sb_object_object=last_id,
                    object_name=faker.street_name() + ", " + faker.city(),
                    dogovor=faker.text(500),
                    dogovor_date=curr_date,
                    dogovor_num=randrange(1, 100000),
                    object_type=choice(["Здание", "Трубопровод"]),
                    d_date=curr_date,
                    sb_id_dogovor=last_id
                )

                inc = IncomeOrm.insert(
                    id_sb_object_filial=customer.id_sb_object_filial,
                    id_sb_object_zakazchik=customer.id_sb_object_zakazchik,
                    id_sb_object_object=last_id,
                    id_sb_object_dogovor=last_id,
                    year=2024,
                    month=month+1,
                    contract_amount=choice(contract_amounts),
                    add_aggr_amount=choice(aggr_amounts),
                )
                last_id += 1


def mock_posts():
    last_id = 1
    objects = ObjectOrm.get_all()
    for obj in objects:
        num_of_posts = randrange(3, 30)
        post_num = 1
        for post in range(num_of_posts):
            PostOrm.insert(
                id_sb_object_filial=obj.id_sb_object_filial,
                id_sb_object_zakazchik=obj.id_sb_object_zakazchik,
                id_sb_object_object=obj.id_sb_object_object,
                id_sb_object_post=last_id,
                post_name=f"{post_num}, {obj.object_name}",
                post_type=choice(["обходной пост", "стационарный пост"]),
                d_date=date.today()
            )
            post_num += 1
            last_id += 1


def mock_mobile_groups():
    last_id = 1
    objects = ObjectOrm.get_all()
    for obj in objects:
        num_of_mg = randrange(1, 5)
        for mg in range(num_of_mg):
            MobileGroupOrm.insert(
                id_sb_object_filial=obj.id_sb_object_filial,
                id_sb_object_zakazchik=obj.id_sb_object_zakazchik,
                id_sb_object_object=obj.id_sb_object_object,
                id_sb_object_mob_group=last_id,
                mg_name=f"МГ. {randrange(20, 400)}",
                work_mode="",
                shift_mode="",
                linear_part="",
                length_from="",
                length_to="",
                d_date=date.today()
            )
            last_id += 1


def mock():
    mock_filials()
    mock_customers()
    mock_offenses()
    mock_incidents()
    mock_events()
    mock_objects_and_income()
    mock_posts()
    