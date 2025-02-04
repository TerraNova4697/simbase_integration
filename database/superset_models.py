from datetime import datetime, time, date
from numbers import Integral

from sqlalchemy import Integer, DateTime, Float, String, SmallInteger, Numeric, Date, Boolean, text, Double, \
    LargeBinary, Text, nulls_last, ForeignKey, JSON, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Annotated

from database.superset_database import Base


# updated_at = Annotated[datetime, mapped_column(
#         server_default=text("TIMEZONE('utc', now())"),
#         onupdate=datetime.datetime.utcnow,
#     )]

vc255 = Annotated[str, mapped_column(String(length=255), nullable=True)]
boolnull = Annotated[bool, mapped_column(Boolean, nullable=True)]


class FetchedDates(Base):
    __tablename__ = "fetched_dates"

    date_created: Mapped[Date] = mapped_column(Date, primary_key=True)


class SqlError(Base):
    __tablename__ = 'sql_errors'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    exception: Mapped[str] = mapped_column(String(length=8191))
    traceback: Mapped[str] = mapped_column(String(length=8191))
    sql: Mapped[str] = mapped_column(String(length=511))
    target_model: Mapped[str] = mapped_column(String(length=127))
    source_object: Mapped[dict] = mapped_column(JSON)


class Filial(Base):
    __tablename__ = "filials"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)
    name: Mapped[str] = mapped_column(String(length=255), nullable=True)
    longitude: Mapped[float] = mapped_column(Double, nullable=True)
    latitude: Mapped[float] = mapped_column(Double, nullable=True)
    date_modified: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    objects: Mapped[list['Object']] = relationship(
        back_populates='filial',
        primaryjoin="Filial.id_sm == Object.filial_id_sm",
    )

    posts: Mapped[list["Post"]] = relationship(
        back_populates='filial',
        primaryjoin="Filial.id_sm == Post.filial_id_sm",
    )
    # mob_groups: Mapped[list["MobGroup"]] = relationship(
    #     back_populates='filial',
    #     primaryjoin="Filial.id_sm == MobGroup.filial_id_sm",
    # )
    security_guards: Mapped[list["SecurityGuard"]] = relationship(
        back_populates="filial",
        primaryjoin="Filial.id_sm == SecurityGuard.filial_id_sm",
    )
    income: Mapped[list["Income"]] = relationship(
        back_populates="filial",
        primaryjoin="Filial.id_sm == Income.filial_id_sm",
    )
    employees: Mapped[list["Employee"]] = relationship(
        back_populates="filial",
        primaryjoin="Filial.id_sm == Employee.filial_id_sm",
    )
    fines: Mapped[list["Fine"]] = relationship(
        back_populates="filial",
        primaryjoin="Filial.id_sm == fines.filial_id_sm",
    )
    triggerings: Mapped[list["Triggering"]] = relationship(
        back_populates="filial",
        primaryjoin="Filial.id_sm == Triggering.filial_id_sm",
    )
    incidents: Mapped[list["Incident"]] = relationship(
        back_populates="filial",
        primaryjoin="Filial.id_sm == Incident.filial_id_sm",
    )
    shifts: Mapped[list["Shift"]] = relationship(
        back_populates="filial",
        primaryjoin="Filial.id_sm == Shift.filial_id_sm",
    )
    training_and_medical_services: Mapped[list["TrainingAndMedicalService"]] = relationship(
        back_populates="filial",
        primaryjoin="Filial.id_sm == TrainingAndMedicalService.filial_id_sm",
    )
    transports: Mapped[list["Transport"]] = relationship(
        back_populates="filial",
        primaryjoin="Filial.id_sm == Transport.filial_id_sm",
    )
    journals: Mapped[list["Journal"]] = relationship(
        back_populates="filial",
        primaryjoin="Filial.id_sm == Journal.filial_id_sm",
    )
    providing_workwears: Mapped[list["ProvidingWorkwears"]] = relationship(
        back_populates="filial",
        primaryjoin="Filial.id_sm == ProvidingWorkwears.filial_id_sm",
    )
    communication_facilities: Mapped[list["CommunicationFacilitiy"]] = relationship(
        back_populates="filial",
        primaryjoin="Filial.id_sm == CommunicationFacilitiy.filial_id_sm",
    )
    weapons_and_special_equipments: Mapped[list["WeaponAndSpecEquipment"]] = relationship(
        back_populates="filial",
        primaryjoin="Filial.id_sm == WeaponAndSpecEquipment.filial_id_sm",
    )


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)
    name: Mapped[str] = mapped_column(String(length=255), nullable=True)
    bin: Mapped[str] = mapped_column(String(length=255), nullable=True)
    status: Mapped[str] = mapped_column(String(length=255), nullable=True)
    date_modified: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    posts: Mapped[list["Post"]] = relationship(
        back_populates='customer',
        primaryjoin="Customer.id_sm == Post.customer_id_sm",
    )
    objects: Mapped[list["Object"]] = relationship(
        back_populates='customer',
        primaryjoin="Customer.id_sm == Object.customer_id_sm",
    )
    # mob_groups: Mapped[list["MobGroup"]] = relationship(
    #     back_populates='customer',
    #     primaryjoin="Customer.id_sm == MobGroup.customer_id_sm",
    # )
    security_guards: Mapped[list["SecurityGuard"]] = relationship(
        back_populates="customer",
        primaryjoin="Customer.id_sm == SecurityGuard.customer_id_sm",
    )
    income: Mapped[list["Income"]] = relationship(
        back_populates="customer",
        primaryjoin="Customer.id_sm == Income.customer_id_sm",
    )
    fines: Mapped[list["Fine"]] = relationship(
        back_populates="customer",
        primaryjoin="Customer.id_sm == Fine.customer_id_sm",
    )
    training_and_medical_services: Mapped[list["TrainingAndMedicalService"]] = relationship(
        back_populates="customer",
        primaryjoin="Customer.id_sm == TrainingAndMedicalService.customer_id_sm",
    )
    transports: Mapped[list["Transport"]] = relationship(
        back_populates="customer",
        primaryjoin="Customer.id_sm == Transport.customer_id_sm",
    )
    journals: Mapped[list["Journal"]] = relationship(
        back_populates="customer",
        primaryjoin="Customer.id_sm == Journal.customer_id_sm",
    )
    providing_workwears: Mapped[list["ProvidingWorkwears"]] = relationship(
        back_populates="customer",
        primaryjoin="Customer.id_sm == ProvidingWorkwears.customer_id_sm",
    )
    communication_facilities: Mapped[list["CommunicationFacilitiy"]] = relationship(
        back_populates="customer",
        primaryjoin="Customer.id_sm == CommunicationFacilitiy.customer_id_sm",
    )
    weapons_and_special_equipments: Mapped[list["WeaponAndSpecEquipment"]] = relationship(
        back_populates="customer",
        primaryjoin="Customer.id_sm == WeaponAndSpecEquipment.customer_id_sm",
    )


