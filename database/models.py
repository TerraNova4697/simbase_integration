from datetime import datetime, time, date
from typing import Annotated

from sqlalchemy import Integer, DateTime, String, SmallInteger, Numeric, Date, Boolean, Time, Double, \
    LargeBinary, Text
from sqlalchemy.dialects.mysql import MEDIUMTEXT, BLOB, TINYINT
from sqlalchemy.orm import Mapped, mapped_column

from database.simbase_database import Base


pk = Annotated[int, mapped_column(Integer, primary_key=True)]
id_sm_key = Annotated[int, mapped_column(Integer, unique=True)]
vc255 = Annotated[str, mapped_column(String(length=255), nullable=True)]
boolnull = Annotated[bool, mapped_column(Boolean, nullable=True)]
doublenull = Annotated[float, mapped_column(Double, nullable=True)]
dtnull = Annotated[datetime, mapped_column(DateTime, nullable=True)]
intnull = Annotated[int, mapped_column(Integer, nullable=True)]
smallintnull = Annotated[int, mapped_column(SmallInteger, nullable=True)]


class Filial(Base):
    __tablename__ = "filials"

    id: Mapped[pk]
    id_sm: Mapped[int]
    name: Mapped[vc255]
    sm_state: Mapped[vc255]
    date_modified: Mapped[dtnull]
    date_created: Mapped[dtnull]


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[id_sm_key]
    name: Mapped[vc255]
    bin: Mapped[vc255]
    status: Mapped[vc255]
    sm_state: Mapped[vc255]
    date_modified: Mapped[dtnull]
    date_created: Mapped[dtnull]


class Object(Base):
    __tablename__ = 'objects'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[id_sm_key]
    filial_id_sm: Mapped[intnull]
    customer_id_sm: Mapped[intnull]
    contract_id_sm: Mapped[intnull]
    contract: Mapped[vc255]
    name: Mapped[vc255]
    contract_date: Mapped[Date] = mapped_column(Date, nullable=True)
    contract_number: Mapped[vc255]
    type: Mapped[vc255]
    sm_state: Mapped[vc255]
    date_modified: Mapped[dtnull]
    date_created: Mapped[dtnull]


class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[pk]
    id_sm: Mapped[id_sm_key]
    filial_id_sm: Mapped[intnull]
    customer_id_sm: Mapped[intnull]
    object_id_sm: Mapped[intnull]
    name: Mapped[vc255]
    type: Mapped[vc255]
    shift_mode: Mapped[intnull]
    operating_mode: Mapped[vc255]
    linear_part: Mapped[str] = mapped_column(MEDIUMTEXT, nullable=True)
    length_from: Mapped[doublenull]
    length_to: Mapped[doublenull]
    sm_state: Mapped[vc255]
    date_modified: Mapped[dtnull]
    date_created: Mapped[dtnull]


class MobileGroup(Base):
    __tablename__ = "mobile_groups"

    i_id: Mapped[int] = mapped_column(primary_key=True)
    id_sb_object_filial: Mapped[int]
    id_sb_object_zakazchik: Mapped[int]
    id_sb_object_object: Mapped[int]
    id_sb_object_post: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_mob_group: Mapped[int]
    mobile_group_name: Mapped[str] = mapped_column(Text)
    operating_mode: Mapped[str] = mapped_column(Text)
    shift_mode: Mapped[str] = mapped_column(Text)
    linear_part: Mapped[str] = mapped_column(Text)
    length_from: Mapped[str] = mapped_column(Text)
    length_to: Mapped[str] = mapped_column(Text)
    date: Mapped[datetime]


class Triggering(Base):
    __tablename__ = 'triggerings'

    id: Mapped[pk]
    id_sm: Mapped[intnull]
    filial_id_sm: Mapped[intnull]
    object_id_sm: Mapped[intnull]
    post_id_sm: Mapped[intnull]
    type: Mapped[vc255]
    customer: Mapped[vc255]
    reason: Mapped[vc255]
    description: Mapped[vc255]
    place: Mapped[vc255]
    departure_mg: Mapped[smallintnull]
    departure_time: Mapped[dtnull]
    arrival_time: Mapped[dtnull]
    response_time: Mapped[time] = mapped_column(Time, nullable=True)
    mg_moment_of_actuation: Mapped[vc255]
    trigger_date: Mapped[dtnull]
    sm_state: Mapped[vc255]
    date_modified: Mapped[dtnull]
    date_created: Mapped[dtnull]


