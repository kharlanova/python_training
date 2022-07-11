from model.contact import Contact
def test_update_first_contact(app):
    app.contact.update_first_contact(
        Contact(firstname="Ivan", middlename="Ivanovich123", lastname="Petrov", nickname="iv", title="123",
                company="Petrov", address="Spb", home="8123456778", mobile="79117685656", work="79871234567", fax="123",
                email="iv@gmail.com", email2="vi@mail.com", email3="bn@mail.com", bday="1", bmonth="January",
                byear="1980", aday="9", amonth="October", ayear="2000", address2="Spb Fontanka", phone2="11",
                notes="11"))