class Contract(Base):
    __tablename__ = "contracts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)
    name: Mapped[str] = mapped_column(String(length=255), nullable=True)
    date_modified: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    object: Mapped[list["Object"]] = relationship(
        back_populates='dogovor',
        primaryjoin="Contract.id_sm == Object.contract_id_sm",
    )
    income: Mapped[list["Income"]] = relationship(
        back_populates='contract',
        primaryjoin="Contract.id_sm == Income.contract_id_sm",
    )


class Object(Base):
    __tablename__ = "objects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)

    filial_id_sm: Mapped[int] = mapped_column(ForeignKey("filials.id_sm", ondelete="CASCADE"), nullable=True)
    filial: Mapped["Filial"] = relationship(back_populates="objects")

    customer_id_sm: Mapped[int] = mapped_column(ForeignKey("customers.id_sm", ondelete="CASCADE"), nullable=True)
    customer: Mapped["Customer"] = relationship(back_populates="objects")

    contract_id_sm: Mapped[int] = mapped_column(ForeignKey("contracts.id_sm", ondelete="CASCADE"), nullable=True)
    contract: Mapped["Contract"] = relationship(back_populates="object")

    contract: Mapped[str] = mapped_column(String(length=255), nullable=True)
    name: Mapped[str] = mapped_column(String(length=255), nullable=True)
    contract_date: Mapped[Date] = mapped_column(Date, nullable=True)
    contract_number: Mapped[str] = mapped_column(String(length=255), nullable=True)
    type: Mapped[str] = mapped_column(String(length=255), nullable=True)
    date_modified: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    posts: Mapped[list["Post"]] = relationship(
        back_populates='object',
        primaryjoin="Object.id_sm == Post.object_id_sm",
    )
    # mob_groups: Mapped[list["MobGroup"]] = relationship(
    #     back_populates='object',
    #     primaryjoin="Object.id_sm == MobGroup.object_id_sm",
    # )
    security_guards: Mapped[list["SecurityGuard"]] = relationship(
        back_populates="object",
        primaryjoin="Object.id_sm == SecurityGuard.object_id_sm",
    )
    income: Mapped[list["Income"]] = relationship(
        back_populates="object",
        primaryjoin="Object.id_sm == Income.object_id_sm",
    )
    triggerings: Mapped[list["Triggering"]] = relationship(
        back_populates="object",
        primaryjoin="Object.id_sm == Triggering.object_id_sm",
    )
    shifts: Mapped[list["Shift"]] = relationship(
        back_populates="object",
        primaryjoin="Object.id_sm == Shift.object_id_sm",
    )


