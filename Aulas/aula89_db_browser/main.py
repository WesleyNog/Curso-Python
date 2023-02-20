import class_agenda as CA
from pathlib import Path

data_base = Path(__file__).parent / 'agenda.db'

if __name__ == '__main__':
    agenda = CA.AgendaDB(data_base)
    agenda.seach('Maria')
    # agenda.listar()