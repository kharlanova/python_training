from model.contact import Contact
from random import randrange
def test_modify_contact(app):
    if app.contact.count()==0:
        app.contact.contact_information(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Petrov", nickname="iv", title="123", company="Petrov", address="Spb", home="8123456778", mobile="79117685656", work="79871234567", fax="123", email="iv@gmail.com", email2="vi@mail.com", email3="bn@mail.com", bday="1" , bmonth = "January", byear = "1980", aday = "9", amonth = "October", ayear = "2000", address2 = "Spb Fontanka", phone2 = "11",notes = "11"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="123", middlename="Ivanovich123", lastname="Petrov", nickname="iv", title="123",
                company="Petrov", address="Spb", home="8123456778", mobile="79117685656", work="79871234567", fax="123",
                email="iv@gmail.com", email2="vi@mail.com", email3="bn@mail.com", bday="1", bmonth="January",
                byear="1980", aday="9", amonth="October", ayear="2000", address2="Spb Fontanka", phone2="11",
                notes="11")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index,contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)