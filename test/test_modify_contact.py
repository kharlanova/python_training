from model.contact import Contact
def test_modify_first_contact(app):
    if app.contact.count()==0:
        app.contact.contact_information(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Petrov", nickname="iv", title="123", company="Petrov", address="Spb", home="8123456778", mobile="79117685656", work="79871234567", fax="123", email="iv@gmail.com", email2="vi@mail.com", email3="bn@mail.com", bday="1" , bmonth = "January", byear = "1980", aday = "9", amonth = "October", ayear = "2000", address2 = "Spb Fontanka", phone2 = "11",notes = "11"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="123", middlename="Ivanovich123", lastname="Petrov", nickname="iv", title="123",
                company="Petrov", address="Spb", home="8123456778", mobile="79117685656", work="79871234567", fax="123",
                email="iv@gmail.com", email2="vi@mail.com", email3="bn@mail.com", bday="1", bmonth="January",
                byear="1980", aday="9", amonth="October", ayear="2000", address2="Spb Fontanka", phone2="11",
                notes="11")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)