class Income(Base):
    __tablename__ = "income_payments"

    id: Mapped[pk]
    filial_id_sm: Mapped[intnull]
    contract_id_sm: Mapped[intnull]
    type: Mapped[vc255]
    status: Mapped[vc255]
    year: Mapped[intnull]
    month: Mapped[vc255]
    contract_amount: Mapped[doublenull]
    additional_agreement_amount: Mapped[doublenull]
    amount_avr: Mapped[doublenull]
    payment_date_avr: Mapped[Date] = mapped_column(Date, nullable=True)
    actual_payment: Mapped[doublenull]
    payment_date_actual: Mapped[Date] = mapped_column(Date, nullable=True)
    deviation_amount: Mapped[doublenull]
    deviation_from_avr: Mapped[doublenull]
    deviation_from_contract_prc: Mapped[vc255]
    deviation_from_avr_prc: Mapped[vc255]
    remainder: Mapped[doublenull]
    comment: Mapped[str] = mapped_column(String(length=255), nullable=True)
    additional_comment: Mapped[str] = mapped_column(String(length=255), nullable=True)
    sm_state: Mapped[vc255]
    date_modified: Mapped[dtnull]
    date_created: Mapped[dtnull]


class Contract(Base):
    __tablename__ = "contracts"

    id: Mapped[pk]
    id_sm: Mapped[intnull]
    start_date: Mapped[Date] = mapped_column(Date, nullable=True)
    warning_date: Mapped[Date] = mapped_column(Date, nullable=True)
    end_date: Mapped[Date] = mapped_column(Date, nullable=True)
    customer_id_sm: Mapped[intnull]
    name: Mapped[vc255]
    type: Mapped[vc255]
    contract_number: Mapped[vc255]
    sm_state: Mapped[vc255]
    date_modified: Mapped[dtnull]
    date_created: Mapped[dtnull]





