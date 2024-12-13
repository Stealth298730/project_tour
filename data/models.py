from sqlalchemy import String ,ForeignKey
from sqlalchemy.orm import Mapped ,mapped_column,relationship
from data.base import Base

class Tour(Base):
    __tablename__ = "tours"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(100))
    departure: Mapped[str] = mapped_column(String(50))
    picture: Mapped[str] = mapped_column(String(1000))
    price: Mapped[int] = mapped_column()
    stars: Mapped[str] = mapped_column(String(10))
    country: Mapped[str] = mapped_column(String(100))
    nights: Mapped[int] = mapped_column()
    date: Mapped[str] = mapped_column(String(100))

class Reserve(Base):
    __tablename__ = "reserve"
    id:Mapped[int] = mapped_column(primary_key=True)
    full_name:Mapped[str] = mapped_column(String(100))
    tour_id:Mapped[int] = mapped_column(ForeignKey(Tour.id))
    tour:Mapped[Tour] = relationship()