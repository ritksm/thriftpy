# -*- coding: utf-8 -*-

from __future__ import absolute_import

from thriftpy.thrift import TPayload, TException

import thriftpy
thriftpy.install_import_hook()

import addressbook as ab
import addressbook_thrift as ab_tt
import storm
import storm_thrift as storm_tt


def test_load_const():
    assert ab.DEFAULT_LIST_SIZE == ab_tt.DEFAULT_LIST_SIZE


def test_load_enum():
    assert ab.PhoneType.MOBILE == ab_tt.PhoneType.MOBILE
    assert ab.PhoneType.HOME == ab_tt.PhoneType.HOME
    assert ab.PhoneType.WORK == ab_tt.PhoneType.WORK


def test_load_struct():
    assert ab_tt.PhoneNumber.__base__ == TPayload
    assert ab.PhoneNumber.thrift_spec == ab_tt.PhoneNumber.thrift_spec

    assert storm_tt.NullStruct.__base__ == TPayload
    assert storm.NullStruct.thrift_spec == storm_tt.NullStruct.thrift_spec

    # TODO make this work
    # assert ab_tt.Person.__base__ == TPayload
    # assert ab.Person.thrift_spec == ab_tt.Person.thrift_spec

    # assert ab_tt.AddressBook.__base__ == TPayload
    # assert ab.AddressBook.thrift_spec == ab_tt.AddressBook.thrift_spec


def test_load_union():
    assert storm_tt.JavaObjectArg.__base__ == TPayload
    assert storm.JavaObjectArg.thrift_spec == \
        storm_tt.JavaObjectArg.thrift_spec


def test_load_exc():
    assert ab_tt.PersonNotExistsError.__base__ == TException
    assert ab.PersonNotExistsError.thrift_spec == \
        ab_tt.PersonNotExistsError.thrift_spec


def test_load_service():
    assert not set(ab.AddressBookService.thrift_services).difference(
        ab_tt.AddressBookService.thrift_services)