class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)

    filial_id_sm: Mapped[int] = mapped_column(ForeignKey("filials.id_sm", ondelete="CASCADE"), nullable=True)
    filial: Mapped["Filial"] = relationship(back_populates="posts")
    customer_id_sm: Mapped[int] = mapped_column(ForeignKey("customers.id_sm", ondelete="CASCADE"), nullable=True)
    customer: Mapped["Customer"] = relationship(back_populates="posts")
    object_id_sm: Mapped[int] = mapped_column(ForeignKey("objects.id_sm", ondelete="CASCADE"), nullable=True)
    object: Mapped["Object"] = relationship(back_populates="posts")

    name: Mapped[str] = mapped_column(String(length=255), nullable=True)
    type: Mapped[str] = mapped_column(String(length=255), nullable=True)
    shift_mode: Mapped[int] = mapped_column(Integer, nullable=True)
    operation_mode: Mapped[int] = mapped_column(Integer, nullable=True)
    linear_part: Mapped[str] = mapped_column(Text, nullable=True)
    length_from: Mapped[float] = mapped_column(Double, nullable=True)
    length_to: Mapped[float] = mapped_column(Double, nullable=True)
    date_modified: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    triggerings: Mapped[list["Triggering"]] = relationship(
        back_populates="post",
        primaryjoin="Post.id_sm == Triggering.post_id_sm",
    )
    shifts: Mapped[list["Shift"]] = relationship(
        back_populates="post",
        primaryjoin="Post.id_sm == Shift.post_id_sm",
    )
    training_and_medical_services: Mapped[list["TrainingAndMedicalService"]] = relationship(
        back_populates="post",
        primaryjoin="Post.id_sm == TrainingAndMedicalService.post_id_sm",
    )
    transports: Mapped[list["Transport"]] = relationship(
        back_populates="post",
        primaryjoin="Post.id_sm == Transport.post_id_sm",
    )
    journals: Mapped[list["Journal"]] = relationship(
        back_populates="post",
        primaryjoin="Post.id_sm == Journal.post_id_sm",
    )
    providing_workwears: Mapped[list["ProvidingWorkwears"]] = relationship(
        back_populates="post",
        primaryjoin="Post.id_sm == ProvidingWorkwears.post_id_sm",
    )
    communication_facilities: Mapped[list["CommunicationFacilitiy"]] = relationship(
        back_populates="post",
        primaryjoin="Post.id_sm == CommunicationFacilitiy.post_id_sm",
    )
    weapons_and_special_equipments: Mapped[list["WeaponAndSpecEquipment"]] = relationship(
        back_populates="post",
        primaryjoin="Post.id_sm == WeaponAndSpecEquipment.post_id_sm",
    )


# class MobGroup(Base):
#     __tablename__ = "mob_groups"

#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     id_sm: Mapped[int] = mapped_column(Integer, unique=True)

#     filial_id_sm: Mapped[int] = mapped_column(ForeignKey("filials.id_sm", ondelete="CASCADE"))
#     filial: Mapped["Filial"] = relationship(back_populates="mob_groups")
#     customer_id_sm: Mapped[int] = mapped_column(ForeignKey("customers.id_sm", ondelete="CASCADE"))
#     customer: Mapped["Customer"] = relationship(back_populates="mob_groups")
#     object_id_sm: Mapped[int] = mapped_column(ForeignKey("objects.id_sm", ondelete="CASCADE"))
#     object: Mapped["Object"] = relationship(back_populates="mob_groups")

