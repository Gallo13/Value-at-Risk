# Jessica Gallo
# Created: 3/17/2019
# Last Modified: 5/05/2019
# Historical Simulation Method

# //////////////////////////////////
# | SETTINGS -> PROJECT INTERPRETER
# | ~ intrinio_sdk
# | ~ mysql_connector_python
# | ~ tkcalander
# /////////////////////////////////

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +  KEY +
# +     DATA FROM USER        | USER INPUT          | API            | DB
# +    -----------------------|---------------------|-----------------------------------
# +     TICKER DATA 1         | ticker1_value    -> | identifier1 -> | ticker_1
# +     TICKER DATA 2         | ticker2_value    -> | identifier2 -> | ticker_2
# +     START DATE DATA       | start_date_entry -> | start_date  -> | db_start_date1(2)
# +     END DATE DATA         | end_date_entry   -> | end_date    -> | db_end_date1(2)
# +     CONFIDENCE LEVEL DATA | conf_value       -> | NA             |
# +
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ======================================================================================================================
# ##### IMPORTS #####
# ======================================================================================================================
# ------------
# TKINTER GUI
# ------------
from __future__ import print_function  # take out once DB is finished

from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk  # for date entry
from tkinter import messagebox
# ------------------
# Intrinio API
# ------------------
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint  # take out when DB is finished
# ---------
# MySQL DB
# ---------
import datetime
import mysql.connector
from mysql.connector import errorcode

# for calendar: https://buildmedia.readthedocs.org/media/pdf/tkcalendar/stable/tkcalendar.pdf

# ======================================================================================================================
# ##### WINDOW SETTINGS #####
# ======================================================================================================================
window = Tk()   # parent is called window
window.title("Historical Simulation Method App")  # sets title in white as HSM App
window.geometry("370x624")  # sets the window to 370 pixels by 590 pixels
window.resizable(0, 0)  # cant resize window
window.configure(background="#42647f")  # sets window background color as blue

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ======================================================================================================================
# ##### INPUT SECTION ##################################################################################################
# ======================================================================================================================
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# ======================================================================================================================
# ##### HEADER #####
# ======================================================================================================================
header_lbl = Label(window,
                   background="#42647f",
                   foreground="gold",
                   text="Historical Method for VaR: ",
                   font=("Dubai Bold", 14),
                   padx=15, pady=15)
header_lbl.grid(columnspan=4, sticky=W+E)  # allows text to expand 4 columns to put it in the middle of the window

# ======================================================================================================================
# ##### TICKER TEXT #####
# ======================================================================================================================


# ----------
# CAPS ONLY
# ----------
def caps(event):
    ticker1_value.set(ticker1_value.get().upper())  # sets anything written in the ticker entry box to all caps


def caps2(event):
    ticker2_value.set(ticker2_value.get().upper())


# -------------
# TICKER LABEL
# -------------
ticker1_lbl = Label(window,
                    background="#42647f",
                    foreground="gold",
                    text="Enter tickers: ",
                    font=("Dubai", 14),
                    padx=10, pady=2)
ticker1_lbl.grid(column=0, row=1, sticky=W)

# ---------------
# TICKER BOX 1
# ---------------
ticker1_value = StringVar()  # makes the textvariable called ticker_value a string
ticker1_txt = Entry(window,
                    width=14,
                    bg="alice blue",
                    textvariable=ticker1_value)
ticker1_txt.grid(column=1, row=1)
ticker1_txt.bind("<KeyRelease>", caps)
ticker1_txt.focus()  # makes the ticker entry box the focus

# -------------
# TICKER BOX 2
# -------------
ticker2_value = StringVar()  # makes the textvariable called ticker_value a string
ticker2_txt = Entry(window,
                    width=14,
                    bg="alice blue",
                    textvariable=ticker2_value)
ticker2_txt.grid(column=1, row=2, pady=8)
ticker2_txt.bind("<KeyRelease>", caps2)
ticker2_txt.focus()  # makes the ticker entry box the focus

# ======================================================================================================================
# ##### START DATE #####
# ======================================================================================================================
# -----------------
# START DATE LABEL
# -----------------
start_lbl = Label(window,
                  background="#42647f",
                  foreground="gold",
                  text="Enter start date: ",
                  font=("Dubai", 14),
                  padx=10, pady=5)
