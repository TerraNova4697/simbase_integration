from datetime import datetime, time
from numbers import Integral

from sqlalchemy import Integer, DateTime, Float, String, SmallInteger, Numeric, Date, Boolean, Time, Double, \
    LargeBinary, Text, nulls_last, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from database.simbase_database import Base


class Filial(Base):
    __tablename__ = "filial"

    i_id: Mapped[int] = mapped_column(primary_key=True)
    name_filial: Mapped[str] = mapped_column(Text)
    id_sb_object_filial: Mapped[int]
    date: Mapped[datetime]


class Customer(Base):
    __tablename__ = "customers"

    i_id: Mapped[int] = mapped_column(primary_key=True)
    name_customer: Mapped[str] = mapped_column(Text)
    id_sb_object_zakazchik: Mapped[int] = mapped_column(Integer, unique=True)
    bin: Mapped[str] = mapped_column(Text)
    date: Mapped[datetime]


class Object(Base):
    __tablename__ = 'objects'

    i_id: Mapped[int] = mapped_column(primary_key=True)
    id_sb_object_filial: Mapped[int]
    id_sb_object_zakazchik: Mapped[int]
    id_sb_object_object: Mapped[int] = mapped_column(Integer, unique=True)
    object_name: Mapped[str] = mapped_column(Text, nullable=True)
    contract: Mapped[str] = mapped_column(Text)
    id_sb_object_dogovor: Mapped[int]
    contract_date: Mapped[Date] = mapped_column(Date)
    contract_number: Mapped[str] = mapped_column(Text, nullable=True)
    type: Mapped[str] = mapped_column(Text)
    date: Mapped[datetime]


class Post(Base):
    __tablename__ = 'posts'

    i_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_sb_object_filial: Mapped[int]
    id_sb_object_zakazchik: Mapped[int]
    id_sb_object_object: Mapped[int]
    id_sb_object_post: Mapped[int] = mapped_column(Integer, nullable=True)
    name_post: Mapped[str] = mapped_column(Text)
    type: Mapped[str] = mapped_column(Text)
    shift_mode: Mapped[str]
    date: Mapped[datetime]


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
    __tablename__ = 'triggering'

    i_id: Mapped[int] = mapped_column(primary_key=True)
    id_sb_object_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_object: Mapped[int] = mapped_column(Integer, nullable=True)
    name_customer: Mapped[str] = mapped_column(Text, nullable=True)
    type: Mapped[str] = mapped_column(Text, nullable=True)
    reason: Mapped[str] = mapped_column(Text, nullable=True)
    place: Mapped[str] = mapped_column(Text, nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    departure_mg: Mapped[bool] = mapped_column(Boolean, nullable=True)
    id_sb_object_mob_group: Mapped[int] = mapped_column(Integer, nullable=True)
    departure_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    arrival_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    description_of_additional_check: Mapped[str] = mapped_column(Text, nullable=True)
    response_time: Mapped[time] = mapped_column(Time, nullable=True)
    mg_moment_of_actuation: Mapped[str] = mapped_column(Text, nullable=True)
    trigger_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class Income(Base):
    __tablename__ = "income"

    i_id: Mapped[int] = mapped_column(primary_key=True)
    id_sb_object_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_zakazchik: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_object: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_dogovor: Mapped[int] = mapped_column(Integer, nullable=True)
    year: Mapped[int] = mapped_column(Integer, nullable=True)
    month: Mapped[str] = mapped_column(Text, nullable=True)
    contract_amount: Mapped[float] = mapped_column(Double, nullable=True)
    add_aggr_amount: Mapped[float] = mapped_column(Double, nullable=True)
    amount_avr: Mapped[float] = mapped_column(Double, nullable=True)
    payment_date_avr: Mapped[Date] = mapped_column(Date, nullable=True)
    actual_amount: Mapped[float] = mapped_column(Double, nullable=True)
    payment_date_actual: Mapped[Date] = mapped_column(Date, nullable=True)
    deviation_amount: Mapped[float] = mapped_column(Double, nullable=True)
    deviation_from_avr: Mapped[float] = mapped_column(Double, nullable=True)


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
    __tablename__ = "journal"

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sb_object_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_zakazchik: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_mob_group: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_post: Mapped[int] = mapped_column(Integer, nullable=True)
    log_of_acceptance: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    finery_journal: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    log_if_incoming: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    import_export_logbook: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    acceptance_log_for_premises_delivery: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    visitor_log: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    vehicle_registration_log: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)


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


class MotorTransport(Base):
    __tablename__ = "motor_transport"

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sb_object_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_zakazchik: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_mob_group: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_post: Mapped[int] = mapped_column(Integer, nullable=True)
    motor_transport: Mapped[int] = mapped_column(Integer, nullable=True)
    additional_sites: Mapped[int] = mapped_column(Integer, nullable=True)
    gps: Mapped[int] = mapped_column(Integer, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)


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


class ProvidingWorkWear(Base):
    __tablename__ = "providing_workwear"

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sb_object_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_zakazchik: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_mob_group: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_post: Mapped[int] = mapped_column(Integer, nullable=True)
    motor_transport: Mapped[int] = mapped_column(Integer, nullable=True)
    gps: Mapped[int] = mapped_column(Integer, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)


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
    __tablename__ = "secutiry_guards"

    i_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_sb_guards: Mapped[int] = mapped_column(Integer)
    object_name: Mapped[str] = mapped_column(Text, nullable=True)
    name: Mapped[str] = mapped_column(Text, nullable=True)
    surname: Mapped[str] = mapped_column(Text, nullable=True)
    job_title: Mapped[str] = mapped_column(Text, nullable=True)
    employee_photo: Mapped[LargeBinary] = mapped_column(LargeBinary, nullable=True)
    gender: Mapped[str] = mapped_column(Text, nullable=True)
    nationality: Mapped[str] = mapped_column(Text, nullable=True)
    customer: Mapped[str] = mapped_column(Text, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    id_sb_object_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_zakazchik: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_object: Mapped[int] = mapped_column(Integer, nullable=True)
    iin: Mapped[str] = mapped_column(Text, nullable=True)
    social_status: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(Text, nullable=True)
    labor_union: Mapped[str] = mapped_column(Text, nullable=True)


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


class TrainingAndMedicalServices(Base):
    __tablename__ = "training_and_medical_services"

    i_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sb_object_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_mob_group: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_zakazchik: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_post: Mapped[int] = mapped_column(Integer, nullable=True)
    annual_retraining_of_security_guards: Mapped[int] = mapped_column(Integer, nullable=True)
    anti_terrorism_training: Mapped[int] = mapped_column(Integer, nullable=True)
    fire_technical_minimum: Mapped[int] = mapped_column(Integer, nullable=True)
    annual_medical_examination: Mapped[int] = mapped_column(Integer, nullable=True)
    pre_shift_medical_examination: Mapped[int] = mapped_column(Integer, nullable=True)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=True)


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
