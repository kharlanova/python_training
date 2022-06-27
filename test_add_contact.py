# -*- coding: utf-8 -*-

import pytest
from contact_information import Contact_information
from application_contact import Application_contact


@pytest.fixture
def app(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_add_contact(app):
    app.open_home_page()
    app.login()
    app.add_new_contact()
    app.contact_information(Contact_information(firstname="Ivan", middlename="Ivanovich", lastname="Petrov", nickname="iv", title="123", company="Petrov", address="Spb", home="8123456778", mobile="79117685656", work="79871234567", fax="123", email="iv@gmail.com", email2="vi@mail.com", email3="bn@mail.com", bday="1" , bmonth = "January", byear = "1980", aday = "9", amonth = "October", ayear = "2000", address2 = "Spb Fontanka", phone2 = "11",notes = "11"))
    app.logout()








