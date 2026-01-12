#models.py

from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)

    receipts = relationship("Receipt", back_populates="user")

class Receipt(Base):
    __tablename__ = 'receipts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    store_name = Column(String)
    purchase_date = Column(DateTime)
    total_amount = Column(Float)
    raw_text = Column(String)
    receipt_data = Column(JSON)
    created_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="receipts")
    items = relationship("ReceiptItem", back_populates="receipt")

class ReceiptItem(Base):
    __tablename__ = 'receipt_items'
    id = Column(Integer, primary_key=True)
    receipt_id = Column(Integer, ForeignKey('receipts.id'))
    name = Column(String)
    quantity = Column(Float)
    unit = Column(String)
    price_per_unit = Column(Float)
    total_price = Column(Float)
    category = Column(String, nullable=True)

    receipt = relationship("Receipt", back_populates="items")
