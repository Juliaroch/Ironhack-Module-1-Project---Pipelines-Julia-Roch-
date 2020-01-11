#Acquisition.py
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy import create_engine

def acquire():
    sqlitedb_path = '../data/raw/juliarochflores.db'
    engine = create_engine(f'sqlite:///{sqlitedb_path}')
    return engine