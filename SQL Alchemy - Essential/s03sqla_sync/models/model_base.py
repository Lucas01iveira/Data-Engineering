# from sqlalchemy.ext.declarative import declarative_base # sqlalchemy version 1.4.31 (abaixo de 2.0)
from sqlalchemy.orm import declarative_base

ModelBase = declarative_base() # MetaClasse (a class that create other classes, which in particular are going to generate objects) responsável por geral os schemas das tabelas do banco de dados com o qual estaremos conectando;
#print('testando')