start_lbl.grid(column=0, row=3, sticky=W)

# ------------------
# START DATE PICKER
# ------------------
style = ttk.Style()
style.theme_use('clam')
style.configure('my.DateEntry',
                fieldbackground='alice blue',
                background='light steel blue',
                foreground='black',
                arrowcolor='black')
start_date_entry = DateEntry(style='my.DateEntry')
start_date_entry.grid(column=1, row=3)
start_date_entry.bind("<<DateEntrySelected>>")  # gets the date selected

# ======================================================================================================================
# ###### END DATE #####
# ======================================================================================================================
# ---------------
# END DATE LABEL
# ---------------
end_lbl = Label(window,
                background="#42647f",
                foreground="gold",
                text="Enter end date: ",
                font=("Dubai", 14),
                padx=10, pady=5)
end_lbl.grid(column=0, row=4, sticky=W)

# ----------------
# END DATE PICKER
# ----------------
style = ttk.Style()
style.theme_use('clam')  # -> uncomment this line if the styling does not work
style.configure('my.DateEntry',
                fieldbackground='alice blue',
                background='light steel blue',
                foreground='black',
                arrowcolor='black')
end_date_entry = DateEntry(style='my.DateEntry')
end_date_entry.grid(column=1, row=4)
end_date_entry.bind("<<DateEntrySelected>>")

# ======================================================================================================================
# ##### CONFIDENCE LEVEL #####
# ======================================================================================================================
# -----------------------
# CONFIDENCE LEVEL LABEL
# -----------------------
conf_lbl = Label(window,
                 background="#42647f",
                 foreground="gold",
                 text="Enter confidence level: ",
                 font=("Dubai", 14),
                 padx=10, pady=5)
conf_lbl.grid(column=0, row=5, sticky=W)

# ---------------------
# CONFIDENCE LEVEL BOX
# ---------------------
conf_value = IntVar()
conf_value.set(95)
conf_txt = Entry(window,
                 width=14,
                 bg="alice blue",
                 textvariable=conf_value)
conf_txt.grid(column=1, row=5)

# -----------------------------
# PERCENT SIGN AFTER ENTRY BOX
# -----------------------------
percent_lbl = Label(window,
                    background="#42647f",
                    foreground="gold",
                    text="%",
                    font=("Dubai", 14))
percent_lbl.grid(column=1, row=5, sticky=E)

# ------------
# BLANK SPACE
# ------------
blank_lbl = Label(window, background="#42647f", text="")
blank_lbl.grid(row=6)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ======================================================================================================================
# ##### RESULTS SECTION ################################################################################################
# ======================================================================================================================
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# ---------------------
# FRAME AROUND RESULTS
# ---------------------
labelframe = LabelFrame(window,
                        background="#42647f",
                        foreground="gold",
                        text="Results",
                        font=("Dubai", 14),
                        cursor="bogosity",
                        relief="raised")
labelframe.grid(columnspan=4, sticky=W+E, padx=15)

# -------
# WE ARE
# -------
result1_lbl = Label(labelframe,
                    background="#42647f",
                    foreground="gold",
                    text="We are       ",
                    font=("Dubai", 14),
                    padx=5, pady=5)
result1_lbl.grid(column=0, row=0)

# -----------------------
# ----- PERCENT BOX -----
# -----------------------
percent_value = IntVar()
percent_value.set("")
percent_result_txt = Entry(labelframe,
                           width=10,
                           state="readonly",
                           textvariable=percent_value,
                           cursor="pirate")
percent_result_txt.grid(column=0, row=0, sticky=E)

# ---------------
# % CERTAIN THAT
# ---------------
result2_lbl = Label(labelframe,
                    background="#42647f",
                    foreground="gold",
                    text="%  certain that",
                    font=("Dubai", 14),
                    padx=5, pady=5)
result2_lbl.grid(column=1, row=0, sticky=W)

# ----------
# THE VALUE
# ----------
result3_lbl = Label(labelframe,
                    background="#42647f",
                    foreground="gold",
                    text="the value     ",
                    font=("Dubai", 14),
                    padx=5, pady=5)
result3_lbl.grid(column=0, row=1)

# -------
# OF THE
# -------
result4_lbl = Label(labelframe,
                    background="#42647f",
                    foreground="gold",
                    text="of the",
                    font=("Dubai", 14),
                    pady=5)
