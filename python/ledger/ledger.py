# -*- coding: utf-8 -*-
from datetime import datetime


COLUMN_WIDTHS = [10, 25, 13]

class LedgerEntry:
    def __init__(self, date, description, change):
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.description = description
        self.change = change


def create_entry(date, description, change):
    return LedgerEntry(date, description, change)


def format_date(date, locale):
    if locale == 'en_US':
        return date.strftime('%m/%d/%Y')
    elif locale == 'nl_NL':
        return date.strftime('%d-%m-%Y')


def make_header(locale):
    column_names = {
        'en_US' : ['Date', 'Description', 'Change'],
        'nl_NL' : ['Datum', 'Omschrijving', 'Verandering']
    }
    columns = [column_name.ljust(column_width) for column_name, column_width in zip(column_names[locale], COLUMN_WIDTHS)]
    return ' | '.join(columns)


def format_change(change, currency, locale):
    sigil = {'USD':'$', 'EUR':u'€'}
    if locale == 'en_US':
        money = sigil[currency] + '{:,.2f}'.format(abs(change/100))
        if change < 0:
            money = '(' + money + ')'
        else:
            money = ' ' + money + ' '
        return money
    elif locale == 'nl_NL':
        money = sigil[currency] + ' ' + '{:,.2f} '.format(change/100)
        money = money.translate(str.maketrans('.,',',.'))
        return money


def truncate(description):
    if len(description) > COLUMN_WIDTHS[1]:
        description = description[:COLUMN_WIDTHS[1]-3] + '...'
    return description


def make_row(entry, currency, locale):
    column_data = [format_date(entry.date, locale), truncate(entry.description), format_change(entry.change, currency, locale)]
    columns = [
                column_data[0].ljust(COLUMN_WIDTHS[0]),
                column_data[1].ljust(COLUMN_WIDTHS[1]),
                column_data[2].rjust(COLUMN_WIDTHS[2])
    ]
    return ' | '.join(columns)


def format_entries(currency, locale, entries):
    table = [make_header(locale)]
    entries.sort(key=lambda x:x.change)
    entries.sort(key=lambda x:x.date)
    for entry in entries:
        table.append(make_row(entry, currency, locale))
    return '\n'.join(table)