class Car(Base):
    __tablename__ = 'cars'

    i_id: Mapped[int] = mapped_column(primary_key=True)
    id_sb_cars: Mapped[int] = mapped_column(Integer, nullable=True)
    brand: Mapped[str] = mapped_column(Text, nullable=True)
    model: Mapped[str] = mapped_column(Text, nullable=True)
    state_number: Mapped[str] = mapped_column(Text, nullable=True)
    engine_displacement: Mapped[str] = mapped_column(Text, nullable=True)
    fuel: Mapped[str] = mapped_column(Text, nullable=True)
    year_of_production: Mapped[int] = mapped_column(Integer, nullable=True)
    mileage: Mapped[int] = mapped_column(Integer, nullable=True)
    card_of_refueling: Mapped[int] = mapped_column(Integer, nullable=True)
    battery_name: Mapped[str] = mapped_column(Text, nullable=True)
    battery_life_years: Mapped[int] = mapped_column(Integer, nullable=True)
    battery_life: Mapped[Date] = mapped_column(Date, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class CommunicationMeans(Base):
    __tablename__ = 'communication_means'

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sb_object_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_zakazchik: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_mob_group: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_post: Mapped[int] = mapped_column(Integer, nullable=True)
    wearable_radios: Mapped[int] = mapped_column(Integer, nullable=True)
    car_radios: Mapped[int] = mapped_column(Integer, nullable=True)
    stationary_radios: Mapped[int] = mapped_column(Integer, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class CommunicationFacilitiy(Base):
    __tablename__ = "communication_facilities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    sm_state: Mapped[vc255]
    filial_id_sm: Mapped[intnull]
    customer_id_sm: Mapped[intnull]
    post_id_sm: Mapped[intnull]
    wearable_radios_quantity: Mapped[smallintnull]
    сar_radios_quantity: Mapped[smallintnull]
    stationary_radios_quantity: Mapped[smallintnull]
    date_modified: Mapped[dtnull]
    date_created: Mapped[dtnull]


class Driver(Base):
    __tablename__ = 'drivers'

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    is_sb_drivers: Mapped[int] = mapped_column(Integer, nullable=True)
    object_name: Mapped[str] = mapped_column(Text, nullable=True)
    name: Mapped[str] = mapped_column(Text, nullable=True)
    surname: Mapped[str] = mapped_column(Text, nullable=True)
    job_title: Mapped[str] = mapped_column(Text, nullable=True)
    employee_photo: Mapped[LargeBinary] = mapped_column(LargeBinary, nullable=True)
    gender: Mapped[str] = mapped_column(Text, nullable=True)
    nationality: Mapped[str] = mapped_column(Text, nullable=True)
    customer: Mapped[str] = mapped_column(Text, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class OsNma(Base):
    __tablename__ = "OS_NMA"

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sb_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    nomenclature: Mapped[str] = mapped_column(Text, nullable=True)
    type: Mapped[str] = mapped_column(Text, nullable=True)
    name_short: Mapped[str] = mapped_column(Text, nullable=True)
    code1C: Mapped[int] = mapped_column(Integer, nullable=True)
    inventory_number: Mapped[int] = mapped_column(Integer, nullable=True)
    OS_groups: Mapped[str] = mapped_column(Text, nullable=True)
    name_of_reg_type: Mapped[str] = mapped_column(Text, nullable=True)
    serial_number: Mapped[str] = mapped_column(Text, nullable=True)
    expiration_date: Mapped[Date] = mapped_column(Date, nullable=True)
    state: Mapped[str] = mapped_column(Text, nullable=True)
    brief_description: Mapped[str] = mapped_column(Text, nullable=True)
    battery_life: Mapped[Date] = mapped_column(Date, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class Event(Base):
    __tablename__ = "events"

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sb_object_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    event_type: Mapped[str] = mapped_column(Text, nullable=True)
    data_to_police: Mapped[str] = mapped_column(Text, nullable=True)
    case_to_police: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    act_to_security_council: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    customer_employees: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    kmg_security_employees: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    contractor_employees: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    commit_date: Mapped[Date] = mapped_column(Date, nullable=True)
    time: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    customer: Mapped[str] = mapped_column(Text, nullable=True)
    amount_of_damage: Mapped[str] = mapped_column(Text, nullable=True)
    full_name: Mapped[str] = mapped_column(Text, nullable=True)
    kmgs_ltd: Mapped[str] = mapped_column(Text, nullable=True)
    third_party: Mapped[str] = mapped_column(Text, nullable=True)
    disciplinary: Mapped[str] = mapped_column(Text, nullable=True)
    kui: Mapped[str] = mapped_column(Text, nullable=True)
    erdr: Mapped[str] = mapped_column(Text, nullable=True)
    sb: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(Text, nullable=True)


class FilialDirector(Base):
    __tablename__ = "filial_director"

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sb_director_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    name: Mapped[str] = mapped_column(Text, nullable=True)
    surname: Mapped[str] = mapped_column(Text, nullable=True)
    job_title: Mapped[str] = mapped_column(Text, nullable=True)
    employee_photo: Mapped[LargeBinary] = mapped_column(LargeBinary, nullable=True)
    gender: Mapped[str] = mapped_column(Text, nullable=True)
    nationality: Mapped[str] = mapped_column(Text, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class FilialLd(Base):
    __tablename__ = "filial_ld"

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    s_filial: Mapped[str] = mapped_column(Text, nullable=True)
    i_count: Mapped[int] = mapped_column(Integer, nullable=True)
    i_max: Mapped[int] = mapped_column(Integer, nullable=True)
    d_first: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    d_new: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class Incident(Base):
    __tablename__ = "incidents"

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sb_object_filial: Mapped[int] = mapped_column(Integer)
    incident_type: Mapped[str] = mapped_column(Text, nullable=True)
    case_to_police: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    act_to_security_council: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    customers_employees: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    kmg_security_employees: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    contractor_employees: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    commit_date: Mapped[Date] = mapped_column(Date, nullable=True)
    time: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    customer: Mapped[str] = mapped_column(Text, nullable=True)
    amount_of_damage: Mapped[str] = mapped_column(Text, nullable=True)
    full_name: Mapped[str] = mapped_column(Text, nullable=True)
    kmgs_ltd: Mapped[str] = mapped_column(Text, nullable=True)
    third_party: Mapped[str] = mapped_column(Text, nullable=True)
    disciplinary: Mapped[str] = mapped_column(Text, nullable=True)
    kui: Mapped[str] = mapped_column(Text, nullable=True)
    erdr: Mapped[str] = mapped_column(Text, nullable=True)
    sb: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(Text, nullable=True)


class Inventory(Base):
    __tablename__ = "inventory"

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sb_tmz: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    nomenclature: Mapped[str] = mapped_column(Text, nullable=True)
    state: Mapped[str] = mapped_column(Text, nullable=True)
    name_short: Mapped[str] = mapped_column(Text, nullable=True)
    product_group: Mapped[str] = mapped_column(Text, nullable=True)
    warehouse: Mapped[str] = mapped_column(Text, nullable=True)
    object: Mapped[str] = mapped_column(Text, nullable=True)
    post: Mapped[str] = mapped_column(Text, nullable=True)
    remainder: Mapped[str] = mapped_column(Text, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class IssuanceOfOsTmz(Base):
    __tablename__ = "issuance_of_OS_TMZ"

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sb_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    nomenclature: Mapped[str] = mapped_column(Text, nullable=True)
    name_short: Mapped[str] = mapped_column(Text, nullable=True)
    product_group: Mapped[str] = mapped_column(Text, nullable=True)
    warehouse: Mapped[str] = mapped_column(Text, nullable=True)
    object: Mapped[str] = mapped_column(Text, nullable=True)
    post: Mapped[str] = mapped_column(Text, nullable=True)
    remainder: Mapped[str] = mapped_column(Text, nullable=True)
    date: Mapped[Date] = mapped_column(DateTime, nullable=True)


class Journal(Base):
    __tablename__ = "journals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    sm_state: Mapped[vc255]
    filial_id_sm: Mapped[intnull]
    customer_id_sm: Mapped[intnull]
    post_id_sm: Mapped[intnull]
    journal_transfer_of_weapons_and_ammunition: Mapped[boolnull]
    journal_finery: Mapped[boolnull]
    journal_aboard: Mapped[boolnull]
    journal_list_of_way: Mapped[boolnull]
    journal_information_and_recording: Mapped[boolnull]
    journal_transfers_of_inventory_items: Mapped[boolnull]
    journal_acceptance_log_for_premises_delivery: Mapped[boolnull]
    journal_visitors: Mapped[boolnull]
    journal_vehicle_registration: Mapped[boolnull]
    date_modified: Mapped[dtnull]
    date_created: Mapped[dtnull]


class MobileGroupComposition(Base):
    __tablename__ = "mobile_group_composition"

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_guard: Mapped[int] = mapped_column(Integer, nullable=True)
    id_driver: Mapped[int] = mapped_column(Integer, nullable=True)
    id_car: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object: Mapped[int] = mapped_column(Integer, nullable=True)
    job_title: Mapped[str] = mapped_column(Text, nullable=True)
    subdivision: Mapped[str] = mapped_column(Text, nullable=True)
    shift_mode: Mapped[str] = mapped_column(Text, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class Transport(Base):
    __tablename__ = "transports"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    sm_state: Mapped[vc255]

    filial_id_sm: Mapped[intnull]
    customer_id_sm: Mapped[intnull]
    post_id_sm: Mapped[intnull]

    transport_quantity: Mapped[smallintnull]
    additional_necessary_transport_quantity: Mapped[smallintnull]
    GPS: Mapped[smallintnull]
    date_modified: Mapped[dtnull]
    date_created: Mapped[dtnull]


class Offense(Base):
    __tablename__ = "offenses"

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sb_object_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    offense_type: Mapped[str] = mapped_column(Text, nullable=True)
    data_to_police: Mapped[str] = mapped_column(Text, nullable=True)
    case_to_police: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    act_to_security_council: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    customer_employees: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    kmg_security_employees: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    contractor_employees: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    commit_date: Mapped[Date] = mapped_column(Date, nullable=True)
    time: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    customer: Mapped[str] = mapped_column(Text, nullable=True)
    amount_of_damage: Mapped[str] = mapped_column(Text, nullable=True)
    full_name: Mapped[str] = mapped_column(Text, nullable=True)
    kmgs_ltd: Mapped[str] = mapped_column(Text, nullable=True)
    third_party: Mapped[str] = mapped_column(Text, nullable=True)
    disciplinary: Mapped[str] = mapped_column(Text, nullable=True)
    kui: Mapped[str] = mapped_column(Text, nullable=True)
    erdr: Mapped[str] = mapped_column(Text, nullable=True)
    sb: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(Text, nullable=True)


class ProvidingWorkwears(Base):
    __tablename__ = "providing_workwears"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    sm_state: Mapped[vc255]
    filial_id_sm: Mapped[intnull]
    customer_id_sm: Mapped[intnull]
    post_id_sm: Mapped[intnull]
    summer_set: Mapped[smallintnull]
    winter_set: Mapped[smallintnull]
    reflective_vets: Mapped[smallintnull]
    summer_shoes: Mapped[smallintnull]
    winter_shoes: Mapped[smallintnull]
    date_modified: Mapped[dtnull]
    date_created: Mapped[dtnull]


class RequirementRequest(Base):
    __tablename__ = "requirement_request"

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sb_object_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    nomination: Mapped[str] = mapped_column(Text, nullable=True)
    quantity: Mapped[str] = mapped_column(Text, nullable=True)
    brief_description: Mapped[str] = mapped_column(Text, nullable=True)
    name: Mapped[str] = mapped_column(Text, nullable=True)
    code: Mapped[float] = mapped_column(Double, nullable=True)
    feature: Mapped[str] = mapped_column(Text, nullable=True)
    to_whom: Mapped[str] = mapped_column(Text, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class RouteSheet(Base):
    __tablename__ = "route_sheet"

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sb_object_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_object: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_mob_group: Mapped[int] = mapped_column(Integer, nullable=True)
    route_number: Mapped[str] = mapped_column(Text, nullable=True)
    id_sb_mashina: Mapped[int] = mapped_column(Integer, nullable=True)
    base_object_name: Mapped[str] = mapped_column(Text, nullable=True)
    protected_area: Mapped[str] = mapped_column(Text, nullable=True)
    length_of_perimeter_of_area: Mapped[str] = mapped_column(Text, nullable=True)
    area_of_sector: Mapped[str] = mapped_column(Text, nullable=True)
    senior_driver_guard: Mapped[str] = mapped_column(Text, nullable=True)
    driver_guard_1: Mapped[str] = mapped_column(Text, nullable=True)
    driver_guard_2: Mapped[str] = mapped_column(Text, nullable=True)
    bypass_post_guard: Mapped[str] = mapped_column(Text, nullable=True)
    working_time_from: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    working_time_to: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    route_task_prepared: Mapped[str] = mapped_column(Text, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class SecurityGuard(Base):
    __tablename__ = "security_guards"

    id: Mapped[pk]
    id_sm: Mapped[id_sm_key]
    filial_id_sm: Mapped[intnull]
    customer_id_sm: Mapped[intnull]
    object_id_sm: Mapped[intnull]
    name: Mapped[vc255]
    surname: Mapped[vc255]
    iin: Mapped[vc255]
    social_status: Mapped[vc255]
    status: Mapped[vc255]
    job_title: Mapped[vc255]
    employee_photo: Mapped[BLOB] = mapped_column(BLOB, nullable=True)
    gender: Mapped[vc255]
    nationality: Mapped[vc255]
    labor_union: Mapped[vc255]
    sm_state: Mapped[vc255]
    date_modified: Mapped[dtnull]
    date_created: Mapped[dtnull]


class ShiftSchedule(Base):
    __tablename__ = "shift_schedule"

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sb_object_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_object: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_post: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_ohranniki: Mapped[int] = mapped_column(Integer, nullable=True)
    shift_date: Mapped[Date] = mapped_column(Date, nullable=True)
    day_of_week: Mapped[str] = mapped_column(Text, nullable=True)
    shift_type: Mapped[str] = mapped_column(Text, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class SpecialEquipment(Base):
    __tablename__ = "special_equipment"

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sb_object_mob_group: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_spec_sredstva: Mapped[int] = mapped_column(Integer, nullable=True)
    nomination: Mapped[str] = mapped_column(Text, nullable=True)
    type: Mapped[str] = mapped_column(Text, nullable=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class Staff(Base):
    __tablename__ = "staff"

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sb_object_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    staffing_level: Mapped[int] = mapped_column(Integer, nullable=True)
    payroll: Mapped[int] = mapped_column(Integer, nullable=True)
    actual_number: Mapped[int] = mapped_column(Integer, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class StaffTurnover(Base):
    __tablename__ = "staff_turnover"

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sb_object_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    staffing_level: Mapped[int] = mapped_column(Integer, nullable=True)
    payroll: Mapped[int] = mapped_column(Integer, nullable=True)
    accepted: Mapped[int] = mapped_column(Integer, nullable=True)
    fired: Mapped[int] = mapped_column(Integer, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class TrainingAndMedicalService(Base):
    __tablename__ = 'training_and_medical_services'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    sm_state: Mapped[vc255]

    filial_id_sm: Mapped[intnull]
    customer_id_sm: Mapped[intnull]
    post_id_sm: Mapped[intnull]

    annual_retraining_of_security_guards_quantity: Mapped[smallintnull]
    anti_terrorism_training_quantity: Mapped[smallintnull]
    annual_medical_examination_quantity: Mapped[smallintnull]
    annual_medical_examination_quantity: Mapped[smallintnull]
    pre_shift_medical_examination_quantity: Mapped[smallintnull]
    date_modified: Mapped[dtnull]
    date_created: Mapped[dtnull]


class Weapons(Base):
    __tablename__ = "weapons"

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sb_object_mob_group: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_oruzhie: Mapped[int] = mapped_column(Integer, nullable=True)
    weapon: Mapped[str] = mapped_column(Text, nullable=True)
    type_of_weapon: Mapped[str] = mapped_column(Text, nullable=True)
    weapon_number: Mapped[int] = mapped_column(Integer, nullable=True)
    ammunition: Mapped[int] = mapped_column(Integer, nullable=True)
    weapons: Mapped[int] = mapped_column(Integer, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class WeaponsAndSpecialEquipment(Base):
    __tablename__ = "weapons_and_special_quipment"

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sb_object_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_zakazchik: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_mob_group: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_post: Mapped[int] = mapped_column(Integer, nullable=True)
    firearms: Mapped[int] = mapped_column(Integer, nullable=True)
    handcuffs: Mapped[int] = mapped_column(Integer, nullable=True)
    pr_73: Mapped[int] = mapped_column(Integer, nullable=True)
    regulatory: Mapped[int] = mapped_column(Integer, nullable=True)
    electric_lantern: Mapped[int] = mapped_column(Integer, nullable=True)
    headlight_finder: Mapped[int] = mapped_column(Integer, nullable=True)
    inspection_mirror: Mapped[int] = mapped_column(Integer, nullable=True)
    metal_detectors: Mapped[int] = mapped_column(Integer, nullable=True)
    binoculars: Mapped[int] = mapped_column(Integer, nullable=True)
    safe: Mapped[int] = mapped_column(Integer, nullable=True)
    wearable_video_recorders: Mapped[int] = mapped_column(Integer, nullable=True)
    car_dvr: Mapped[int] = mapped_column(Integer, nullable=True)
    cell_phones: Mapped[int] = mapped_column(Integer, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class Shift(Base):
    __tablename__ = "shifts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[intnull]
    filial_id_sm: Mapped[intnull]
    object_id_sm: Mapped[intnull]
    post_id_sm: Mapped[intnull]
    security_guard_id_sm: Mapped[intnull]
    security_guard_replaced_id_sm: Mapped[intnull]
    joined_posts: Mapped[boolnull]
    shift_date: Mapped[Date] = mapped_column(Date, nullable=True)
    shift_type: Mapped[vc255]
    sm_state: Mapped[vc255]
    date_modified: Mapped[dtnull]
    date_created: Mapped[dtnull]


class ContractTRU(Base):
    __tablename__ = 'contract_TRU'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[intnull]
    name: Mapped[vc255]
    sm_state: Mapped[vc255]
    date_modified: Mapped[dtnull]
    date_created: Mapped[dtnull]


class Fine(Base):
    __tablename__ = "fines"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[intnull]
    filial_id_sm: Mapped[intnull]
    customer_id_sm: Mapped[intnull]
    circumstances: Mapped[str] = mapped_column(Text, nullable=True)
    violation_type: Mapped[vc255]
    fine_type: Mapped[vc255]
    request_amount: Mapped[doublenull]
    recognition_amount: Mapped[doublenull]
    fine_number: Mapped[vc255]
    fine_date: Mapped[date] = mapped_column(Date, nullable=True)
    decision: Mapped[vc255]
    sm_state: Mapped[vc255]
    date_modified: Mapped[dtnull]
    date_created: Mapped[dtnull]


class LegalClaims(Base):
    __tablename__ = 'legal_claims'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[intnull]
    sm_state: Mapped[vc255]
    responsible_employee_id_sm: Mapped[intnull]
    contract_TRU_id_sm: Mapped[intnull]
    conclusion_date: Mapped[date] = mapped_column(Date, nullable=True)
    contract_number: Mapped[vc255]
    applicant: Mapped[vc255]
    defendant: Mapped[vc255]
    case_classification: Mapped[vc255]
    property_requirements: Mapped[vc255]
    currency: Mapped[vc255]
    non_property_claims: Mapped[vc255]
    grounds_of_claim: Mapped[vc255]
    result: Mapped[vc255]
    dishonest_supplier: Mapped[int] = mapped_column(TINYINT, nullable=True)
    date_modified: Mapped[dtnull]
    date_created: Mapped[dtnull]


class Employee(Base):
    __tablename__ = 'employee'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[intnull]
    employee: Mapped[vc255]
    name: Mapped[vc255]
    second_name: Mapped[vc255]
    middle_name: Mapped[vc255]
    filial_id_sm: Mapped[intnull]
    job_title: Mapped[vc255]
    job_type: Mapped[vc255]
    subdivision: Mapped[vc255]
    iin: Mapped[vc255]
    personnel_number: Mapped[vc255]
    gender: Mapped[vc255]
    nationality: Mapped[vc255]
    birth_date: Mapped[Date] = mapped_column(Date, nullable=True)
    place_of_birth: Mapped[vc255]
    social_status: Mapped[vc255]
    employee_type: Mapped[vc255]
    type: Mapped[vc255]
    position_level: Mapped[vc255]
    reserved: Mapped[int] = mapped_column(TINYINT, nullable=True)
    labor_union: Mapped[vc255]
    nomenclature_CEO: Mapped[int] = mapped_column(TINYINT, nullable=True)
    nomenclature_CA: Mapped[int] = mapped_column(TINYINT, nullable=True)
    retiree: Mapped[int] = mapped_column(TINYINT, nullable=True)
    member_collective_agreement: Mapped[int] = mapped_column(TINYINT, nullable=True)
    wage_rate: Mapped[int] = mapped_column(TINYINT, nullable=True)
    salary: Mapped[int] = mapped_column(TINYINT, nullable=True)
    rating: Mapped[int] = mapped_column(TINYINT, nullable=True)
    sm_state: Mapped[vc255]
    date_modified: Mapped[dtnull]
    date_created: Mapped[dtnull]