result4_lbl.grid(column=0, row=1, sticky=E)

# -------------------
# PORTFOLIO WILL NOT
# -------------------
result5_lbl = Label(labelframe,
                    background="#42647f",
                    foreground="gold",
                    text="portfolio will not",
                    font=("Dubai", 14),
                    pady=5)
result5_lbl.grid(column=1, row=1, sticky=W)

# ---------------
# DROP MORE THAN
# ---------------
result3_lbl = Label(labelframe,
                    background="#42647f",
                    foreground="gold",
                    text="       drop more than ",
                    font=("Dubai", 14),
                    pady=5)
result3_lbl.grid(column=0, row=2)

# -----------------------------------
# ----- VALUE OF THE RESULT BOX -----
# -----------------------------------
result_value = IntVar()
result_value.set("")
value_result_txt = Entry(labelframe,
                         width=10,
                         state="readonly",
                         textvariable=result_value,
                         cursor="pirate")
value_result_txt.grid(column=1, row=2, sticky=W)

# ---------
# OVER THE
# ---------
result6_lbl = Label(labelframe,
                    background="#42647f",
                    foreground="gold",
                    text="over the",
                    font=("Dubai", 14),
                    padx=5, pady=5)
result6_lbl.grid(column=1, row=2, sticky=E)

# -----
# NEXT
# -----
result7_lbl = Label(labelframe,
                    background="#42647f",
                    foreground="gold",
                    text="next  ",
                    font=("Dubai", 14),
                    padx=5, pady=5)
result7_lbl.grid(column=0, row=3)

# ------------------------------
# ----- N TRADING DAYS BOX -----
# ------------------------------
trading_days = IntVar()
trading_days.set("")
trading_days_result_txt = Entry(labelframe,
                                width=10,
                                state="readonly",
                                textvariable=trading_days,
                                cursor="pirate")
trading_days_result_txt.grid(column=0, row=3, sticky=E)

# -------------
# TRADING DAYS
# -------------
result8_lbl = Label(labelframe,
                    background="#42647f",
                    foreground="gold",
                    text="trading days.",
                    font=("Dubai", 14),
                    padx=5, pady=5)
result8_lbl.grid(column=1, row=3, sticky=W)

# -------------
# BLANK SPACES
# -------------
blank2_lbl = Label(labelframe, background="#42647f", text="")
blank2_lbl.grid(row=4)

blank3_lbl = Label(window, background="#42647f", text="")
blank3_lbl.grid(rowspan=3)

# ======================================================================================================================
# ##### DATA BASE ######################################################################################################
# ======================================================================================================================
# ---------------------
#  CONNECTING TO MYSQL
# ---------------------
try:
    cnx = mysql.connector.connect(user='root',
                                  password='InBocaAlLupo15',
                                  host='127.0.0.1',
                                  database='my_hsm_db')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        messagebox.showerror("Error", "Something is wrong with your user name or password")
        # error message box pops up with username or password is incorrect
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        messagebox.showerror("Error", "Database does not exist")
        # error message box pops up if it can't find the database

# ======================================================================================================================
# ##### INTRINIO STOCK API #############################################################################################
# ======================================================================================================================

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = 'OjllN2Y3MjljNzAzMzljMmYxMmViZTI4Mjg0YzFhYjc2'
# My API key from Intrinio to call the data

historical_data_api = intrinio_sdk.HistoricalDataApi()
# to get historical data

# ======================================================================================================================
# ##### DEFINING CALCULATE BUTTON ######################################################################################
# ======================================================================================================================