#     name: Mapped[str] = mapped_column(String(length=255))
#     operating_mode: Mapped[str] = mapped_column(String(length=255))
#     linear_part: Mapped[str] = mapped_column(Text)
#     length_from: Mapped[float] = mapped_column(Double)
#     length_to: Mapped[float] = mapped_column(Double)
#     date: Mapped[datetime]


class SecurityGuard(Base):
    __tablename__ = "security_guards"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)

    filial_id_sm: Mapped[int] = mapped_column(ForeignKey("filials.id_sm", ondelete="CASCADE"), nullable=True)
    filial: Mapped["Filial"] = relationship(back_populates="security_guards")
    customer_id_sm: Mapped[int] = mapped_column(ForeignKey("customers.id_sm", ondelete="CASCADE"), nullable=True)
    customer: Mapped["Customer"] = relationship(back_populates="security_guards")
    object_id_sm: Mapped[int] = mapped_column(ForeignKey("objects.id_sm", ondelete="CASCADE"), nullable=True)
    object: Mapped["Object"] = relationship(back_populates="security_guards")

    name: Mapped[str] = mapped_column(String(length=255), nullable=True)
    surname: Mapped[str] = mapped_column(String(length=255), nullable=True)
    iin: Mapped[str] = mapped_column(String(length=255), nullable=True)
    social_status: Mapped[str] = mapped_column(String(length=255), nullable=True)
    status: Mapped[str] = mapped_column(String(length=255), nullable=True)
    job_title: Mapped[str] = mapped_column(String(length=255), nullable=True)
    employee_photo: Mapped[LargeBinary] = mapped_column(LargeBinary, nullable=True)
    gender: Mapped[str] = mapped_column(String(length=255), nullable=True)
    nationality: Mapped[str] = mapped_column(String(length=255), nullable=True)
    labor_union: Mapped[str] = mapped_column(String(length=255), nullable=True)
    date_modified: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    shifts: Mapped[list["Shift"]] = relationship(
        back_populates="security_guard",
        primaryjoin="SecurityGuard.id_sm == Shift.security_guard_id_sm",
    )
    shifts_replaced: Mapped[list["Shift"]] = relationship(
        back_populates="security_guard_replaced",
        primaryjoin="SecurityGuard.id_sm == Shift.security_guard_replaced_id_sm",
    )


class Income(Base):
    __tablename__ = "income"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)

    filial_id_sm: Mapped[int] = mapped_column(ForeignKey("filials.id_sm", ondelete="NO ACTION"), nullable=True)
    filial: Mapped["Filial"] = relationship(back_populates="income")

    customer_id_sm: Mapped[int] = mapped_column(ForeignKey("customers.id_sm", ondelete="NO ACTION"), nullable=True)
    customer: Mapped["Customer"] = relationship(back_populates="income")
    
    object_id_sm: Mapped[int] = mapped_column(ForeignKey("objects.id_sm", ondelete="NO ACTION"), nullable=True)
    object: Mapped["Object"] = relationship(back_populates="income")
    
    contract_id_sm: Mapped[int] = mapped_column(ForeignKey("contracts.id_sm", ondelete="NO ACTION"), nullable=True)
    contract: Mapped["Contract"] = relationship(back_populates="income")
    
    type: Mapped[str] = mapped_column(String(length=255), nullable=True)
    status: Mapped[str] = mapped_column(String(length=255), nullable=True)
    year: Mapped[int] = mapped_column(Integer, nullable=True)
    month: Mapped[str] = mapped_column(String(length=255), nullable=True)
    contract_amount: Mapped[float] = mapped_column(Double, nullable=True)
    additional_agreement_amount: Mapped[float] = mapped_column(Double, nullable=True)
    amount_avr: Mapped[float] = mapped_column(Double, nullable=True)
    payment_date_avr: Mapped[Date] = mapped_column(Date, nullable=True)
    actual_payment: Mapped[float] = mapped_column(Double, nullable=True)
    payment_date_actual: Mapped[Date] = mapped_column(Date, nullable=True)
    deviation_amount: Mapped[float] = mapped_column(Double, nullable=True)
    deviation_from_avr: Mapped[float] = mapped_column(Double, nullable=True)
    deviation_from_contract_prc: Mapped[str] = mapped_column(String(length=255), nullable=True)
    deviation_from_avr_prc: Mapped[str] = mapped_column(String(length=255), nullable=True)
    remainder: Mapped[float] = mapped_column(Double, nullable=True)
    comment: Mapped[str] = mapped_column(String(length=1023), nullable=True)
    additional_comment: Mapped[str] = mapped_column(String(length=1023), nullable=True)
    date_modified: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class Employee(Base):
    __tablename__ = 'employee'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)
    employee: Mapped[vc255]
    name: Mapped[vc255]
    second_name: Mapped[vc255]
    middle_name: Mapped[vc255]
    
    filial_id_sm: Mapped[int] = mapped_column(ForeignKey("filials.id_sm", ondelete="NO ACTION"), nullable=True)
    filial: Mapped["Filial"] = relationship(back_populates="employees")

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
    reserved: Mapped[boolnull]
    labor_union: Mapped[vc255]
    nomenclature_CEO: Mapped[boolnull]
    nomenclature_CA: Mapped[boolnull]
    retiree: Mapped[boolnull]
    member_collective_agreement: Mapped[boolnull]
    wage_rate: Mapped[boolnull]
    salary: Mapped[boolnull]
    rating: Mapped[boolnull]
    date_modified: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    legal_claims: Mapped[list["LegalClaims"]] = relationship(
        back_populates="responsible_employee",
        primaryjoin="Employee.id_sm == LegalClaims.responsible_employee_id_sm",
    )


