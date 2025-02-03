from datetime import datetime, time
from numbers import Integral

from sqlalchemy import Integer, DateTime, Float, String, SmallInteger, Numeric, Date, Boolean, Time, Double, \
    LargeBinary, Text, nulls_last, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.superset_database import Base


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
    name: Mapped[str] = mapped_column(String(length=255))
    date: Mapped[datetime]

    objects: Mapped[list['Object']] = relationship(
        back_populates='filial',
        primaryjoin="Filial.id_sm == Object.filial_id_sm",
    )

    posts: Mapped[list["Post"]] = relationship(
        back_populates='filial',
        primaryjoin="Filial.id_sm == Post.filial_id_sm",
    )
    mob_groups: Mapped[list["MobGroup"]] = relationship(
        back_populates='filial',
        primaryjoin="Filial.id_sm == MobGroup.filial_id_sm",
    )
    security_guards: Mapped[list["SecurityGuard"]] = relationship(
        back_populates="filial",
        primaryjoin="Filial.id_sm == SecurityGuard.filial_id_sm",
    )
    income: Mapped[list["Income"]] = relationship(
        back_populates="filial",
        primaryjoin="Filial.id_sm == Income.filial_id_sm",
    )


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)
    name: Mapped[str] = mapped_column(String(length=255))
    bin: Mapped[str] = mapped_column(String(length=255))
    date: Mapped[datetime]

    posts: Mapped[list["Post"]] = relationship(
        back_populates='customer',
        primaryjoin="Customer.id_sm == Post.customer_id_sm",
    )
    objects: Mapped[list["Object"]] = relationship(
        back_populates='customer',
        primaryjoin="Customer.id_sm == Object.customer_id_sm",
    )
    mob_groups: Mapped[list["MobGroup"]] = relationship(
        back_populates='customer',
        primaryjoin="Customer.id_sm == MobGroup.customer_id_sm",
    )
    security_guards: Mapped[list["SecurityGuard"]] = relationship(
        back_populates="customer",
        primaryjoin="Customer.id_sm == SecurityGuard.customer_id_sm",
    )
    income: Mapped[list["Income"]] = relationship(
        back_populates="customer",
        primaryjoin="Customer.id_sm == Income.customer_id_sm",
    )


class Contract(Base):
    __tablename__ = "contract"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)
    name: Mapped[str] = mapped_column(String(length=255), nullable=True)

    object: Mapped[list["Object"]] = relationship(
        back_populates='dogovor',
        primaryjoin="Contract.id_sm == Object.dogovor_id_sm",
    )
    income: Mapped[list["Income"]] = relationship(
        back_populates='contract',
        primaryjoin="Contract.id_sm == Income.contract_id_sm",
    )


class Object(Base):
    __tablename__ = "objects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)

    filial_id_sm: Mapped[int] = mapped_column(ForeignKey("filials.id_sm", ondelete="CASCADE"))
    filial: Mapped["Filial"] = relationship(back_populates="objects")

    customer_id_sm: Mapped[int] = mapped_column(ForeignKey("customers.id_sm", ondelete="CASCADE"))
    customer: Mapped["Customer"] = relationship(back_populates="objects")

    dogovor_id_sm: Mapped[int] = mapped_column(ForeignKey("contract.id_sm", ondelete="CASCADE"), nullable=True)
    dogovor: Mapped["Contract"] = relationship(back_populates="object")

    contract: Mapped[str] = mapped_column(String(length=255), nullable=True)
    name: Mapped[str] = mapped_column(String(length=255))
    contract_date: Mapped[Date] = mapped_column(Date)
    contract_number: Mapped[str] = mapped_column(String(length=255), nullable=True)
    type: Mapped[str] = mapped_column(String(length=255))
    date: Mapped[datetime]

    posts: Mapped[list["Post"]] = relationship(
        back_populates='object',
        primaryjoin="Object.id_sm == Post.object_id_sm",
    )
    mob_groups: Mapped[list["MobGroup"]] = relationship(
        back_populates='object',
        primaryjoin="Object.id_sm == MobGroup.object_id_sm",
    )
    security_guards: Mapped[list["SecurityGuard"]] = relationship(
        back_populates="object",
        primaryjoin="Object.id_sm == SecurityGuard.object_id_sm",
    )
    income: Mapped[list["Income"]] = relationship(
        back_populates="object",
        primaryjoin="Object.id_sm == Income.object_id_sm",
    )


class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)

    filial_id_sm: Mapped[int] = mapped_column(ForeignKey("filials.id_sm", ondelete="CASCADE"))
    filial: Mapped["Filial"] = relationship(back_populates="posts")
    customer_id_sm: Mapped[int] = mapped_column(ForeignKey("customers.id_sm", ondelete="CASCADE"))
    customer: Mapped["Customer"] = relationship(back_populates="posts")
    object_id_sm: Mapped[int] = mapped_column(ForeignKey("objects.id_sm", ondelete="CASCADE"))
    object: Mapped["Object"] = relationship(back_populates="posts")

    name: Mapped[str] = mapped_column(String(length=255))
    type: Mapped[str] = mapped_column(String(length=255))
    shift_mode: Mapped[int]
    date: Mapped[datetime]


class MobGroup(Base):
    __tablename__ = "mob_groups"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_sm: Mapped[int] = mapped_column(Integer, unique=True)

    filial_id_sm: Mapped[int] = mapped_column(ForeignKey("filials.id_sm", ondelete="CASCADE"))
    filial: Mapped["Filial"] = relationship(back_populates="mob_groups")
    customer_id_sm: Mapped[int] = mapped_column(ForeignKey("customers.id_sm", ondelete="CASCADE"))
    customer: Mapped["Customer"] = relationship(back_populates="mob_groups")
    object_id_sm: Mapped[int] = mapped_column(ForeignKey("objects.id_sm", ondelete="CASCADE"))
    object: Mapped["Object"] = relationship(back_populates="mob_groups")

    name: Mapped[str] = mapped_column(String(length=255))
    operating_mode: Mapped[str] = mapped_column(String(length=255))
    linear_part: Mapped[str] = mapped_column(Text)
    length_from: Mapped[float] = mapped_column(Double)
    length_to: Mapped[float] = mapped_column(Double)
    date: Mapped[datetime]


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
    date: Mapped[datetime]


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
    
    contract_id_sm: Mapped[int] = mapped_column(ForeignKey("contract.id_sm", ondelete="NO ACTION"), nullable=True)
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
    comment: Mapped[str] = mapped_column(String(length=255), nullable=True)
    additional_comment: Mapped[str] = mapped_column(String(length=255), nullable=True)
    date: Mapped[datetime]