# WHAT CALCULATE BUTTON DOES
def OnCalc():
    # --------------------------------------
    # PUTS PERCENTAGE FROM USER INTO RESULTS
    # --------------------------------------
    percent_value.set(conf_value.get())

    # -------------------------
    # STOCK API VALUES TICKER 1
    # -------------------------
    identifier1 = ticker1_value.get()
    # str | An identifier for an entity such as a Company, Security, Index, etc
    # (Ticker, FIGI, ISIN, CUSIP, CIK, LEI, Intrinio ID)
    tag1 = 'adj_close_price'
    # str | An Intrinio data tag ID or code (<a href='https://data.intrinio.com/data-tags'>reference</a>)
    frequency1 = 'daily'
    # str | Return historical data in the given frequency (optional) (default to daily)
    start_date1 = start_date_entry.get_date()
    # date | Get historical data on or after this date (optional)
    end_date1 = end_date_entry.get_date()
    # date | Get historical date on or before this date (optional)
    sort_order1 = 'asc'
    # str | Sort by date `asc` or `desc` (optional) (default to desc)
    next_page1 = ''
    # str | Gets the next page of data from a previous API call (optional)

    # --------------------------
    # GETTING STOCK API TICKER 1
    # --------------------------
    try:
        api_response1 = historical_data_api.get_historical_data(identifier1,
                                                                tag1,
                                                                frequency=frequency1,
                                                                start_date=start_date1,
                                                                end_date=end_date1,
                                                                sort_order=sort_order1,
                                                                next_page=next_page1)
        pprint(api_response1)  # take out when DB is created
    except ApiException as e:
        messagebox.showerror("Error", "Exception when calling HistoricalDataApi->get_historical_data: %s")
        # Error pop up message when data can't be collected from API

    # -------------------------
    # STOCK API VALUES TICKER 2
    # -------------------------
    identifier2 = ticker2_value.get()
    # str | An identifier for an entity such as a Company, Security, Index, etc
    # (Ticker, FIGI, ISIN, CUSIP, CIK, LEI, Intrinio ID)
    tag2 = 'adj_close_price'
    # str | An Intrinio data tag ID or code (<a href='https://data.intrinio.com/data-tags'>reference</a>)
    frequency2 = 'daily'
    # str | Return historical data in the given frequency (optional) (default to daily)
    start_date2 = start_date_entry.get_date()
    # date | Get historical data on or after this date (optional)
    end_date2 = end_date_entry.get_date()
    # date | Get historical date on or before this date (optional)
    sort_order2 = 'desc'
    # str | Sort by date `asc` or `desc` (optional) (default to desc)
    next_page2 = ''
    # str | Gets the next page of data from a previous API call (optional)

    # --------------------------
    # GETTING STOCK API TICKER 2
    # --------------------------
    try:
        api_response2 = historical_data_api.get_historical_data(identifier2,
                                                                tag2,
                                                                frequency=frequency2,
                                                                start_date=start_date2,
                                                                end_date=end_date2,
                                                                sort_order=sort_order2,
                                                                next_page=next_page2)
        pprint(api_response2)  # take out when DB is created => put this data into DB
    except ApiException as e:
        messagebox.showerror("Error", "Exception when calling HistoricalDataApi->get_historical_data: %s")
        # Error pop up message when data can't be collected from API

    # --------------------------------
    # PUTTING STOCK DATA INTO DATABASE
    # --------------------------------
    # def CanFindData(yes):
        # if the stock data already exists in stock_info_table, this pulls the numbers
        # if yes:

    start_date_entry.get_date()
    end_date_entry.get_date()

    try:
        cursor = cnx.cursor()

        # checks if info is already in database
        cursor.execute(
            "SELECT value_of_result "
            "FROM stock_info_tbl "
            "WHERE ticker_1 = %s and ticker_2 = %s and start_date = %s and end_date = %s, percent_value = %s",
            (identifier1, identifier2, start_date_entry, end_date_entry, percent_value)
        )

        # gets result from database
        result = cursor.fetchone()

        # puts result in entry box
        result_value.set(result)

        cursor.close()
        cnx.close()

        # if there are no records for the information, it will run through the process
        #else:
    except EXCEPTION:
        cursor2 = cnx.cursor()

        sql_stock_info = ("INSERT INTO stock_info_tbl "
                          "(id_stock, ticker_1, ticker_2, start_date, end_date) "  # add total_portfolio_value
                          " VALUES (%(id_stock)s,%(ticker_1)s, %(ticker_2)s, %(start_date_entry)s, "
                          "%(end_date_entry)s)")

        id_stock = cursor2.lastrowid
        # .lastrowid => auto increments id_stock since python disables auto increment

        data_stock = {
            'id_stock': id_stock,
            'ticker_1': identifier1,
            'ticker_2': identifier2,
            'start_date': start_date_entry,
            'end_date': end_date_entry,
        }

        # Puts data into the table
        cursor2.execute(sql_stock_info, data_stock)

        # Makes sure data is committed or saved to the database
        cnx.commit()

        # ----------------------------
        # TICKER_1_RETURN_OF_STOCK_TBL
        # ----------------------------
        # QUERYING DATES
        date_query1 = ("SELECT dates_1 FROM ticker_1_return_of_stock_tbl"
                       "WHERE dates_1 BETWEEN %s AND %s")

        db_start_date1 = start_date_entry
        db_end_date1 = end_date_entry

        cursor2.execute(date_query1, (db_start_date1, db_end_date1))

         # QUERYING CLOSING PRICES
        closing_price_query1 = ("SELECT closing_prices_1 FROM ticker_1_return_of_stock_tbl"
                                "WHERE closing_price_1 BETWEEN %s AND %s")

        db_closing_price_start1 = start_date1
        db_closing_price_end1 = end_date1

        cursor2.execute(closing_price_query1, (db_closing_price_start1, db_closing_price_end1))

        # ----------------------------
        # TICKER_2_RETURN_OF_STOCK_TBL
        # ----------------------------
        # QUERYING DATES
        date_query2 = ("SELECT dates_2 FROM ticker_2_return_of_stock_tbl"
                       "WHERE dates_2 BETWEEN %s AND %s")

        db_start_date2 = start_date_entry
        db_end_date2 = end_date_entry

        cursor2.execute(date_query2, (db_start_date2, db_end_date2))

        # QUERYING CLOSING PRICES
        closing_price_query2 = ("SELECT closing_prices_2 FROM ticker_2_return_of_stock_tbl"
                                "WHERE closing_price_2 BETWEEN %s AND %s")

        db_closing_price_start2 = start_date2
        db_closing_price_end2 = end_date2

        cursor2.execute(closing_price_query2, (db_closing_price_start2, db_closing_price_end2))

        # cnx.commit()

        # --------------
        # CONFIDENCE_TBL
        # --------------

        sql_conf_perc = ("INSERT INTO confidence_tbl "
                         "(conf_percent) "
                         " VALUES (%s)")

        conf_perc = percent_value

        # Puts data into the table
        cursor2.execute(sql_conf_perc, conf_perc)

        # COUNTS THE NUMBER OF ROWS TO GET THE NUMBER OF DAYS WITHIN THE PERIOD
        number_of_rows = cursor2.execute("SELECT number_of_shares_1 FROM ticker_1_weight_tbl")

        # PUTTING THE AMOUNT OF ROWS INTO THE TRADING DAYS BOX IN RESULTS
        trading_days.set(number_of_rows)

        cursor2.close()
        cnx.close()

    # CanFindData(yes)

