from datetime import datetime, date, time

from sqlalchemy import Integer, DateTime, Float, String, SmallInteger, Numeric, Date, Boolean, Time
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class Filial(Base):
    __tablename__ = "filial"

    i_id: Mapped[int] = mapped_column(primary_key=True)
    s_name_filial: Mapped[str] = mapped_column(String(length=512), nullable=True)
    id_sb_object_filial: Mapped[int] = mapped_column(nullable=True) # TODO: will be foreign key
    d_date: Mapped[datetime] = mapped_column(nullable=True)


class Customer(Base):
    __tablename__ = "customers"

    i_id: Mapped[int] = mapped_column(primary_key=True)
    s_name: Mapped[str] = mapped_column(String(length=512), nullable=True)
    id_sb_object_zakazchik: Mapped[int] = mapped_column(Integer, nullable=True) # TODO:
    s_bin: Mapped[str] = mapped_column(String(length=512), nullable=True)
    d_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class Object(Base):
    __tablename__ = 'objects'

    i_id: Mapped[int] = mapped_column(primary_key=True)
    id_sb_object_filial: Mapped[int] = mapped_column(Integer, nullable=True)# TODO:
    id_sb_object_zakazchik: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_object: Mapped[int] = mapped_column(Integer, nullable=True)# TODO:
    object_name: Mapped[str] = mapped_column(String(length=512), nullable=True)
    dogovor: Mapped[str] = mapped_column(String(length=512), nullable=True)
    sb_id_dogovor: Mapped[int] = mapped_column(Integer, nullable=True)
    dogovor_date: Mapped[date] = mapped_column(Date, nullable=True)
    dogovor_num: Mapped[str] = mapped_column(String(length=512), nullable=True)
    object_type: Mapped[str] = mapped_column(String(length=512), nullable=True)
    d_date: Mapped[date] = mapped_column(Date, nullable=True)


class Post(Base):
    __tablename__ = 'posts'

    i_id: Mapped[int] = mapped_column(primary_key=True)
    id_sb_object_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_zakazchik: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_object: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_post: Mapped[int] = mapped_column(Integer, nullable=True)
    post_name: Mapped[str] = mapped_column(String(length=512), nullable=True)
    post_type: Mapped[str] = mapped_column(String(length=512), nullable=True)
    shift_mode: Mapped[str] = mapped_column(String(length=512), nullable=True)
    d_date: Mapped[date] = mapped_column(Date, nullable=True)


class MobileGroup(Base):
    __tablename__ = "mobile_groups"

    i_id: Mapped[int] = mapped_column(primary_key=True)
    id_sb_object_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_zakazchik: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_object: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_mob_group: Mapped[int] = mapped_column(Integer, nullable=True)
    mg_name: Mapped[str] = mapped_column(String(length=512), nullable=True)
    work_mode: Mapped[str] = mapped_column(String(length=512), nullable=True)
    shift_mode: Mapped[str] = mapped_column(String(length=512), nullable=True)
    linear_part: Mapped[str] = mapped_column(String(length=512), nullable=True)
    length_from: Mapped[str] = mapped_column(String(length=512), nullable=True)
    length_to: Mapped[str] = mapped_column(String(length=512), nullable=True)
    d_date: Mapped[date] = mapped_column(Date, nullable=True)


class Triggering(Base):
    __tablename__ = 'triggering'

    i_id: Mapped[int] = mapped_column(primary_key=True)
    id_sb_object_filial: Mapped[int] = mapped_column(Integer, nullable=True)
    id_sb_object_object: Mapped[int] = mapped_column(Integer, nullable=True)
    name_customer: Mapped[str] = mapped_column(String(length=512), nullable=True)
    type: Mapped[str] = mapped_column(String(length=512), nullable=True)
    reason: Mapped[str] = mapped_column(String(length=512), nullable=True)
    place: Mapped[str] = mapped_column(String(length=512), nullable=True)
    description: Mapped[str] = mapped_column(String(length=512), nullable=True)
    departure_mg: Mapped[bool] = mapped_column(Boolean, nullable=True)
    id_sb_object_mob_group: Mapped[int] = mapped_column(Integer, nullable=True)
    departure_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    arrival_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    description_of_additional_check: Mapped[str] = mapped_column(String(length=512), nullable=True)
    response_time: Mapped[time] = mapped_column(Time, nullable=True)
    mg_moment_of_actuation: Mapped[str] = mapped_column(String(length=512), nullable=True)
    trigger_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
