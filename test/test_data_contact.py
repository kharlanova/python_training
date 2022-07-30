import re
from random import randrange


def test_data_contact_on_home_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_home = contacts[index]
    contact_edit = app.contact.get_contact_info_from_edit_page(index)
    assert contact_home.firstname.rstrip(" ") == contact_edit.firstname.rstrip(" ")
    assert contact_home.lastname.rstrip(" ") == contact_edit.lastname.rstrip(" ")
    assert contact_home.address.rstrip(" ") == contact_edit.address.rstrip(" ")
    assert contact_home.all_emails_from_home_page == merge_emails_like_on_home_page(contact_edit)
    assert contact_home.all_phones_from_home_page == merge_phones_like_on_home_page(contact_edit)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x:x is not None and len(x) > 0,
                                       [contact.email, contact.email2, contact.email3]))

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x:x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