# ======================================================================================================================
# ##### DEFINING CLEAR BUTTON ##########################################################################################
# ======================================================================================================================


# WHAT CLEAR BUTTON DOES
def OnClear():
    # Deletes boxes
    # -- INPUT SECTION --
    ticker1_txt.delete(0, END)
    ticker2_txt.delete(0, END)
    conf_txt.delete(0, END)
    # -- RESULTS SECTION --
    # percent box
    percent_result_txt.configure(state="normal")
    percent_result_txt.delete(0, END)
    percent_result_txt.configure(state="readonly")
    # value result box
    value_result_txt.configure(state="normal")
    value_result_txt.delete(0, END)
    value_result_txt.configure(state="readonly")
    # trading days box
    trading_days_result_txt.configure(state="normal")
    trading_days_result_txt.delete(0, END)
    trading_days_result_txt.configure(state="readonly")

    ticker1_txt.focus()
    # focuses on ticker text box after pressed


# ======================================================================================================================
# ##### CALCULATE BUTTON #####
# ======================================================================================================================
calc_btn = Button(window,
                  text="Calculate",
                  command=OnCalc,
                  font=("Dubai Bold", 13),
                  bg="alice blue",
                  fg="black",
                  padx=7,
                  cursor="hand2")
calc_btn.grid(column=1, row=12, sticky=W)

# ======================================================================================================================
# ##### CLEAR BUTTON #####
# ======================================================================================================================
clear_btn = Button(window,
                   text="Clear",
                   command=OnClear,
                   font=("Dubai Bold", 13),
                   bg="alice blue",
                   fg="black",
                   padx=7,
                   cursor="hand2")
clear_btn.grid(column=2, row=12, sticky=E)

# ======================================================================================================================
# ##### WINDOW #####
# ======================================================================================================================
window.mainloop()