class ContractTRU(Base):
    __tablename__ = 'contract_TRU'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)
    name: Mapped[vc255]
    date_modified: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    legal_claims: Mapped[list["LegalClaims"]] = relationship(
        back_populates="contract_TRU",
        primaryjoin="ContractTRU.id_sm == LegalClaims.contract_TRU_id_sm",
    )


class LegalClaims(Base):
    __tablename__ = 'legal_claims'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)
    
    responsible_employee_id_sm: Mapped[int] = mapped_column(ForeignKey("employee.id_sm", ondelete="NO ACTION"), nullable=True)
    responsible_employee: Mapped["Employee"] = relationship(back_populates="legal_claims")

    contract_TRU_id_sm: Mapped[int] = mapped_column(ForeignKey("contract_TRU.id_sm", ondelete="NO ACTION"), nullable=True)
    contract_TRU: Mapped['ContractTRU'] = relationship(back_populates="legal_claims")

    conclusion_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    contract_number: Mapped[vc255]
    applicant: Mapped[vc255]
    defendant: Mapped[vc255]
    case_classification: Mapped[vc255]
    property_requirements: Mapped[vc255]
    currency: Mapped[vc255]
    non_property_claims: Mapped[vc255]
    grounds_of_claim: Mapped[vc255]
    result: Mapped[vc255]
    dishonest_supplier: Mapped[boolnull]
    date_modified: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class Fine(Base):
    __tablename__ = "fines"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)

    filial_id_sm: Mapped[int] = mapped_column(ForeignKey("filials.id_sm", ondelete="NO ACTION"), nullable=True)
    filial: Mapped["Filial"] = relationship(back_populates="fines")
    customer_id_sm: Mapped[int] = mapped_column(ForeignKey("customers.id_sm", ondelete="CASCADE"), nullable=True)
    customer: Mapped["Customer"] = relationship(back_populates="fines")

    circumstances: Mapped[str] = mapped_column(Text, nullable=True)
    violation_type: Mapped[vc255]
    fine_type: Mapped[vc255]
    request_amount: Mapped[float] = mapped_column(Double, nullable=True)
    recognition_amount: Mapped[float] = mapped_column(Double, nullable=True)
    fine_number: Mapped[vc255]
    fine_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    decision: Mapped[vc255]
    date_modified: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class Triggering(Base):
    __tablename__ = "triggerings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)

    filial_id_sm: Mapped[int] = mapped_column(ForeignKey("filials.id_sm", ondelete="NO ACTION"), nullable=True)
    filial: Mapped["Filial"] = relationship(back_populates="triggerings")
    object_id_sm: Mapped[int] = mapped_column(ForeignKey("objects.id_sm", ondelete="NO ACTION"), nullable=True)
    object: Mapped["Object"] = relationship(back_populates="triggerings")
    post_id_sm: Mapped[int] = mapped_column(ForeignKey("posts.id_sm", ondelete="NO ACTION"), nullable=True)
    post: Mapped["Post"] = relationship(back_populates="triggerings")

    type: Mapped[vc255]
    customer: Mapped[vc255]
    reason: Mapped[vc255]
    description: Mapped[vc255]
    place: Mapped[vc255]
    departure_mg: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    departure_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    arrival_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    response_time: Mapped[time] = mapped_column(Time, nullable=True)
    mg_moment_of_actuation: Mapped[vc255]
    trigger_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_modified: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class Incident(Base):
    __tablename__ = "incidents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)

    filial_id_sm: Mapped[int] = mapped_column(ForeignKey("filials.id_sm", ondelete="NO ACTION"), nullable=True)
    filial: Mapped["Filial"] = relationship(back_populates="incidents")

    type: Mapped[vc255]
    subtype: Mapped[vc255]
    data_on_the_transfer_of_relations_ap: Mapped[vc255]
    the_case_has_been_transferred_to_the_police: Mapped[boolnull]
    the_act_was_submitted_to_the_Security_Council: Mapped[boolnull]
    customers_employees: Mapped[boolnull]
    KMGSecurity_employees: Mapped[boolnull]
    contractor_employees: Mapped[boolnull]
    commit_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    time: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    customer: Mapped[vc255]
    amount_of_damage: Mapped[vc255]
    full_name: Mapped[vc255]
    KMGS_LTD: Mapped[vc255]
    third_party: Mapped[vc255]
    disciplinary: Mapped[vc255]
    KUI: Mapped[vc255]
    ERDR: Mapped[vc255]
    SB: Mapped[vc255]
    status: Mapped[vc255]
    date_modified: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class Shift(Base):
    __tablename__ = "shifts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)

    filial_id_sm: Mapped[int] = mapped_column(ForeignKey("filials.id_sm", ondelete="NO ACTION"), nullable=True)
    filial: Mapped["Filial"] = relationship(back_populates="shifts")
    object_id_sm: Mapped[int] = mapped_column(ForeignKey("objects.id_sm", ondelete="NO ACTION"), nullable=True)
    object: Mapped["Object"] = relationship(back_populates="shifts")
    post_id_sm: Mapped[int] = mapped_column(ForeignKey("posts.id_sm", ondelete="NO ACTION"), nullable=True)
    post: Mapped["Post"] = relationship(back_populates="shifts")
    security_guard_id_sm: Mapped[int] = mapped_column(ForeignKey("security_guards.id_sm", ondelete="NO ACTION"), nullable=True)
    security_guard: Mapped["Post"] = relationship(back_populates="shifts")
    security_guard_replaces_id_sm: Mapped[int] = mapped_column(ForeignKey("security_guards.id_sm", ondelete="NO ACTION"), nullable=True)
    security_guard_replaces: Mapped["Post"] = relationship(back_populates="shifts_replaced")

    joined_posts: Mapped[boolnull]
    shift_date: Mapped[date] = mapped_column(Date, nullable=True)
    shift_type: Mapped[vc255]
    date_modified: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class TrainingAndMedicalService(Base):
    __tablename__ = 'training_and_medical_services'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)

    filial_id_sm: Mapped[int] = mapped_column(ForeignKey("filials.id_sm", ondelete="NO ACTION"), nullable=True)
    filial: Mapped["Filial"] = relationship(back_populates="training_and_medical_services")
    customer_id_sm: Mapped[int] = mapped_column(ForeignKey("customers.id_sm", ondelete="CASCADE"), nullable=True)
    customer: Mapped["Customer"] = relationship(back_populates="training_and_medical_services")
    post_id_sm: Mapped[int] = mapped_column(ForeignKey("posts.id_sm", ondelete="NO ACTION"), nullable=True)
    post: Mapped["Post"] = relationship(back_populates="training_and_medical_services")

    annual_retraining_of_security_guards_quant: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    anti_terrorism_training_quant: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    fire_technical_minimum_quant: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    annual_medical_examination_quant: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    pre_shift_medical_examination_quant: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    date_modified: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class Transport(Base):
    __tablename__ = "transports"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)

    filial_id_sm: Mapped[int] = mapped_column(ForeignKey("filials.id_sm", ondelete="NO ACTION"), nullable=True)
    filial: Mapped["Filial"] = relationship(back_populates="transports")
    customer_id_sm: Mapped[int] = mapped_column(ForeignKey("customers.id_sm", ondelete="CASCADE"), nullable=True)
    customer: Mapped["Customer"] = relationship(back_populates="transports")
    post_id_sm: Mapped[int] = mapped_column(ForeignKey("posts.id_sm", ondelete="NO ACTION"), nullable=True)
    post: Mapped["Post"] = relationship(back_populates="transports")

    transport_quant: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    additional_necessary_transport_quant: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    GPS: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    date_modified: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class Journal(Base):
    __tablename__ = "journals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)

    filial_id_sm: Mapped[int] = mapped_column(ForeignKey("filials.id_sm", ondelete="NO ACTION"), nullable=True)
    filial: Mapped["Filial"] = relationship(back_populates="journals")
    customer_id_sm: Mapped[int] = mapped_column(ForeignKey("customers.id_sm", ondelete="CASCADE"), nullable=True)
    customer: Mapped["Customer"] = relationship(back_populates="journals")
    post_id_sm: Mapped[int] = mapped_column(ForeignKey("posts.id_sm", ondelete="NO ACTION"), nullable=True)
    post: Mapped["Post"] = relationship(back_populates="journals")

    log_of_accept_and_transf_of_weapon_and_ammunition: Mapped[boolnull]
    finery_journal: Mapped[boolnull]
    log_of_inc_info_and_recor_of_activation_of_tech_sec_means: Mapped[boolnull]
    import_export_log_and_contrib_removals_of_inventory_items: Mapped[boolnull]
    acceptance_log_for_premises_delivery: Mapped[boolnull]
    visitor_log: Mapped[boolnull]
    vehicle_registration_log: Mapped[boolnull]
    date_modified: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class ProvidingWorkwears(Base):
    __tablename__ = "providing_workwears"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)

    filial_id_sm: Mapped[int] = mapped_column(ForeignKey("filials.id_sm", ondelete="NO ACTION"), nullable=True)
    filial: Mapped["Filial"] = relationship(back_populates="providing_workwears")
    customer_id_sm: Mapped[int] = mapped_column(ForeignKey("customers.id_sm", ondelete="CASCADE"), nullable=True)
    customer: Mapped["Customer"] = relationship(back_populates="providing_workwears")
    post_id_sm: Mapped[int] = mapped_column(ForeignKey("posts.id_sm", ondelete="NO ACTION"), nullable=True)
    post: Mapped["Post"] = relationship(back_populates="providing_workwears")

    summer_set: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    winter_set: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    reflective_vets: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    summer_shoes: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    winter_shoes: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    date_modified: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class CommunicationFacilitiy(Base):
    __tablename__ = "communication_facilities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)

    filial_id_sm: Mapped[int] = mapped_column(ForeignKey("filials.id_sm", ondelete="NO ACTION"), nullable=True)
    filial: Mapped["Filial"] = relationship(back_populates="communication_facilities")
    customer_id_sm: Mapped[int] = mapped_column(ForeignKey("customers.id_sm", ondelete="CASCADE"), nullable=True)
    customer: Mapped["Customer"] = relationship(back_populates="communication_facilities")
    post_id_sm: Mapped[int] = mapped_column(ForeignKey("posts.id_sm", ondelete="NO ACTION"), nullable=True)
    post: Mapped["Post"] = relationship(back_populates="communication_facilities")

    wearable_radios_quant: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    сar_radios_quant: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    stationary_radios_quant: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    date_modified: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class WeaponAndSpecEquipment(Base):
    __tablename__ = "weapons_and_special_equipments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)

    filial_id_sm: Mapped[int] = mapped_column(ForeignKey("filials.id_sm", ondelete="NO ACTION"), nullable=True)
    filial: Mapped["Filial"] = relationship(back_populates="weapons_and_special_equipments")
    customer_id_sm: Mapped[int] = mapped_column(ForeignKey("customers.id_sm", ondelete="CASCADE"), nullable=True)
    customer: Mapped["Customer"] = relationship(back_populates="weapons_and_special_equipments")
    post_id_sm: Mapped[int] = mapped_column(ForeignKey("posts.id_sm", ondelete="NO ACTION"), nullable=True)
    post: Mapped["Post"] = relationship(back_populates="weapons_and_special_equipments")

    firearms: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    handcuffs: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    PR73: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    regulatory: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    electric_lantern: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    headlight_finder: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    inspection_mirror: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    detectors_and_metal_detectors: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    binoculars: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    safe_for_storing_weapons: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    wearable_video_recorders: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    car_DVRs: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    cell_phones: Mapped[int] = mapped_column(SmallInteger, nullable=True)
    date_modified: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, nullable=True)
